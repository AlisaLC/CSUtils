from demoparser2 import DemoParser


class DemoAnalyzer:
    def __init__(self, demo_file):
        self.parser = DemoParser(demo_file)

        self.map_name = self.parser.parse_header()['map_name']

        self.player_info = self.parser.parse_player_info().set_index('steamid')

        self.tick_to_round = self.parser.parse_ticks(
            ["total_rounds_played"]
        ).groupby(
            ['total_rounds_played'], as_index=False
        ).agg(
            first_tick=('tick', 'first'),
            last_tick=('tick', 'last'),
        )

        self.grenades = self.__parse_grenades()

    def __parse_grenades(self):
        grenades = self.parser.parse_grenades()
        grenades.sort_values(by=['tick'], inplace=True)
        grenades = grenades.groupby(['thrower_steamid', 'grenade_type', 'entity_id'], as_index=False).agg(
            first_tick=('tick', 'first'),
            last_tick=('tick', 'last'),
            first_X=('X', 'first'),
            last_X=('X', 'last'),
            first_Y=('Y', 'first'),
            last_Y=('Y', 'last'),
            first_Z=('Z', 'first'),
            last_Z=('Z', 'last'),
        )
        grenades.drop_duplicates(inplace=True)
        grenades = grenades.join(self.player_info, on='thrower_steamid')
        grenades.drop(columns=['team_number'], inplace=True)
        grenades.reset_index(drop=True, inplace=True)
        grenades.sort_values(by=['first_tick', 'last_tick'], inplace=True)
        grenades = grenades[[
            'name', 'grenade_type', 'entity_id',
            'first_tick', 'last_tick',
            'first_X', 'last_X',
            'first_Y', 'last_Y',
            'first_Z', 'last_Z',
            'thrower_steamid'
        ]]
        grenades['round'] = grenades['first_tick'].apply(
            lambda x: self.tick_to_round[self.tick_to_round['first_tick'] < x]['total_rounds_played'].max() + 1
        )
        return grenades
