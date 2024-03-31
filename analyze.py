from demoparser2 import DemoParser
import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='CS2 Demo Analyzer')
    arg_parser.add_argument('demo_file', type=str, help='CS2 demo file')
    args = arg_parser.parse_args()

    parser = DemoParser(args.demo_file)
    df = parser.parse_event("player_death", player=["last_place_name", "team_name"], other=["total_rounds_played", "is_warmup_period"])
    df = df[df["attacker_team_name"] != df["user_team_name"]]
    df = df[df["is_warmup_period"] == False]
    df = df.groupby(["attacker_name", "total_rounds_played"]).size().to_frame(name='round_kills').reset_index()
    df = df.sort_values(by=["attacker_name", "total_rounds_played"])
    df['total_kills'] = df.groupby('attacker_name')['round_kills'].cumsum()
    df['round_kills'] = df['round_kills'].apply(lambda x: '*' * x)
    df.to_csv('results/output.csv', index=False)
