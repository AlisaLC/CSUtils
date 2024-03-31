import steammessages_pb2 as _steammessages_pb2
import engine_gcmessages_pb2 as _engine_gcmessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ECsgoGCMsg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMsgGCCStrike15_v2_Base: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingStart: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingStop: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingClient2ServerPing: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingGC2ServerReserve: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingServerReservationResponse: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientReserve: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingServerRoundStats: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingClient2GCHello: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientHello: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingServerMatchEnd: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingServer2GCKick: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingGCOperationalStats: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingGC2ServerRankUpdate: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ServerNotificationForUserPenalty: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientReportPlayer: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientReportServer: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientCommendPlayer: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientReportResponse: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientCommendPlayerQuery: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientCommendPlayerQueryResponse: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_WatchInfoUsers: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientRequestPlayersProfile: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_PlayersProfile: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_PlayerOverwatchCaseStatus: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GC2ClientTextMsg: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Client2GCTextMsg: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchEndRunRewardDrops: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchEndRewardDropsNotification: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientRequestWatchInfoFriends2: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchList: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchListRequestRecentUserGames: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GC2ServerReservationUpdate: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientVarValueNotificationInfo: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_TournamentMatchRewardDropsNotification: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchListRequestTournamentGames: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchListRequestFullGameInfo: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GiftsLeaderboardRequest: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GiftsLeaderboardResponse: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ServerVarValueNotificationInfo: _ClassVar[ECsgoGCMsg]
    k_EMsgGCToGCReloadVersions: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientSubmitSurveyVote: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Server2GCClientValidate: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchListRequestLiveGameForUser: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Server2GCPureServerValidationFailure: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_AccountPrivacySettings: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_SetMyActivityInfo: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchListRequestTournamentPredictions: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchListUploadTournamentPredictions: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_DraftSummary: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientRequestJoinFriendData: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientRequestJoinServerData: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientRequestNewMission: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GC2ServerNotifyXPRewarded: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GC2ClientTournamentInfo: _ClassVar[ECsgoGCMsg]
    k_EMsgGC_GlobalGame_Subscribe: _ClassVar[ECsgoGCMsg]
    k_EMsgGC_GlobalGame_Unsubscribe: _ClassVar[ECsgoGCMsg]
    k_EMsgGC_GlobalGame_Play: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_AcknowledgePenalty: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GC2ClientGlobalStats: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Client2GCStreamUnlock: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_FantasyRequestClientData: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_FantasyUpdateClientData: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GCToClientSteamdatagramTicket: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientToGCRequestTicket: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientToGCRequestElevate: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GlobalChat: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GlobalChat_Subscribe: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GlobalChat_Unsubscribe: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientAuthKeyCode: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GotvSyncPacket: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientPlayerDecalSign: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientLogonFatalError: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientPollState: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Party_Register: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Party_Unregister: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Party_Search: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Party_Invite: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_Account_RequestCoPlays: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientGCRankUpdate: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientRequestOffers: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientAccountBalance: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientPartyJoinRelay: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientPartyWarning: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_MatchmakingServerMatchEndPartial: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_SetEventFavorite: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GetEventFavorites_Request: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientPerfReport: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GetEventFavorites_Response: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientRequestSouvenir: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_ClientReportValidation: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GC2ClientRefuseSecureMode: _ClassVar[ECsgoGCMsg]
    k_EMsgGCCStrike15_v2_GC2ClientRequestValidation: _ClassVar[ECsgoGCMsg]

class ECsgoSteamUserStat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ECsgoSteamUserStat_XpEarnedGames: _ClassVar[ECsgoSteamUserStat]
    k_ECsgoSteamUserStat_MatchWinsCompetitive: _ClassVar[ECsgoSteamUserStat]
    k_ECsgoSteamUserStat_SurvivedDangerZone: _ClassVar[ECsgoSteamUserStat]
k_EMsgGCCStrike15_v2_Base: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingStart: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingStop: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingClient2ServerPing: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ServerReserve: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingServerReservationResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ClientReserve: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingServerRoundStats: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingClient2GCHello: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ClientHello: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingServerMatchEnd: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingServer2GCKick: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGCOperationalStats: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingGC2ServerRankUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ServerNotificationForUserPenalty: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientReportPlayer: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientReportServer: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientCommendPlayer: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientReportResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientCommendPlayerQuery: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientCommendPlayerQueryResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_WatchInfoUsers: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestPlayersProfile: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PlayersProfile: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment: ECsgoGCMsg
k_EMsgGCCStrike15_v2_PlayerOverwatchCaseStatus: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientTextMsg: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCTextMsg: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchEndRunRewardDrops: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchEndRewardDropsNotification: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestWatchInfoFriends2: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchList: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestRecentUserGames: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ServerReservationUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientVarValueNotificationInfo: ECsgoGCMsg
k_EMsgGCCStrike15_v2_TournamentMatchRewardDropsNotification: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestTournamentGames: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestFullGameInfo: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GiftsLeaderboardRequest: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GiftsLeaderboardResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ServerVarValueNotificationInfo: ECsgoGCMsg
k_EMsgGCToGCReloadVersions: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientSubmitSurveyVote: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Server2GCClientValidate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestLiveGameForUser: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Server2GCPureServerValidationFailure: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse: ECsgoGCMsg
k_EMsgGCCStrike15_v2_AccountPrivacySettings: ECsgoGCMsg
k_EMsgGCCStrike15_v2_SetMyActivityInfo: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListRequestTournamentPredictions: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchListUploadTournamentPredictions: ECsgoGCMsg
k_EMsgGCCStrike15_v2_DraftSummary: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestJoinFriendData: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestJoinServerData: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestNewMission: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ServerNotifyXPRewarded: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientTournamentInfo: ECsgoGCMsg
k_EMsgGC_GlobalGame_Subscribe: ECsgoGCMsg
k_EMsgGC_GlobalGame_Unsubscribe: ECsgoGCMsg
k_EMsgGC_GlobalGame_Play: ECsgoGCMsg
k_EMsgGCCStrike15_v2_AcknowledgePenalty: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientGlobalStats: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Client2GCStreamUnlock: ECsgoGCMsg
k_EMsgGCCStrike15_v2_FantasyRequestClientData: ECsgoGCMsg
k_EMsgGCCStrike15_v2_FantasyUpdateClientData: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GCToClientSteamdatagramTicket: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientToGCRequestTicket: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientToGCRequestElevate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GlobalChat: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GlobalChat_Subscribe: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GlobalChat_Unsubscribe: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientAuthKeyCode: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GotvSyncPacket: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPlayerDecalSign: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientLogonFatalError: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPollState: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Party_Register: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Party_Unregister: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Party_Search: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Party_Invite: ECsgoGCMsg
k_EMsgGCCStrike15_v2_Account_RequestCoPlays: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientGCRankUpdate: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestOffers: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientAccountBalance: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPartyJoinRelay: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPartyWarning: ECsgoGCMsg
k_EMsgGCCStrike15_v2_MatchmakingServerMatchEndPartial: ECsgoGCMsg
k_EMsgGCCStrike15_v2_SetEventFavorite: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GetEventFavorites_Request: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientPerfReport: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GetEventFavorites_Response: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientRequestSouvenir: ECsgoGCMsg
k_EMsgGCCStrike15_v2_ClientReportValidation: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientRefuseSecureMode: ECsgoGCMsg
k_EMsgGCCStrike15_v2_GC2ClientRequestValidation: ECsgoGCMsg
k_ECsgoSteamUserStat_XpEarnedGames: ECsgoSteamUserStat
k_ECsgoSteamUserStat_MatchWinsCompetitive: ECsgoSteamUserStat
k_ECsgoSteamUserStat_SurvivedDangerZone: ECsgoSteamUserStat

class GameServerPing(_message.Message):
    __slots__ = ("ping", "ip", "instances")
    PING_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    ping: int
    ip: int
    instances: int
    def __init__(self, ping: _Optional[int] = ..., ip: _Optional[int] = ..., instances: _Optional[int] = ...) -> None: ...

class DataCenterPing(_message.Message):
    __slots__ = ("data_center_id", "ping")
    DATA_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    data_center_id: int
    ping: int
    def __init__(self, data_center_id: _Optional[int] = ..., ping: _Optional[int] = ...) -> None: ...

class DetailedSearchStatistic(_message.Message):
    __slots__ = ("game_type", "search_time_avg", "players_searching")
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TIME_AVG_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_SEARCHING_FIELD_NUMBER: _ClassVar[int]
    game_type: int
    search_time_avg: int
    players_searching: int
    def __init__(self, game_type: _Optional[int] = ..., search_time_avg: _Optional[int] = ..., players_searching: _Optional[int] = ...) -> None: ...

class TournamentPlayer(_message.Message):
    __slots__ = ("account_id", "player_nick", "player_name", "player_dob", "player_flag", "player_location", "player_desc")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NICK_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DOB_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FLAG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DESC_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    player_nick: str
    player_name: str
    player_dob: int
    player_flag: str
    player_location: str
    player_desc: str
    def __init__(self, account_id: _Optional[int] = ..., player_nick: _Optional[str] = ..., player_name: _Optional[str] = ..., player_dob: _Optional[int] = ..., player_flag: _Optional[str] = ..., player_location: _Optional[str] = ..., player_desc: _Optional[str] = ...) -> None: ...

class TournamentTeam(_message.Message):
    __slots__ = ("team_id", "team_tag", "team_flag", "team_name", "players")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_TAG_FIELD_NUMBER: _ClassVar[int]
    TEAM_FLAG_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    team_tag: str
    team_flag: str
    team_name: str
    players: _containers.RepeatedCompositeFieldContainer[TournamentPlayer]
    def __init__(self, team_id: _Optional[int] = ..., team_tag: _Optional[str] = ..., team_flag: _Optional[str] = ..., team_name: _Optional[str] = ..., players: _Optional[_Iterable[_Union[TournamentPlayer, _Mapping]]] = ...) -> None: ...

class TournamentEvent(_message.Message):
    __slots__ = ("event_id", "event_tag", "event_name", "event_time_start", "event_time_end", "event_public", "event_stage_id", "event_stage_name", "active_section_id")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TAG_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_START_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_END_FIELD_NUMBER: _ClassVar[int]
    EVENT_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    EVENT_STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    event_tag: str
    event_name: str
    event_time_start: int
    event_time_end: int
    event_public: int
    event_stage_id: int
    event_stage_name: str
    active_section_id: int
    def __init__(self, event_id: _Optional[int] = ..., event_tag: _Optional[str] = ..., event_name: _Optional[str] = ..., event_time_start: _Optional[int] = ..., event_time_end: _Optional[int] = ..., event_public: _Optional[int] = ..., event_stage_id: _Optional[int] = ..., event_stage_name: _Optional[str] = ..., active_section_id: _Optional[int] = ...) -> None: ...

class GlobalStatistics(_message.Message):
    __slots__ = ("players_online", "servers_online", "players_searching", "servers_available", "ongoing_matches", "search_time_avg", "search_statistics", "main_post_url", "required_appid_version", "pricesheet_version", "twitch_streams_version", "active_tournament_eventid", "active_survey_id", "rtime32_cur", "rtime32_event_start")
    PLAYERS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    SERVERS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_SEARCHING_FIELD_NUMBER: _ClassVar[int]
    SERVERS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ONGOING_MATCHES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TIME_AVG_FIELD_NUMBER: _ClassVar[int]
    SEARCH_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    MAIN_POST_URL_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPID_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRICESHEET_VERSION_FIELD_NUMBER: _ClassVar[int]
    TWITCH_STREAMS_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TOURNAMENT_EVENTID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SURVEY_ID_FIELD_NUMBER: _ClassVar[int]
    RTIME32_CUR_FIELD_NUMBER: _ClassVar[int]
    RTIME32_EVENT_START_FIELD_NUMBER: _ClassVar[int]
    players_online: int
    servers_online: int
    players_searching: int
    servers_available: int
    ongoing_matches: int
    search_time_avg: int
    search_statistics: _containers.RepeatedCompositeFieldContainer[DetailedSearchStatistic]
    main_post_url: str
    required_appid_version: int
    pricesheet_version: int
    twitch_streams_version: int
    active_tournament_eventid: int
    active_survey_id: int
    rtime32_cur: int
    rtime32_event_start: int
    def __init__(self, players_online: _Optional[int] = ..., servers_online: _Optional[int] = ..., players_searching: _Optional[int] = ..., servers_available: _Optional[int] = ..., ongoing_matches: _Optional[int] = ..., search_time_avg: _Optional[int] = ..., search_statistics: _Optional[_Iterable[_Union[DetailedSearchStatistic, _Mapping]]] = ..., main_post_url: _Optional[str] = ..., required_appid_version: _Optional[int] = ..., pricesheet_version: _Optional[int] = ..., twitch_streams_version: _Optional[int] = ..., active_tournament_eventid: _Optional[int] = ..., active_survey_id: _Optional[int] = ..., rtime32_cur: _Optional[int] = ..., rtime32_event_start: _Optional[int] = ...) -> None: ...

class OperationalStatisticDescription(_message.Message):
    __slots__ = ("name", "idkey")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDKEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    idkey: int
    def __init__(self, name: _Optional[str] = ..., idkey: _Optional[int] = ...) -> None: ...

class OperationalStatisticElement(_message.Message):
    __slots__ = ("idkey", "values")
    IDKEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    idkey: int
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, idkey: _Optional[int] = ..., values: _Optional[_Iterable[int]] = ...) -> None: ...

class OperationalStatisticsPacket(_message.Message):
    __slots__ = ("packetid", "mstimestamp", "values")
    PACKETID_FIELD_NUMBER: _ClassVar[int]
    MSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    packetid: int
    mstimestamp: int
    values: _containers.RepeatedCompositeFieldContainer[OperationalStatisticElement]
    def __init__(self, packetid: _Optional[int] = ..., mstimestamp: _Optional[int] = ..., values: _Optional[_Iterable[_Union[OperationalStatisticElement, _Mapping]]] = ...) -> None: ...

class PlayerRankingInfo(_message.Message):
    __slots__ = ("account_id", "rank_id", "wins", "rank_change", "rank_type_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_ID_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    RANK_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RANK_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    rank_id: int
    wins: int
    rank_change: float
    rank_type_id: int
    def __init__(self, account_id: _Optional[int] = ..., rank_id: _Optional[int] = ..., wins: _Optional[int] = ..., rank_change: _Optional[float] = ..., rank_type_id: _Optional[int] = ...) -> None: ...

class PlayerCommendationInfo(_message.Message):
    __slots__ = ("cmd_friendly", "cmd_teaching", "cmd_leader")
    CMD_FRIENDLY_FIELD_NUMBER: _ClassVar[int]
    CMD_TEACHING_FIELD_NUMBER: _ClassVar[int]
    CMD_LEADER_FIELD_NUMBER: _ClassVar[int]
    cmd_friendly: int
    cmd_teaching: int
    cmd_leader: int
    def __init__(self, cmd_friendly: _Optional[int] = ..., cmd_teaching: _Optional[int] = ..., cmd_leader: _Optional[int] = ...) -> None: ...

class PlayerMedalsInfo(_message.Message):
    __slots__ = ("display_items_defidx", "featured_display_item_defidx")
    DISPLAY_ITEMS_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    FEATURED_DISPLAY_ITEM_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    display_items_defidx: _containers.RepeatedScalarFieldContainer[int]
    featured_display_item_defidx: int
    def __init__(self, display_items_defidx: _Optional[_Iterable[int]] = ..., featured_display_item_defidx: _Optional[int] = ...) -> None: ...

class AccountActivity(_message.Message):
    __slots__ = ("activity", "mode", "map", "matchid")
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    activity: int
    mode: int
    map: int
    matchid: int
    def __init__(self, activity: _Optional[int] = ..., mode: _Optional[int] = ..., map: _Optional[int] = ..., matchid: _Optional[int] = ...) -> None: ...

class TournamentMatchSetup(_message.Message):
    __slots__ = ("event_id", "team_id_ct", "team_id_t", "event_stage_id")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_CT_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_T_FIELD_NUMBER: _ClassVar[int]
    EVENT_STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    team_id_ct: int
    team_id_t: int
    event_stage_id: int
    def __init__(self, event_id: _Optional[int] = ..., team_id_ct: _Optional[int] = ..., team_id_t: _Optional[int] = ..., event_stage_id: _Optional[int] = ...) -> None: ...

class ServerHltvInfo(_message.Message):
    __slots__ = ("tv_udp_port", "tv_watch_key", "tv_slots", "tv_clients", "tv_proxies", "tv_time", "game_type", "game_mapgroup", "game_map", "tv_master_steamid", "tv_local_slots", "tv_local_clients", "tv_local_proxies", "tv_relay_slots", "tv_relay_clients", "tv_relay_proxies", "tv_relay_address", "tv_relay_port", "tv_relay_steamid", "flags")
    TV_UDP_PORT_FIELD_NUMBER: _ClassVar[int]
    TV_WATCH_KEY_FIELD_NUMBER: _ClassVar[int]
    TV_SLOTS_FIELD_NUMBER: _ClassVar[int]
    TV_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    TV_PROXIES_FIELD_NUMBER: _ClassVar[int]
    TV_TIME_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    GAME_MAPGROUP_FIELD_NUMBER: _ClassVar[int]
    GAME_MAP_FIELD_NUMBER: _ClassVar[int]
    TV_MASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    TV_LOCAL_SLOTS_FIELD_NUMBER: _ClassVar[int]
    TV_LOCAL_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    TV_LOCAL_PROXIES_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_SLOTS_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_PROXIES_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_PORT_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_STEAMID_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    tv_udp_port: int
    tv_watch_key: int
    tv_slots: int
    tv_clients: int
    tv_proxies: int
    tv_time: int
    game_type: int
    game_mapgroup: str
    game_map: str
    tv_master_steamid: int
    tv_local_slots: int
    tv_local_clients: int
    tv_local_proxies: int
    tv_relay_slots: int
    tv_relay_clients: int
    tv_relay_proxies: int
    tv_relay_address: int
    tv_relay_port: int
    tv_relay_steamid: int
    flags: int
    def __init__(self, tv_udp_port: _Optional[int] = ..., tv_watch_key: _Optional[int] = ..., tv_slots: _Optional[int] = ..., tv_clients: _Optional[int] = ..., tv_proxies: _Optional[int] = ..., tv_time: _Optional[int] = ..., game_type: _Optional[int] = ..., game_mapgroup: _Optional[str] = ..., game_map: _Optional[str] = ..., tv_master_steamid: _Optional[int] = ..., tv_local_slots: _Optional[int] = ..., tv_local_clients: _Optional[int] = ..., tv_local_proxies: _Optional[int] = ..., tv_relay_slots: _Optional[int] = ..., tv_relay_clients: _Optional[int] = ..., tv_relay_proxies: _Optional[int] = ..., tv_relay_address: _Optional[int] = ..., tv_relay_port: _Optional[int] = ..., tv_relay_steamid: _Optional[int] = ..., flags: _Optional[int] = ...) -> None: ...

class IpAddressMask(_message.Message):
    __slots__ = ("a", "b", "c", "d", "bits", "token")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    BITS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    c: int
    d: int
    bits: int
    token: int
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ..., c: _Optional[int] = ..., d: _Optional[int] = ..., bits: _Optional[int] = ..., token: _Optional[int] = ...) -> None: ...

class CMsgCsgoSteamUserStatChange(_message.Message):
    __slots__ = ("ecsgosteamuserstat", "delta", "absolute")
    ECSGOSTEAMUSERSTAT_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
    ecsgosteamuserstat: int
    delta: int
    absolute: bool
    def __init__(self, ecsgosteamuserstat: _Optional[int] = ..., delta: _Optional[int] = ..., absolute: bool = ...) -> None: ...

class XpProgressData(_message.Message):
    __slots__ = ("xp_points", "xp_category")
    XP_POINTS_FIELD_NUMBER: _ClassVar[int]
    XP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    xp_points: int
    xp_category: int
    def __init__(self, xp_points: _Optional[int] = ..., xp_category: _Optional[int] = ...) -> None: ...

class MatchEndItemUpdates(_message.Message):
    __slots__ = ("item_id", "item_attr_defidx", "item_attr_delta_value")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ATTR_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    ITEM_ATTR_DELTA_VALUE_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    item_attr_defidx: int
    item_attr_delta_value: int
    def __init__(self, item_id: _Optional[int] = ..., item_attr_defidx: _Optional[int] = ..., item_attr_delta_value: _Optional[int] = ...) -> None: ...

class ScoreLeaderboardData(_message.Message):
    __slots__ = ("quest_id", "score", "accountentries", "matchentries")
    class Entry(_message.Message):
        __slots__ = ("tag", "val")
        TAG_FIELD_NUMBER: _ClassVar[int]
        VAL_FIELD_NUMBER: _ClassVar[int]
        tag: int
        val: int
        def __init__(self, tag: _Optional[int] = ..., val: _Optional[int] = ...) -> None: ...
    class AccountEntries(_message.Message):
        __slots__ = ("accountid", "entries")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        entries: _containers.RepeatedCompositeFieldContainer[ScoreLeaderboardData.Entry]
        def __init__(self, accountid: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[ScoreLeaderboardData.Entry, _Mapping]]] = ...) -> None: ...
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTENTRIES_FIELD_NUMBER: _ClassVar[int]
    MATCHENTRIES_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    score: int
    accountentries: _containers.RepeatedCompositeFieldContainer[ScoreLeaderboardData.AccountEntries]
    matchentries: _containers.RepeatedCompositeFieldContainer[ScoreLeaderboardData.Entry]
    def __init__(self, quest_id: _Optional[int] = ..., score: _Optional[int] = ..., accountentries: _Optional[_Iterable[_Union[ScoreLeaderboardData.AccountEntries, _Mapping]]] = ..., matchentries: _Optional[_Iterable[_Union[ScoreLeaderboardData.Entry, _Mapping]]] = ...) -> None: ...

class PlayerQuestData(_message.Message):
    __slots__ = ("quester_account_id", "quest_item_data", "xp_progress_data", "time_played", "mm_game_mode", "item_updates", "operation_points_eligible", "userstatchanges")
    class QuestItemData(_message.Message):
        __slots__ = ("quest_id", "quest_normal_points_earned", "quest_bonus_points_earned")
        QUEST_ID_FIELD_NUMBER: _ClassVar[int]
        QUEST_NORMAL_POINTS_EARNED_FIELD_NUMBER: _ClassVar[int]
        QUEST_BONUS_POINTS_EARNED_FIELD_NUMBER: _ClassVar[int]
        quest_id: int
        quest_normal_points_earned: int
        quest_bonus_points_earned: int
        def __init__(self, quest_id: _Optional[int] = ..., quest_normal_points_earned: _Optional[int] = ..., quest_bonus_points_earned: _Optional[int] = ...) -> None: ...
    QUESTER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_ITEM_DATA_FIELD_NUMBER: _ClassVar[int]
    XP_PROGRESS_DATA_FIELD_NUMBER: _ClassVar[int]
    TIME_PLAYED_FIELD_NUMBER: _ClassVar[int]
    MM_GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    ITEM_UPDATES_FIELD_NUMBER: _ClassVar[int]
    OPERATION_POINTS_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    USERSTATCHANGES_FIELD_NUMBER: _ClassVar[int]
    quester_account_id: int
    quest_item_data: _containers.RepeatedCompositeFieldContainer[PlayerQuestData.QuestItemData]
    xp_progress_data: _containers.RepeatedCompositeFieldContainer[XpProgressData]
    time_played: int
    mm_game_mode: int
    item_updates: _containers.RepeatedCompositeFieldContainer[MatchEndItemUpdates]
    operation_points_eligible: bool
    userstatchanges: _containers.RepeatedCompositeFieldContainer[CMsgCsgoSteamUserStatChange]
    def __init__(self, quester_account_id: _Optional[int] = ..., quest_item_data: _Optional[_Iterable[_Union[PlayerQuestData.QuestItemData, _Mapping]]] = ..., xp_progress_data: _Optional[_Iterable[_Union[XpProgressData, _Mapping]]] = ..., time_played: _Optional[int] = ..., mm_game_mode: _Optional[int] = ..., item_updates: _Optional[_Iterable[_Union[MatchEndItemUpdates, _Mapping]]] = ..., operation_points_eligible: bool = ..., userstatchanges: _Optional[_Iterable[_Union[CMsgCsgoSteamUserStatChange, _Mapping]]] = ...) -> None: ...

class CMsgGC_ServerQuestUpdateData(_message.Message):
    __slots__ = ("player_quest_data", "binary_data", "mm_game_mode", "missionlbsdata")
    PLAYER_QUEST_DATA_FIELD_NUMBER: _ClassVar[int]
    BINARY_DATA_FIELD_NUMBER: _ClassVar[int]
    MM_GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    MISSIONLBSDATA_FIELD_NUMBER: _ClassVar[int]
    player_quest_data: _containers.RepeatedCompositeFieldContainer[PlayerQuestData]
    binary_data: bytes
    mm_game_mode: int
    missionlbsdata: ScoreLeaderboardData
    def __init__(self, player_quest_data: _Optional[_Iterable[_Union[PlayerQuestData, _Mapping]]] = ..., binary_data: _Optional[bytes] = ..., mm_game_mode: _Optional[int] = ..., missionlbsdata: _Optional[_Union[ScoreLeaderboardData, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGCOperationalStats(_message.Message):
    __slots__ = ("packetid", "namekeys", "packets")
    PACKETID_FIELD_NUMBER: _ClassVar[int]
    NAMEKEYS_FIELD_NUMBER: _ClassVar[int]
    PACKETS_FIELD_NUMBER: _ClassVar[int]
    packetid: int
    namekeys: _containers.RepeatedCompositeFieldContainer[OperationalStatisticDescription]
    packets: _containers.RepeatedCompositeFieldContainer[OperationalStatisticsPacket]
    def __init__(self, packetid: _Optional[int] = ..., namekeys: _Optional[_Iterable[_Union[OperationalStatisticDescription, _Mapping]]] = ..., packets: _Optional[_Iterable[_Union[OperationalStatisticsPacket, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm(_message.Message):
    __slots__ = ("token", "stamp", "exchange")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    STAMP_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    token: int
    stamp: int
    exchange: int
    def __init__(self, token: _Optional[int] = ..., stamp: _Optional[int] = ..., exchange: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ServerReservationUpdate(_message.Message):
    __slots__ = ("viewers_external_total", "viewers_external_steam")
    VIEWERS_EXTERNAL_TOTAL_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_EXTERNAL_STEAM_FIELD_NUMBER: _ClassVar[int]
    viewers_external_total: int
    viewers_external_steam: int
    def __init__(self, viewers_external_total: _Optional[int] = ..., viewers_external_steam: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingStart(_message.Message):
    __slots__ = ("account_ids", "game_type", "ticket_data", "client_version", "tournament_match", "prime_only")
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    TICKET_DATA_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PRIME_ONLY_FIELD_NUMBER: _ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    game_type: int
    ticket_data: str
    client_version: int
    tournament_match: TournamentMatchSetup
    prime_only: bool
    def __init__(self, account_ids: _Optional[_Iterable[int]] = ..., game_type: _Optional[int] = ..., ticket_data: _Optional[str] = ..., client_version: _Optional[int] = ..., tournament_match: _Optional[_Union[TournamentMatchSetup, _Mapping]] = ..., prime_only: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingStop(_message.Message):
    __slots__ = ("abandon",)
    ABANDON_FIELD_NUMBER: _ClassVar[int]
    abandon: int
    def __init__(self, abandon: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingClient2ServerPing(_message.Message):
    __slots__ = ("gameserverpings", "offset_index", "final_batch", "data_center_pings", "max_ping", "test_token")
    GAMESERVERPINGS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_INDEX_FIELD_NUMBER: _ClassVar[int]
    FINAL_BATCH_FIELD_NUMBER: _ClassVar[int]
    DATA_CENTER_PINGS_FIELD_NUMBER: _ClassVar[int]
    MAX_PING_FIELD_NUMBER: _ClassVar[int]
    TEST_TOKEN_FIELD_NUMBER: _ClassVar[int]
    gameserverpings: _containers.RepeatedCompositeFieldContainer[GameServerPing]
    offset_index: int
    final_batch: int
    data_center_pings: _containers.RepeatedCompositeFieldContainer[DataCenterPing]
    max_ping: int
    test_token: int
    def __init__(self, gameserverpings: _Optional[_Iterable[_Union[GameServerPing, _Mapping]]] = ..., offset_index: _Optional[int] = ..., final_batch: _Optional[int] = ..., data_center_pings: _Optional[_Iterable[_Union[DataCenterPing, _Mapping]]] = ..., max_ping: _Optional[int] = ..., test_token: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate(_message.Message):
    __slots__ = ("matchmaking", "waiting_account_id_sessions", "error", "ongoingmatch_account_id_sessions", "global_stats", "failping_account_id_sessions", "penalty_account_id_sessions", "failready_account_id_sessions", "vacbanned_account_id_sessions", "server_ipaddress_mask", "notes", "penalty_account_id_sessions_green", "insufficientlevel_sessions", "vsncheck_account_id_sessions", "launcher_mismatch_sessions")
    class Note(_message.Message):
        __slots__ = ("type", "region_id", "region_r", "distance")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_R_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        type: int
        region_id: int
        region_r: float
        distance: float
        def __init__(self, type: _Optional[int] = ..., region_id: _Optional[int] = ..., region_r: _Optional[float] = ..., distance: _Optional[float] = ...) -> None: ...
    MATCHMAKING_FIELD_NUMBER: _ClassVar[int]
    WAITING_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ONGOINGMATCH_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_STATS_FIELD_NUMBER: _ClassVar[int]
    FAILPING_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    PENALTY_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    FAILREADY_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    VACBANNED_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    SERVER_IPADDRESS_MASK_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PENALTY_ACCOUNT_ID_SESSIONS_GREEN_FIELD_NUMBER: _ClassVar[int]
    INSUFFICIENTLEVEL_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    VSNCHECK_ACCOUNT_ID_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_MISMATCH_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    matchmaking: int
    waiting_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    error: str
    ongoingmatch_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    global_stats: GlobalStatistics
    failping_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    penalty_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    failready_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    vacbanned_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    server_ipaddress_mask: IpAddressMask
    notes: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate.Note]
    penalty_account_id_sessions_green: _containers.RepeatedScalarFieldContainer[int]
    insufficientlevel_sessions: _containers.RepeatedScalarFieldContainer[int]
    vsncheck_account_id_sessions: _containers.RepeatedScalarFieldContainer[int]
    launcher_mismatch_sessions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, matchmaking: _Optional[int] = ..., waiting_account_id_sessions: _Optional[_Iterable[int]] = ..., error: _Optional[str] = ..., ongoingmatch_account_id_sessions: _Optional[_Iterable[int]] = ..., global_stats: _Optional[_Union[GlobalStatistics, _Mapping]] = ..., failping_account_id_sessions: _Optional[_Iterable[int]] = ..., penalty_account_id_sessions: _Optional[_Iterable[int]] = ..., failready_account_id_sessions: _Optional[_Iterable[int]] = ..., vacbanned_account_id_sessions: _Optional[_Iterable[int]] = ..., server_ipaddress_mask: _Optional[_Union[IpAddressMask, _Mapping]] = ..., notes: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate.Note, _Mapping]]] = ..., penalty_account_id_sessions_green: _Optional[_Iterable[int]] = ..., insufficientlevel_sessions: _Optional[_Iterable[int]] = ..., vsncheck_account_id_sessions: _Optional[_Iterable[int]] = ..., launcher_mismatch_sessions: _Optional[_Iterable[int]] = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentMatchDraft(_message.Message):
    __slots__ = ("event_id", "event_stage_id", "team_id_0", "team_id_1", "maps_count", "maps_current", "team_id_start", "team_id_veto1", "team_id_pickn", "drafts")
    class Entry(_message.Message):
        __slots__ = ("mapid", "team_id_ct")
        MAPID_FIELD_NUMBER: _ClassVar[int]
        TEAM_ID_CT_FIELD_NUMBER: _ClassVar[int]
        mapid: int
        team_id_ct: int
        def __init__(self, mapid: _Optional[int] = ..., team_id_ct: _Optional[int] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_0_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_1_FIELD_NUMBER: _ClassVar[int]
    MAPS_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAPS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_START_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_VETO1_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_PICKN_FIELD_NUMBER: _ClassVar[int]
    DRAFTS_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    event_stage_id: int
    team_id_0: int
    team_id_1: int
    maps_count: int
    maps_current: int
    team_id_start: int
    team_id_veto1: int
    team_id_pickn: int
    drafts: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentMatchDraft.Entry]
    def __init__(self, event_id: _Optional[int] = ..., event_stage_id: _Optional[int] = ..., team_id_0: _Optional[int] = ..., team_id_1: _Optional[int] = ..., maps_count: _Optional[int] = ..., maps_current: _Optional[int] = ..., team_id_start: _Optional[int] = ..., team_id_veto1: _Optional[int] = ..., team_id_pickn: _Optional[int] = ..., drafts: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentMatchDraft.Entry, _Mapping]]] = ...) -> None: ...

class CPreMatchInfoData(_message.Message):
    __slots__ = ("predictions_pct", "draft", "stats", "wins")
    class TeamStats(_message.Message):
        __slots__ = ("match_info_idxtxt", "match_info_txt", "match_info_teams")
        MATCH_INFO_IDXTXT_FIELD_NUMBER: _ClassVar[int]
        MATCH_INFO_TXT_FIELD_NUMBER: _ClassVar[int]
        MATCH_INFO_TEAMS_FIELD_NUMBER: _ClassVar[int]
        match_info_idxtxt: int
        match_info_txt: str
        match_info_teams: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, match_info_idxtxt: _Optional[int] = ..., match_info_txt: _Optional[str] = ..., match_info_teams: _Optional[_Iterable[str]] = ...) -> None: ...
    PREDICTIONS_PCT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    predictions_pct: int
    draft: CDataGCCStrike15_v2_TournamentMatchDraft
    stats: _containers.RepeatedCompositeFieldContainer[CPreMatchInfoData.TeamStats]
    wins: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, predictions_pct: _Optional[int] = ..., draft: _Optional[_Union[CDataGCCStrike15_v2_TournamentMatchDraft, _Mapping]] = ..., stats: _Optional[_Iterable[_Union[CPreMatchInfoData.TeamStats, _Mapping]]] = ..., wins: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve(_message.Message):
    __slots__ = ("account_ids", "game_type", "match_id", "server_version", "flags", "rankings", "encryption_key", "encryption_key_pub", "party_ids", "whitelist", "tv_master_steamid", "tournament_event", "tournament_teams", "tournament_casters_account_ids", "tv_relay_steamid", "pre_match_data", "rtime32_event_start", "tv_control")
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    RANKINGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_PUB_FIELD_NUMBER: _ClassVar[int]
    PARTY_IDS_FIELD_NUMBER: _ClassVar[int]
    WHITELIST_FIELD_NUMBER: _ClassVar[int]
    TV_MASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_TEAMS_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_CASTERS_ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    TV_RELAY_STEAMID_FIELD_NUMBER: _ClassVar[int]
    PRE_MATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    RTIME32_EVENT_START_FIELD_NUMBER: _ClassVar[int]
    TV_CONTROL_FIELD_NUMBER: _ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    game_type: int
    match_id: int
    server_version: int
    flags: int
    rankings: _containers.RepeatedCompositeFieldContainer[PlayerRankingInfo]
    encryption_key: int
    encryption_key_pub: int
    party_ids: _containers.RepeatedScalarFieldContainer[int]
    whitelist: _containers.RepeatedCompositeFieldContainer[IpAddressMask]
    tv_master_steamid: int
    tournament_event: TournamentEvent
    tournament_teams: _containers.RepeatedCompositeFieldContainer[TournamentTeam]
    tournament_casters_account_ids: _containers.RepeatedScalarFieldContainer[int]
    tv_relay_steamid: int
    pre_match_data: CPreMatchInfoData
    rtime32_event_start: int
    tv_control: int
    def __init__(self, account_ids: _Optional[_Iterable[int]] = ..., game_type: _Optional[int] = ..., match_id: _Optional[int] = ..., server_version: _Optional[int] = ..., flags: _Optional[int] = ..., rankings: _Optional[_Iterable[_Union[PlayerRankingInfo, _Mapping]]] = ..., encryption_key: _Optional[int] = ..., encryption_key_pub: _Optional[int] = ..., party_ids: _Optional[_Iterable[int]] = ..., whitelist: _Optional[_Iterable[_Union[IpAddressMask, _Mapping]]] = ..., tv_master_steamid: _Optional[int] = ..., tournament_event: _Optional[_Union[TournamentEvent, _Mapping]] = ..., tournament_teams: _Optional[_Iterable[_Union[TournamentTeam, _Mapping]]] = ..., tournament_casters_account_ids: _Optional[_Iterable[int]] = ..., tv_relay_steamid: _Optional[int] = ..., pre_match_data: _Optional[_Union[CPreMatchInfoData, _Mapping]] = ..., rtime32_event_start: _Optional[int] = ..., tv_control: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingServerReservationResponse(_message.Message):
    __slots__ = ("reservationid", "reservation", "map", "gc_reservation_sent", "server_version", "tv_info", "reward_player_accounts", "idle_player_accounts", "reward_item_attr_def_idx", "reward_item_attr_value", "reward_item_attr_reward_idx", "reward_drop_list", "tournament_tag", "legacy_steamdatagram_port", "steamdatagram_routing", "test_token", "flags")
    RESERVATIONID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    GC_RESERVATION_SENT_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    TV_INFO_FIELD_NUMBER: _ClassVar[int]
    REWARD_PLAYER_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    IDLE_PLAYER_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_ITEM_ATTR_DEF_IDX_FIELD_NUMBER: _ClassVar[int]
    REWARD_ITEM_ATTR_VALUE_FIELD_NUMBER: _ClassVar[int]
    REWARD_ITEM_ATTR_REWARD_IDX_FIELD_NUMBER: _ClassVar[int]
    REWARD_DROP_LIST_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_TAG_FIELD_NUMBER: _ClassVar[int]
    LEGACY_STEAMDATAGRAM_PORT_FIELD_NUMBER: _ClassVar[int]
    STEAMDATAGRAM_ROUTING_FIELD_NUMBER: _ClassVar[int]
    TEST_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    reservationid: int
    reservation: CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve
    map: str
    gc_reservation_sent: int
    server_version: int
    tv_info: ServerHltvInfo
    reward_player_accounts: _containers.RepeatedScalarFieldContainer[int]
    idle_player_accounts: _containers.RepeatedScalarFieldContainer[int]
    reward_item_attr_def_idx: int
    reward_item_attr_value: int
    reward_item_attr_reward_idx: int
    reward_drop_list: int
    tournament_tag: str
    legacy_steamdatagram_port: int
    steamdatagram_routing: int
    test_token: int
    flags: int
    def __init__(self, reservationid: _Optional[int] = ..., reservation: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve, _Mapping]] = ..., map: _Optional[str] = ..., gc_reservation_sent: _Optional[int] = ..., server_version: _Optional[int] = ..., tv_info: _Optional[_Union[ServerHltvInfo, _Mapping]] = ..., reward_player_accounts: _Optional[_Iterable[int]] = ..., idle_player_accounts: _Optional[_Iterable[int]] = ..., reward_item_attr_def_idx: _Optional[int] = ..., reward_item_attr_value: _Optional[int] = ..., reward_item_attr_reward_idx: _Optional[int] = ..., reward_drop_list: _Optional[int] = ..., tournament_tag: _Optional[str] = ..., legacy_steamdatagram_port: _Optional[int] = ..., steamdatagram_routing: _Optional[int] = ..., test_token: _Optional[int] = ..., flags: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve(_message.Message):
    __slots__ = ("serverid", "direct_udp_ip", "direct_udp_port", "reservationid", "reservation", "map", "server_address")
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    DIRECT_UDP_IP_FIELD_NUMBER: _ClassVar[int]
    DIRECT_UDP_PORT_FIELD_NUMBER: _ClassVar[int]
    RESERVATIONID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    serverid: int
    direct_udp_ip: int
    direct_udp_port: int
    reservationid: int
    reservation: CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve
    map: str
    server_address: str
    def __init__(self, serverid: _Optional[int] = ..., direct_udp_ip: _Optional[int] = ..., direct_udp_port: _Optional[int] = ..., reservationid: _Optional[int] = ..., reservation: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve, _Mapping]] = ..., map: _Optional[str] = ..., server_address: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingServerRoundStats(_message.Message):
    __slots__ = ("reservationid", "reservation", "map", "round", "kills", "assists", "deaths", "scores", "pings", "round_result", "match_result", "team_scores", "confirm", "reservation_stage", "match_duration", "enemy_kills", "enemy_headshots", "enemy_3ks", "enemy_4ks", "enemy_5ks", "mvps", "spectators_count", "spectators_count_tv", "spectators_count_lnk", "enemy_kills_agg", "drop_info")
    class DropInfo(_message.Message):
        __slots__ = ("account_mvp",)
        ACCOUNT_MVP_FIELD_NUMBER: _ClassVar[int]
        account_mvp: int
        def __init__(self, account_mvp: _Optional[int] = ...) -> None: ...
    RESERVATIONID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    ROUND_FIELD_NUMBER: _ClassVar[int]
    KILLS_FIELD_NUMBER: _ClassVar[int]
    ASSISTS_FIELD_NUMBER: _ClassVar[int]
    DEATHS_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    PINGS_FIELD_NUMBER: _ClassVar[int]
    ROUND_RESULT_FIELD_NUMBER: _ClassVar[int]
    MATCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    TEAM_SCORES_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_STAGE_FIELD_NUMBER: _ClassVar[int]
    MATCH_DURATION_FIELD_NUMBER: _ClassVar[int]
    ENEMY_KILLS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_HEADSHOTS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_3KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_4KS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_5KS_FIELD_NUMBER: _ClassVar[int]
    MVPS_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_COUNT_TV_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_COUNT_LNK_FIELD_NUMBER: _ClassVar[int]
    ENEMY_KILLS_AGG_FIELD_NUMBER: _ClassVar[int]
    DROP_INFO_FIELD_NUMBER: _ClassVar[int]
    reservationid: int
    reservation: CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve
    map: str
    round: int
    kills: _containers.RepeatedScalarFieldContainer[int]
    assists: _containers.RepeatedScalarFieldContainer[int]
    deaths: _containers.RepeatedScalarFieldContainer[int]
    scores: _containers.RepeatedScalarFieldContainer[int]
    pings: _containers.RepeatedScalarFieldContainer[int]
    round_result: int
    match_result: int
    team_scores: _containers.RepeatedScalarFieldContainer[int]
    confirm: CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm
    reservation_stage: int
    match_duration: int
    enemy_kills: _containers.RepeatedScalarFieldContainer[int]
    enemy_headshots: _containers.RepeatedScalarFieldContainer[int]
    enemy_3ks: _containers.RepeatedScalarFieldContainer[int]
    enemy_4ks: _containers.RepeatedScalarFieldContainer[int]
    enemy_5ks: _containers.RepeatedScalarFieldContainer[int]
    mvps: _containers.RepeatedScalarFieldContainer[int]
    spectators_count: int
    spectators_count_tv: int
    spectators_count_lnk: int
    enemy_kills_agg: _containers.RepeatedScalarFieldContainer[int]
    drop_info: CMsgGCCStrike15_v2_MatchmakingServerRoundStats.DropInfo
    def __init__(self, reservationid: _Optional[int] = ..., reservation: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve, _Mapping]] = ..., map: _Optional[str] = ..., round: _Optional[int] = ..., kills: _Optional[_Iterable[int]] = ..., assists: _Optional[_Iterable[int]] = ..., deaths: _Optional[_Iterable[int]] = ..., scores: _Optional[_Iterable[int]] = ..., pings: _Optional[_Iterable[int]] = ..., round_result: _Optional[int] = ..., match_result: _Optional[int] = ..., team_scores: _Optional[_Iterable[int]] = ..., confirm: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm, _Mapping]] = ..., reservation_stage: _Optional[int] = ..., match_duration: _Optional[int] = ..., enemy_kills: _Optional[_Iterable[int]] = ..., enemy_headshots: _Optional[_Iterable[int]] = ..., enemy_3ks: _Optional[_Iterable[int]] = ..., enemy_4ks: _Optional[_Iterable[int]] = ..., enemy_5ks: _Optional[_Iterable[int]] = ..., mvps: _Optional[_Iterable[int]] = ..., spectators_count: _Optional[int] = ..., spectators_count_tv: _Optional[int] = ..., spectators_count_lnk: _Optional[int] = ..., enemy_kills_agg: _Optional[_Iterable[int]] = ..., drop_info: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingServerRoundStats.DropInfo, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingServerMatchEnd(_message.Message):
    __slots__ = ("stats", "confirm", "rematch", "replay_token", "replay_cluster_id", "aborted_match", "match_end_quest_data", "server_version")
    STATS_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    REMATCH_FIELD_NUMBER: _ClassVar[int]
    REPLAY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REPLAY_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ABORTED_MATCH_FIELD_NUMBER: _ClassVar[int]
    MATCH_END_QUEST_DATA_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    stats: CMsgGCCStrike15_v2_MatchmakingServerRoundStats
    confirm: CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm
    rematch: int
    replay_token: int
    replay_cluster_id: int
    aborted_match: bool
    match_end_quest_data: CMsgGC_ServerQuestUpdateData
    server_version: int
    def __init__(self, stats: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingServerRoundStats, _Mapping]] = ..., confirm: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm, _Mapping]] = ..., rematch: _Optional[int] = ..., replay_token: _Optional[int] = ..., replay_cluster_id: _Optional[int] = ..., aborted_match: bool = ..., match_end_quest_data: _Optional[_Union[CMsgGC_ServerQuestUpdateData, _Mapping]] = ..., server_version: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingServerMatchEndPartial(_message.Message):
    __slots__ = ("reservationid", "reservation", "confirm", "completed_player_quest_data", "server_version")
    RESERVATIONID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_PLAYER_QUEST_DATA_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    reservationid: int
    reservation: CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve
    confirm: CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm
    completed_player_quest_data: CMsgGC_ServerQuestUpdateData
    server_version: int
    def __init__(self, reservationid: _Optional[int] = ..., reservation: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve, _Mapping]] = ..., confirm: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm, _Mapping]] = ..., completed_player_quest_data: _Optional[_Union[CMsgGC_ServerQuestUpdateData, _Mapping]] = ..., server_version: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingClient2GCHello(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ClientHello(_message.Message):
    __slots__ = ("account_id", "ongoingmatch", "global_stats", "penalty_seconds", "penalty_reason", "vac_banned", "ranking", "commendation", "medals", "my_current_event", "my_current_event_teams", "my_current_team", "my_current_event_stages", "survey_vote", "activity", "player_level", "player_cur_xp", "player_xp_bonus_flags", "rankings")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ONGOINGMATCH_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PENALTY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PENALTY_REASON_FIELD_NUMBER: _ClassVar[int]
    VAC_BANNED_FIELD_NUMBER: _ClassVar[int]
    RANKING_FIELD_NUMBER: _ClassVar[int]
    COMMENDATION_FIELD_NUMBER: _ClassVar[int]
    MEDALS_FIELD_NUMBER: _ClassVar[int]
    MY_CURRENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    MY_CURRENT_EVENT_TEAMS_FIELD_NUMBER: _ClassVar[int]
    MY_CURRENT_TEAM_FIELD_NUMBER: _ClassVar[int]
    MY_CURRENT_EVENT_STAGES_FIELD_NUMBER: _ClassVar[int]
    SURVEY_VOTE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_CUR_XP_FIELD_NUMBER: _ClassVar[int]
    PLAYER_XP_BONUS_FLAGS_FIELD_NUMBER: _ClassVar[int]
    RANKINGS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    ongoingmatch: CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    global_stats: GlobalStatistics
    penalty_seconds: int
    penalty_reason: int
    vac_banned: int
    ranking: PlayerRankingInfo
    commendation: PlayerCommendationInfo
    medals: PlayerMedalsInfo
    my_current_event: TournamentEvent
    my_current_event_teams: _containers.RepeatedCompositeFieldContainer[TournamentTeam]
    my_current_team: TournamentTeam
    my_current_event_stages: _containers.RepeatedCompositeFieldContainer[TournamentEvent]
    survey_vote: int
    activity: AccountActivity
    player_level: int
    player_cur_xp: int
    player_xp_bonus_flags: int
    rankings: _containers.RepeatedCompositeFieldContainer[PlayerRankingInfo]
    def __init__(self, account_id: _Optional[int] = ..., ongoingmatch: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve, _Mapping]] = ..., global_stats: _Optional[_Union[GlobalStatistics, _Mapping]] = ..., penalty_seconds: _Optional[int] = ..., penalty_reason: _Optional[int] = ..., vac_banned: _Optional[int] = ..., ranking: _Optional[_Union[PlayerRankingInfo, _Mapping]] = ..., commendation: _Optional[_Union[PlayerCommendationInfo, _Mapping]] = ..., medals: _Optional[_Union[PlayerMedalsInfo, _Mapping]] = ..., my_current_event: _Optional[_Union[TournamentEvent, _Mapping]] = ..., my_current_event_teams: _Optional[_Iterable[_Union[TournamentTeam, _Mapping]]] = ..., my_current_team: _Optional[_Union[TournamentTeam, _Mapping]] = ..., my_current_event_stages: _Optional[_Iterable[_Union[TournamentEvent, _Mapping]]] = ..., survey_vote: _Optional[int] = ..., activity: _Optional[_Union[AccountActivity, _Mapping]] = ..., player_level: _Optional[int] = ..., player_cur_xp: _Optional[int] = ..., player_xp_bonus_flags: _Optional[int] = ..., rankings: _Optional[_Iterable[_Union[PlayerRankingInfo, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_AccountPrivacySettings(_message.Message):
    __slots__ = ("settings",)
    class Setting(_message.Message):
        __slots__ = ("setting_type", "setting_value")
        SETTING_TYPE_FIELD_NUMBER: _ClassVar[int]
        SETTING_VALUE_FIELD_NUMBER: _ClassVar[int]
        setting_type: int
        setting_value: int
        def __init__(self, setting_type: _Optional[int] = ..., setting_value: _Optional[int] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_AccountPrivacySettings.Setting]
    def __init__(self, settings: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_AccountPrivacySettings.Setting, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon(_message.Message):
    __slots__ = ("account_id", "abandoned_match", "penalty_seconds", "penalty_reason")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ABANDONED_MATCH_FIELD_NUMBER: _ClassVar[int]
    PENALTY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PENALTY_REASON_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    abandoned_match: CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    penalty_seconds: int
    penalty_reason: int
    def __init__(self, account_id: _Optional[int] = ..., abandoned_match: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve, _Mapping]] = ..., penalty_seconds: _Optional[int] = ..., penalty_reason: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingServer2GCKick(_message.Message):
    __slots__ = ("account_id", "reservation", "reason")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    reservation: CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve
    reason: int
    def __init__(self, account_id: _Optional[int] = ..., reservation: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve, _Mapping]] = ..., reason: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingGC2ServerRankUpdate(_message.Message):
    __slots__ = ("rankings", "match_id")
    RANKINGS_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    rankings: _containers.RepeatedCompositeFieldContainer[PlayerRankingInfo]
    match_id: int
    def __init__(self, rankings: _Optional[_Iterable[_Union[PlayerRankingInfo, _Mapping]]] = ..., match_id: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientGCRankUpdate(_message.Message):
    __slots__ = ("rankings",)
    RANKINGS_FIELD_NUMBER: _ClassVar[int]
    rankings: _containers.RepeatedCompositeFieldContainer[PlayerRankingInfo]
    def __init__(self, rankings: _Optional[_Iterable[_Union[PlayerRankingInfo, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate(_message.Message):
    __slots__ = ("main_post_url",)
    MAIN_POST_URL_FIELD_NUMBER: _ClassVar[int]
    main_post_url: str
    def __init__(self, main_post_url: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ServerNotificationForUserPenalty(_message.Message):
    __slots__ = ("account_id", "reason", "seconds", "communication_cooldown")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_COOLDOWN_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    reason: int
    seconds: int
    communication_cooldown: bool
    def __init__(self, account_id: _Optional[int] = ..., reason: _Optional[int] = ..., seconds: _Optional[int] = ..., communication_cooldown: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientReportPlayer(_message.Message):
    __slots__ = ("account_id", "rpt_aimbot", "rpt_wallhack", "rpt_speedhack", "rpt_teamharm", "rpt_textabuse", "rpt_voiceabuse", "match_id", "report_from_demo")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RPT_AIMBOT_FIELD_NUMBER: _ClassVar[int]
    RPT_WALLHACK_FIELD_NUMBER: _ClassVar[int]
    RPT_SPEEDHACK_FIELD_NUMBER: _ClassVar[int]
    RPT_TEAMHARM_FIELD_NUMBER: _ClassVar[int]
    RPT_TEXTABUSE_FIELD_NUMBER: _ClassVar[int]
    RPT_VOICEABUSE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_FROM_DEMO_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    rpt_aimbot: int
    rpt_wallhack: int
    rpt_speedhack: int
    rpt_teamharm: int
    rpt_textabuse: int
    rpt_voiceabuse: int
    match_id: int
    report_from_demo: bool
    def __init__(self, account_id: _Optional[int] = ..., rpt_aimbot: _Optional[int] = ..., rpt_wallhack: _Optional[int] = ..., rpt_speedhack: _Optional[int] = ..., rpt_teamharm: _Optional[int] = ..., rpt_textabuse: _Optional[int] = ..., rpt_voiceabuse: _Optional[int] = ..., match_id: _Optional[int] = ..., report_from_demo: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientCommendPlayer(_message.Message):
    __slots__ = ("account_id", "match_id", "commendation", "tokens")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENDATION_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    match_id: int
    commendation: PlayerCommendationInfo
    tokens: int
    def __init__(self, account_id: _Optional[int] = ..., match_id: _Optional[int] = ..., commendation: _Optional[_Union[PlayerCommendationInfo, _Mapping]] = ..., tokens: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientReportServer(_message.Message):
    __slots__ = ("rpt_poorperf", "rpt_abusivemodels", "rpt_badmotd", "rpt_listingabuse", "rpt_inventoryabuse", "match_id")
    RPT_POORPERF_FIELD_NUMBER: _ClassVar[int]
    RPT_ABUSIVEMODELS_FIELD_NUMBER: _ClassVar[int]
    RPT_BADMOTD_FIELD_NUMBER: _ClassVar[int]
    RPT_LISTINGABUSE_FIELD_NUMBER: _ClassVar[int]
    RPT_INVENTORYABUSE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    rpt_poorperf: int
    rpt_abusivemodels: int
    rpt_badmotd: int
    rpt_listingabuse: int
    rpt_inventoryabuse: int
    match_id: int
    def __init__(self, rpt_poorperf: _Optional[int] = ..., rpt_abusivemodels: _Optional[int] = ..., rpt_badmotd: _Optional[int] = ..., rpt_listingabuse: _Optional[int] = ..., rpt_inventoryabuse: _Optional[int] = ..., match_id: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientReportResponse(_message.Message):
    __slots__ = ("confirmation_id", "account_id", "server_ip", "response_type", "response_result", "tokens")
    CONFIRMATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_RESULT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    confirmation_id: int
    account_id: int
    server_ip: int
    response_type: int
    response_result: int
    tokens: int
    def __init__(self, confirmation_id: _Optional[int] = ..., account_id: _Optional[int] = ..., server_ip: _Optional[int] = ..., response_type: _Optional[int] = ..., response_result: _Optional[int] = ..., tokens: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestWatchInfoFriends(_message.Message):
    __slots__ = ("request_id", "account_ids", "serverid", "matchid", "client_launcher", "data_center_pings")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    DATA_CENTER_PINGS_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    serverid: int
    matchid: int
    client_launcher: int
    data_center_pings: _containers.RepeatedCompositeFieldContainer[DataCenterPing]
    def __init__(self, request_id: _Optional[int] = ..., account_ids: _Optional[_Iterable[int]] = ..., serverid: _Optional[int] = ..., matchid: _Optional[int] = ..., client_launcher: _Optional[int] = ..., data_center_pings: _Optional[_Iterable[_Union[DataCenterPing, _Mapping]]] = ...) -> None: ...

class WatchableMatchInfo(_message.Message):
    __slots__ = ("server_ip", "tv_port", "tv_spectators", "tv_time", "tv_watch_password", "cl_decryptdata_key", "cl_decryptdata_key_pub", "game_type", "game_mapgroup", "game_map", "server_id", "match_id", "reservation_id")
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    TV_PORT_FIELD_NUMBER: _ClassVar[int]
    TV_SPECTATORS_FIELD_NUMBER: _ClassVar[int]
    TV_TIME_FIELD_NUMBER: _ClassVar[int]
    TV_WATCH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CL_DECRYPTDATA_KEY_FIELD_NUMBER: _ClassVar[int]
    CL_DECRYPTDATA_KEY_PUB_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    GAME_MAPGROUP_FIELD_NUMBER: _ClassVar[int]
    GAME_MAP_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    server_ip: int
    tv_port: int
    tv_spectators: int
    tv_time: int
    tv_watch_password: bytes
    cl_decryptdata_key: int
    cl_decryptdata_key_pub: int
    game_type: int
    game_mapgroup: str
    game_map: str
    server_id: int
    match_id: int
    reservation_id: int
    def __init__(self, server_ip: _Optional[int] = ..., tv_port: _Optional[int] = ..., tv_spectators: _Optional[int] = ..., tv_time: _Optional[int] = ..., tv_watch_password: _Optional[bytes] = ..., cl_decryptdata_key: _Optional[int] = ..., cl_decryptdata_key_pub: _Optional[int] = ..., game_type: _Optional[int] = ..., game_mapgroup: _Optional[str] = ..., game_map: _Optional[str] = ..., server_id: _Optional[int] = ..., match_id: _Optional[int] = ..., reservation_id: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestJoinFriendData(_message.Message):
    __slots__ = ("version", "account_id", "join_token", "join_ipp", "res", "errormsg")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    JOIN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    JOIN_IPP_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    version: int
    account_id: int
    join_token: int
    join_ipp: int
    res: CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    errormsg: str
    def __init__(self, version: _Optional[int] = ..., account_id: _Optional[int] = ..., join_token: _Optional[int] = ..., join_ipp: _Optional[int] = ..., res: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve, _Mapping]] = ..., errormsg: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestJoinServerData(_message.Message):
    __slots__ = ("version", "account_id", "serverid", "server_ip", "server_port", "res", "errormsg")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    version: int
    account_id: int
    serverid: int
    server_ip: int
    server_port: int
    res: CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    errormsg: str
    def __init__(self, version: _Optional[int] = ..., account_id: _Optional[int] = ..., serverid: _Optional[int] = ..., server_ip: _Optional[int] = ..., server_port: _Optional[int] = ..., res: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve, _Mapping]] = ..., errormsg: _Optional[str] = ...) -> None: ...

class CMsgGCCstrike15_v2_ClientRequestNewMission(_message.Message):
    __slots__ = ("mission_id", "campaign_id")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    mission_id: int
    campaign_id: int
    def __init__(self, mission_id: _Optional[int] = ..., campaign_id: _Optional[int] = ...) -> None: ...

class CMsgGCCstrike15_v2_GC2ServerNotifyXPRewarded(_message.Message):
    __slots__ = ("xp_progress_data", "account_id", "current_xp", "current_level", "upgraded_defidx", "operation_points_awarded")
    XP_PROGRESS_DATA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_XP_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    UPGRADED_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    OPERATION_POINTS_AWARDED_FIELD_NUMBER: _ClassVar[int]
    xp_progress_data: _containers.RepeatedCompositeFieldContainer[XpProgressData]
    account_id: int
    current_xp: int
    current_level: int
    upgraded_defidx: int
    operation_points_awarded: int
    def __init__(self, xp_progress_data: _Optional[_Iterable[_Union[XpProgressData, _Mapping]]] = ..., account_id: _Optional[int] = ..., current_xp: _Optional[int] = ..., current_level: _Optional[int] = ..., upgraded_defidx: _Optional[int] = ..., operation_points_awarded: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_WatchInfoUsers(_message.Message):
    __slots__ = ("request_id", "account_ids", "watchable_match_infos", "extended_timeout")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    WATCHABLE_MATCH_INFOS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    watchable_match_infos: _containers.RepeatedCompositeFieldContainer[WatchableMatchInfo]
    extended_timeout: int
    def __init__(self, request_id: _Optional[int] = ..., account_ids: _Optional[_Iterable[int]] = ..., watchable_match_infos: _Optional[_Iterable[_Union[WatchableMatchInfo, _Mapping]]] = ..., extended_timeout: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestPlayersProfile(_message.Message):
    __slots__ = ("request_id__deprecated", "account_ids__deprecated", "account_id", "request_level")
    REQUEST_ID__DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_IDS__DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    request_id__deprecated: int
    account_ids__deprecated: _containers.RepeatedScalarFieldContainer[int]
    account_id: int
    request_level: int
    def __init__(self, request_id__deprecated: _Optional[int] = ..., account_ids__deprecated: _Optional[_Iterable[int]] = ..., account_id: _Optional[int] = ..., request_level: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_PlayersProfile(_message.Message):
    __slots__ = ("request_id", "account_profiles")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_PROFILES_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    account_profiles: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_MatchmakingGC2ClientHello]
    def __init__(self, request_id: _Optional[int] = ..., account_profiles: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_MatchmakingGC2ClientHello, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate(_message.Message):
    __slots__ = ("caseid", "suspectid", "fractionid", "rpt_aimbot", "rpt_wallhack", "rpt_speedhack", "rpt_teamharm", "reason")
    CASEID_FIELD_NUMBER: _ClassVar[int]
    SUSPECTID_FIELD_NUMBER: _ClassVar[int]
    FRACTIONID_FIELD_NUMBER: _ClassVar[int]
    RPT_AIMBOT_FIELD_NUMBER: _ClassVar[int]
    RPT_WALLHACK_FIELD_NUMBER: _ClassVar[int]
    RPT_SPEEDHACK_FIELD_NUMBER: _ClassVar[int]
    RPT_TEAMHARM_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    caseid: int
    suspectid: int
    fractionid: int
    rpt_aimbot: int
    rpt_wallhack: int
    rpt_speedhack: int
    rpt_teamharm: int
    reason: int
    def __init__(self, caseid: _Optional[int] = ..., suspectid: _Optional[int] = ..., fractionid: _Optional[int] = ..., rpt_aimbot: _Optional[int] = ..., rpt_wallhack: _Optional[int] = ..., rpt_speedhack: _Optional[int] = ..., rpt_teamharm: _Optional[int] = ..., reason: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment(_message.Message):
    __slots__ = ("caseid", "caseurl", "verdict", "timestamp", "throttleseconds", "suspectid", "fractionid", "numrounds", "fractionrounds", "streakconvictions", "reason")
    CASEID_FIELD_NUMBER: _ClassVar[int]
    CASEURL_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    THROTTLESECONDS_FIELD_NUMBER: _ClassVar[int]
    SUSPECTID_FIELD_NUMBER: _ClassVar[int]
    FRACTIONID_FIELD_NUMBER: _ClassVar[int]
    NUMROUNDS_FIELD_NUMBER: _ClassVar[int]
    FRACTIONROUNDS_FIELD_NUMBER: _ClassVar[int]
    STREAKCONVICTIONS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    caseid: int
    caseurl: str
    verdict: int
    timestamp: int
    throttleseconds: int
    suspectid: int
    fractionid: int
    numrounds: int
    fractionrounds: int
    streakconvictions: int
    reason: int
    def __init__(self, caseid: _Optional[int] = ..., caseurl: _Optional[str] = ..., verdict: _Optional[int] = ..., timestamp: _Optional[int] = ..., throttleseconds: _Optional[int] = ..., suspectid: _Optional[int] = ..., fractionid: _Optional[int] = ..., numrounds: _Optional[int] = ..., fractionrounds: _Optional[int] = ..., streakconvictions: _Optional[int] = ..., reason: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_PlayerOverwatchCaseStatus(_message.Message):
    __slots__ = ("caseid", "statusid")
    CASEID_FIELD_NUMBER: _ClassVar[int]
    STATUSID_FIELD_NUMBER: _ClassVar[int]
    caseid: int
    statusid: int
    def __init__(self, caseid: _Optional[int] = ..., statusid: _Optional[int] = ...) -> None: ...

class CClientHeaderOverwatchEvidence(_message.Message):
    __slots__ = ("accountid", "caseid")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    caseid: int
    def __init__(self, accountid: _Optional[int] = ..., caseid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientTextMsg(_message.Message):
    __slots__ = ("id", "type", "payload")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    payload: bytes
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCTextMsg(_message.Message):
    __slots__ = ("id", "args")
    ID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    args: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, id: _Optional[int] = ..., args: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchEndRunRewardDrops(_message.Message):
    __slots__ = ("serverinfo", "match_end_quest_data")
    SERVERINFO_FIELD_NUMBER: _ClassVar[int]
    MATCH_END_QUEST_DATA_FIELD_NUMBER: _ClassVar[int]
    serverinfo: CMsgGCCStrike15_v2_MatchmakingServerReservationResponse
    match_end_quest_data: CMsgGC_ServerQuestUpdateData
    def __init__(self, serverinfo: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingServerReservationResponse, _Mapping]] = ..., match_end_quest_data: _Optional[_Union[CMsgGC_ServerQuestUpdateData, _Mapping]] = ...) -> None: ...

class CEconItemPreviewDataBlock(_message.Message):
    __slots__ = ("accountid", "itemid", "defindex", "paintindex", "rarity", "quality", "paintwear", "paintseed", "killeaterscoretype", "killeatervalue", "customname", "stickers", "inventory", "origin", "questid", "dropreason", "musicindex", "entindex")
    class Sticker(_message.Message):
        __slots__ = ("slot", "sticker_id", "wear", "scale", "rotation", "tint_id")
        SLOT_FIELD_NUMBER: _ClassVar[int]
        STICKER_ID_FIELD_NUMBER: _ClassVar[int]
        WEAR_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        TINT_ID_FIELD_NUMBER: _ClassVar[int]
        slot: int
        sticker_id: int
        wear: float
        scale: float
        rotation: float
        tint_id: int
        def __init__(self, slot: _Optional[int] = ..., sticker_id: _Optional[int] = ..., wear: _Optional[float] = ..., scale: _Optional[float] = ..., rotation: _Optional[float] = ..., tint_id: _Optional[int] = ...) -> None: ...
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    DEFINDEX_FIELD_NUMBER: _ClassVar[int]
    PAINTINDEX_FIELD_NUMBER: _ClassVar[int]
    RARITY_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    PAINTWEAR_FIELD_NUMBER: _ClassVar[int]
    PAINTSEED_FIELD_NUMBER: _ClassVar[int]
    KILLEATERSCORETYPE_FIELD_NUMBER: _ClassVar[int]
    KILLEATERVALUE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMNAME_FIELD_NUMBER: _ClassVar[int]
    STICKERS_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    QUESTID_FIELD_NUMBER: _ClassVar[int]
    DROPREASON_FIELD_NUMBER: _ClassVar[int]
    MUSICINDEX_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    itemid: int
    defindex: int
    paintindex: int
    rarity: int
    quality: int
    paintwear: int
    paintseed: int
    killeaterscoretype: int
    killeatervalue: int
    customname: str
    stickers: _containers.RepeatedCompositeFieldContainer[CEconItemPreviewDataBlock.Sticker]
    inventory: int
    origin: int
    questid: int
    dropreason: int
    musicindex: int
    entindex: int
    def __init__(self, accountid: _Optional[int] = ..., itemid: _Optional[int] = ..., defindex: _Optional[int] = ..., paintindex: _Optional[int] = ..., rarity: _Optional[int] = ..., quality: _Optional[int] = ..., paintwear: _Optional[int] = ..., paintseed: _Optional[int] = ..., killeaterscoretype: _Optional[int] = ..., killeatervalue: _Optional[int] = ..., customname: _Optional[str] = ..., stickers: _Optional[_Iterable[_Union[CEconItemPreviewDataBlock.Sticker, _Mapping]]] = ..., inventory: _Optional[int] = ..., origin: _Optional[int] = ..., questid: _Optional[int] = ..., dropreason: _Optional[int] = ..., musicindex: _Optional[int] = ..., entindex: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchEndRewardDropsNotification(_message.Message):
    __slots__ = ("iteminfo",)
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    iteminfo: CEconItemPreviewDataBlock
    def __init__(self, iteminfo: _Optional[_Union[CEconItemPreviewDataBlock, _Mapping]] = ...) -> None: ...

class CMsgItemAcknowledged(_message.Message):
    __slots__ = ("iteminfo",)
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    iteminfo: CEconItemPreviewDataBlock
    def __init__(self, iteminfo: _Optional[_Union[CEconItemPreviewDataBlock, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest(_message.Message):
    __slots__ = ("param_s", "param_a", "param_d", "param_m")
    PARAM_S_FIELD_NUMBER: _ClassVar[int]
    PARAM_A_FIELD_NUMBER: _ClassVar[int]
    PARAM_D_FIELD_NUMBER: _ClassVar[int]
    PARAM_M_FIELD_NUMBER: _ClassVar[int]
    param_s: int
    param_a: int
    param_d: int
    param_m: int
    def __init__(self, param_s: _Optional[int] = ..., param_a: _Optional[int] = ..., param_d: _Optional[int] = ..., param_m: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse(_message.Message):
    __slots__ = ("iteminfo",)
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    iteminfo: CEconItemPreviewDataBlock
    def __init__(self, iteminfo: _Optional[_Union[CEconItemPreviewDataBlock, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_TournamentMatchRewardDropsNotification(_message.Message):
    __slots__ = ("match_id", "defindex", "accountids")
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINDEX_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    defindex: int
    accountids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, match_id: _Optional[int] = ..., defindex: _Optional[int] = ..., accountids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestLiveGameForUser(_message.Message):
    __slots__ = ("accountid",)
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    def __init__(self, accountid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestRecentUserGames(_message.Message):
    __slots__ = ("accountid",)
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    def __init__(self, accountid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestTournamentGames(_message.Message):
    __slots__ = ("eventid",)
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    def __init__(self, eventid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchListRequestFullGameInfo(_message.Message):
    __slots__ = ("matchid", "outcomeid", "token")
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    OUTCOMEID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    matchid: int
    outcomeid: int
    token: int
    def __init__(self, matchid: _Optional[int] = ..., outcomeid: _Optional[int] = ..., token: _Optional[int] = ...) -> None: ...

class CDataGCCStrike15_v2_MatchInfo(_message.Message):
    __slots__ = ("matchid", "matchtime", "watchablematchinfo", "roundstats_legacy", "roundstatsall")
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    MATCHTIME_FIELD_NUMBER: _ClassVar[int]
    WATCHABLEMATCHINFO_FIELD_NUMBER: _ClassVar[int]
    ROUNDSTATS_LEGACY_FIELD_NUMBER: _ClassVar[int]
    ROUNDSTATSALL_FIELD_NUMBER: _ClassVar[int]
    matchid: int
    matchtime: int
    watchablematchinfo: WatchableMatchInfo
    roundstats_legacy: CMsgGCCStrike15_v2_MatchmakingServerRoundStats
    roundstatsall: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_MatchmakingServerRoundStats]
    def __init__(self, matchid: _Optional[int] = ..., matchtime: _Optional[int] = ..., watchablematchinfo: _Optional[_Union[WatchableMatchInfo, _Mapping]] = ..., roundstats_legacy: _Optional[_Union[CMsgGCCStrike15_v2_MatchmakingServerRoundStats, _Mapping]] = ..., roundstatsall: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_MatchmakingServerRoundStats, _Mapping]]] = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentGroupTeam(_message.Message):
    __slots__ = ("team_id", "score", "correctpick")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CORRECTPICK_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    score: int
    correctpick: bool
    def __init__(self, team_id: _Optional[int] = ..., score: _Optional[int] = ..., correctpick: bool = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentGroup(_message.Message):
    __slots__ = ("groupid", "name", "desc", "picks__deprecated", "teams", "stage_ids", "picklockuntiltime", "pickableteams", "points_per_pick", "picks")
    class Picks(_message.Message):
        __slots__ = ("pickids",)
        PICKIDS_FIELD_NUMBER: _ClassVar[int]
        pickids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, pickids: _Optional[_Iterable[int]] = ...) -> None: ...
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    PICKS__DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    STAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    PICKLOCKUNTILTIME_FIELD_NUMBER: _ClassVar[int]
    PICKABLETEAMS_FIELD_NUMBER: _ClassVar[int]
    POINTS_PER_PICK_FIELD_NUMBER: _ClassVar[int]
    PICKS_FIELD_NUMBER: _ClassVar[int]
    groupid: int
    name: str
    desc: str
    picks__deprecated: int
    teams: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentGroupTeam]
    stage_ids: _containers.RepeatedScalarFieldContainer[int]
    picklockuntiltime: int
    pickableteams: int
    points_per_pick: int
    picks: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentGroup.Picks]
    def __init__(self, groupid: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., picks__deprecated: _Optional[int] = ..., teams: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentGroupTeam, _Mapping]]] = ..., stage_ids: _Optional[_Iterable[int]] = ..., picklockuntiltime: _Optional[int] = ..., pickableteams: _Optional[int] = ..., points_per_pick: _Optional[int] = ..., picks: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentGroup.Picks, _Mapping]]] = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentSection(_message.Message):
    __slots__ = ("sectionid", "name", "desc", "groups")
    SECTIONID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    sectionid: int
    name: str
    desc: str
    groups: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentGroup]
    def __init__(self, sectionid: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., groups: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentGroup, _Mapping]]] = ...) -> None: ...

class CDataGCCStrike15_v2_TournamentInfo(_message.Message):
    __slots__ = ("sections", "tournament_event", "tournament_teams")
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENT_TEAMS_FIELD_NUMBER: _ClassVar[int]
    sections: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_TournamentSection]
    tournament_event: TournamentEvent
    tournament_teams: _containers.RepeatedCompositeFieldContainer[TournamentTeam]
    def __init__(self, sections: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_TournamentSection, _Mapping]]] = ..., tournament_event: _Optional[_Union[TournamentEvent, _Mapping]] = ..., tournament_teams: _Optional[_Iterable[_Union[TournamentTeam, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_MatchList(_message.Message):
    __slots__ = ("msgrequestid", "accountid", "servertime", "matches", "streams", "tournamentinfo")
    MSGREQUESTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SERVERTIME_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENTINFO_FIELD_NUMBER: _ClassVar[int]
    msgrequestid: int
    accountid: int
    servertime: int
    matches: _containers.RepeatedCompositeFieldContainer[CDataGCCStrike15_v2_MatchInfo]
    streams: _containers.RepeatedCompositeFieldContainer[TournamentTeam]
    tournamentinfo: CDataGCCStrike15_v2_TournamentInfo
    def __init__(self, msgrequestid: _Optional[int] = ..., accountid: _Optional[int] = ..., servertime: _Optional[int] = ..., matches: _Optional[_Iterable[_Union[CDataGCCStrike15_v2_MatchInfo, _Mapping]]] = ..., streams: _Optional[_Iterable[_Union[TournamentTeam, _Mapping]]] = ..., tournamentinfo: _Optional[_Union[CDataGCCStrike15_v2_TournamentInfo, _Mapping]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Predictions(_message.Message):
    __slots__ = ("event_id", "group_match_team_picks")
    class GroupMatchTeamPick(_message.Message):
        __slots__ = ("sectionid", "groupid", "index", "teamid", "itemid")
        SECTIONID_FIELD_NUMBER: _ClassVar[int]
        GROUPID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TEAMID_FIELD_NUMBER: _ClassVar[int]
        ITEMID_FIELD_NUMBER: _ClassVar[int]
        sectionid: int
        groupid: int
        index: int
        teamid: int
        itemid: int
        def __init__(self, sectionid: _Optional[int] = ..., groupid: _Optional[int] = ..., index: _Optional[int] = ..., teamid: _Optional[int] = ..., itemid: _Optional[int] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_MATCH_TEAM_PICKS_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    group_match_team_picks: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Predictions.GroupMatchTeamPick]
    def __init__(self, event_id: _Optional[int] = ..., group_match_team_picks: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Predictions.GroupMatchTeamPick, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Fantasy(_message.Message):
    __slots__ = ("event_id", "teams")
    class FantasySlot(_message.Message):
        __slots__ = ("type", "pick", "itemid")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PICK_FIELD_NUMBER: _ClassVar[int]
        ITEMID_FIELD_NUMBER: _ClassVar[int]
        type: int
        pick: int
        itemid: int
        def __init__(self, type: _Optional[int] = ..., pick: _Optional[int] = ..., itemid: _Optional[int] = ...) -> None: ...
    class FantasyTeam(_message.Message):
        __slots__ = ("sectionid", "slots")
        SECTIONID_FIELD_NUMBER: _ClassVar[int]
        SLOTS_FIELD_NUMBER: _ClassVar[int]
        sectionid: int
        slots: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Fantasy.FantasySlot]
        def __init__(self, sectionid: _Optional[int] = ..., slots: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Fantasy.FantasySlot, _Mapping]]] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    teams: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Fantasy.FantasyTeam]
    def __init__(self, event_id: _Optional[int] = ..., teams: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Fantasy.FantasyTeam, _Mapping]]] = ...) -> None: ...

class CAttribute_String(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class CMsgGCToGCReloadVersions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgCStrike15Welcome(_message.Message):
    __slots__ = ("store_item_hash", "timeplayedconsecutively", "time_first_played", "last_time_played", "last_ip_address", "gscookieid", "uniqueid")
    STORE_ITEM_HASH_FIELD_NUMBER: _ClassVar[int]
    TIMEPLAYEDCONSECUTIVELY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIRST_PLAYED_FIELD_NUMBER: _ClassVar[int]
    LAST_TIME_PLAYED_FIELD_NUMBER: _ClassVar[int]
    LAST_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GSCOOKIEID_FIELD_NUMBER: _ClassVar[int]
    UNIQUEID_FIELD_NUMBER: _ClassVar[int]
    store_item_hash: int
    timeplayedconsecutively: int
    time_first_played: int
    last_time_played: int
    last_ip_address: int
    gscookieid: int
    uniqueid: int
    def __init__(self, store_item_hash: _Optional[int] = ..., timeplayedconsecutively: _Optional[int] = ..., time_first_played: _Optional[int] = ..., last_time_played: _Optional[int] = ..., last_ip_address: _Optional[int] = ..., gscookieid: _Optional[int] = ..., uniqueid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientVarValueNotificationInfo(_message.Message):
    __slots__ = ("value_name", "value_int", "server_addr", "server_port", "choked_blocks")
    VALUE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_INT_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    CHOKED_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    value_name: str
    value_int: int
    server_addr: int
    server_port: int
    choked_blocks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value_name: _Optional[str] = ..., value_int: _Optional[int] = ..., server_addr: _Optional[int] = ..., server_port: _Optional[int] = ..., choked_blocks: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ServerVarValueNotificationInfo(_message.Message):
    __slots__ = ("accountid", "viewangles", "type")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    VIEWANGLES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    viewangles: _containers.RepeatedScalarFieldContainer[int]
    type: int
    def __init__(self, accountid: _Optional[int] = ..., viewangles: _Optional[_Iterable[int]] = ..., type: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_GiftsLeaderboardRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgGCCStrike15_v2_GiftsLeaderboardResponse(_message.Message):
    __slots__ = ("servertime", "time_period_seconds", "total_gifts_given", "total_givers", "entries")
    class GiftLeaderboardEntry(_message.Message):
        __slots__ = ("accountid", "gifts")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        GIFTS_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        gifts: int
        def __init__(self, accountid: _Optional[int] = ..., gifts: _Optional[int] = ...) -> None: ...
    SERVERTIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GIFTS_GIVEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GIVERS_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    servertime: int
    time_period_seconds: int
    total_gifts_given: int
    total_givers: int
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_GiftsLeaderboardResponse.GiftLeaderboardEntry]
    def __init__(self, servertime: _Optional[int] = ..., time_period_seconds: _Optional[int] = ..., total_gifts_given: _Optional[int] = ..., total_givers: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_GiftsLeaderboardResponse.GiftLeaderboardEntry, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientSubmitSurveyVote(_message.Message):
    __slots__ = ("survey_id", "vote")
    SURVEY_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    survey_id: int
    vote: int
    def __init__(self, survey_id: _Optional[int] = ..., vote: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Server2GCClientValidate(_message.Message):
    __slots__ = ("accountid",)
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    def __init__(self, accountid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Server2GCPureServerValidationFailure(_message.Message):
    __slots__ = ("accountid", "path", "file", "crc", "hash", "len", "pack_number", "pack_file_id")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    PACK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PACK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    path: str
    file: str
    crc: int
    hash: int
    len: int
    pack_number: int
    pack_file_id: int
    def __init__(self, accountid: _Optional[int] = ..., path: _Optional[str] = ..., file: _Optional[str] = ..., crc: _Optional[int] = ..., hash: _Optional[int] = ..., len: _Optional[int] = ..., pack_number: _Optional[int] = ..., pack_file_id: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientTournamentInfo(_message.Message):
    __slots__ = ("eventid", "stageid", "game_type", "teamids")
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    STAGEID_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEAMIDS_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    stageid: int
    game_type: int
    teamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, eventid: _Optional[int] = ..., stageid: _Optional[int] = ..., game_type: _Optional[int] = ..., teamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CSOEconCoupon(_message.Message):
    __slots__ = ("entryid", "defidx", "expiration_date")
    ENTRYID_FIELD_NUMBER: _ClassVar[int]
    DEFIDX_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    entryid: int
    defidx: int
    expiration_date: int
    def __init__(self, entryid: _Optional[int] = ..., defidx: _Optional[int] = ..., expiration_date: _Optional[int] = ...) -> None: ...

class CSOQuestProgress(_message.Message):
    __slots__ = ("questid", "points_remaining", "bonus_points")
    QUESTID_FIELD_NUMBER: _ClassVar[int]
    POINTS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    BONUS_POINTS_FIELD_NUMBER: _ClassVar[int]
    questid: int
    points_remaining: int
    bonus_points: int
    def __init__(self, questid: _Optional[int] = ..., points_remaining: _Optional[int] = ..., bonus_points: _Optional[int] = ...) -> None: ...

class CSOAccountSeasonalOperation(_message.Message):
    __slots__ = ("season_value", "tier_unlocked", "premium_tiers", "mission_id", "missions_completed")
    SEASON_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIER_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_TIERS_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    season_value: int
    tier_unlocked: int
    premium_tiers: int
    mission_id: int
    missions_completed: int
    def __init__(self, season_value: _Optional[int] = ..., tier_unlocked: _Optional[int] = ..., premium_tiers: _Optional[int] = ..., mission_id: _Optional[int] = ..., missions_completed: _Optional[int] = ...) -> None: ...

class CSOPersonaDataPublic(_message.Message):
    __slots__ = ("player_level", "commendation", "elevated_state")
    PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    COMMENDATION_FIELD_NUMBER: _ClassVar[int]
    ELEVATED_STATE_FIELD_NUMBER: _ClassVar[int]
    player_level: int
    commendation: PlayerCommendationInfo
    elevated_state: bool
    def __init__(self, player_level: _Optional[int] = ..., commendation: _Optional[_Union[PlayerCommendationInfo, _Mapping]] = ..., elevated_state: bool = ...) -> None: ...

class CMsgGC_GlobalGame_Subscribe(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: int
    def __init__(self, ticket: _Optional[int] = ...) -> None: ...

class CMsgGC_GlobalGame_Unsubscribe(_message.Message):
    __slots__ = ("timeleft",)
    TIMELEFT_FIELD_NUMBER: _ClassVar[int]
    timeleft: int
    def __init__(self, timeleft: _Optional[int] = ...) -> None: ...

class CMsgGC_GlobalGame_Play(_message.Message):
    __slots__ = ("ticket", "gametimems", "msperpoint")
    TICKET_FIELD_NUMBER: _ClassVar[int]
    GAMETIMEMS_FIELD_NUMBER: _ClassVar[int]
    MSPERPOINT_FIELD_NUMBER: _ClassVar[int]
    ticket: int
    gametimems: int
    msperpoint: int
    def __init__(self, ticket: _Optional[int] = ..., gametimems: _Optional[int] = ..., msperpoint: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_AcknowledgePenalty(_message.Message):
    __slots__ = ("acknowledged",)
    ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    acknowledged: int
    def __init__(self, acknowledged: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin(_message.Message):
    __slots__ = ("defindex", "upgradeid", "hours", "prestigetime")
    DEFINDEX_FIELD_NUMBER: _ClassVar[int]
    UPGRADEID_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    PRESTIGETIME_FIELD_NUMBER: _ClassVar[int]
    defindex: int
    upgradeid: int
    hours: int
    prestigetime: int
    def __init__(self, defindex: _Optional[int] = ..., upgradeid: _Optional[int] = ..., hours: _Optional[int] = ..., prestigetime: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Client2GCStreamUnlock(_message.Message):
    __slots__ = ("ticket", "os")
    TICKET_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    ticket: int
    os: int
    def __init__(self, ticket: _Optional[int] = ..., os: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientToGCRequestElevate(_message.Message):
    __slots__ = ("stage",)
    STAGE_FIELD_NUMBER: _ClassVar[int]
    stage: int
    def __init__(self, stage: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientToGCChat(_message.Message):
    __slots__ = ("match_id", "text")
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    text: str
    def __init__(self, match_id: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_GCToClientChat(_message.Message):
    __slots__ = ("account_id", "text")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    text: str
    def __init__(self, account_id: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientAuthKeyCode(_message.Message):
    __slots__ = ("eventid", "code")
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    code: str
    def __init__(self, eventid: _Optional[int] = ..., code: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_GotvSyncPacket(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _engine_gcmessages_pb2.CEngineGotvSyncPacket
    def __init__(self, data: _Optional[_Union[_engine_gcmessages_pb2.CEngineGotvSyncPacket, _Mapping]] = ...) -> None: ...

class PlayerDecalDigitalSignature(_message.Message):
    __slots__ = ("signature", "accountid", "rtime", "endpos", "startpos", "right", "tx_defidx", "entindex", "hitbox", "creationtime", "equipslot", "trace_id", "normal", "tint_id")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    RTIME_FIELD_NUMBER: _ClassVar[int]
    ENDPOS_FIELD_NUMBER: _ClassVar[int]
    STARTPOS_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    TX_DEFIDX_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    HITBOX_FIELD_NUMBER: _ClassVar[int]
    CREATIONTIME_FIELD_NUMBER: _ClassVar[int]
    EQUIPSLOT_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    TINT_ID_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    accountid: int
    rtime: int
    endpos: _containers.RepeatedScalarFieldContainer[float]
    startpos: _containers.RepeatedScalarFieldContainer[float]
    right: _containers.RepeatedScalarFieldContainer[float]
    tx_defidx: int
    entindex: int
    hitbox: int
    creationtime: float
    equipslot: int
    trace_id: int
    normal: _containers.RepeatedScalarFieldContainer[float]
    tint_id: int
    def __init__(self, signature: _Optional[bytes] = ..., accountid: _Optional[int] = ..., rtime: _Optional[int] = ..., endpos: _Optional[_Iterable[float]] = ..., startpos: _Optional[_Iterable[float]] = ..., right: _Optional[_Iterable[float]] = ..., tx_defidx: _Optional[int] = ..., entindex: _Optional[int] = ..., hitbox: _Optional[int] = ..., creationtime: _Optional[float] = ..., equipslot: _Optional[int] = ..., trace_id: _Optional[int] = ..., normal: _Optional[_Iterable[float]] = ..., tint_id: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPlayerDecalSign(_message.Message):
    __slots__ = ("data", "itemid")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    data: PlayerDecalDigitalSignature
    itemid: int
    def __init__(self, data: _Optional[_Union[PlayerDecalDigitalSignature, _Mapping]] = ..., itemid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientLogonFatalError(_message.Message):
    __slots__ = ("errorcode", "message", "country")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    errorcode: int
    message: str
    country: str
    def __init__(self, errorcode: _Optional[int] = ..., message: _Optional[str] = ..., country: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPollState(_message.Message):
    __slots__ = ("pollid", "names", "values")
    POLLID_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    pollid: int
    names: _containers.RepeatedScalarFieldContainer[str]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, pollid: _Optional[int] = ..., names: _Optional[_Iterable[str]] = ..., values: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Party_Register(_message.Message):
    __slots__ = ("id", "ver", "apr", "ark", "nby", "grp", "slots", "launcher", "game_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    VER_FIELD_NUMBER: _ClassVar[int]
    APR_FIELD_NUMBER: _ClassVar[int]
    ARK_FIELD_NUMBER: _ClassVar[int]
    NBY_FIELD_NUMBER: _ClassVar[int]
    GRP_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    ver: int
    apr: int
    ark: int
    nby: int
    grp: int
    slots: int
    launcher: int
    game_type: int
    def __init__(self, id: _Optional[int] = ..., ver: _Optional[int] = ..., apr: _Optional[int] = ..., ark: _Optional[int] = ..., nby: _Optional[int] = ..., grp: _Optional[int] = ..., slots: _Optional[int] = ..., launcher: _Optional[int] = ..., game_type: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Party_Search(_message.Message):
    __slots__ = ("ver", "apr", "ark", "grps", "launcher", "game_type")
    VER_FIELD_NUMBER: _ClassVar[int]
    APR_FIELD_NUMBER: _ClassVar[int]
    ARK_FIELD_NUMBER: _ClassVar[int]
    GRPS_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    ver: int
    apr: int
    ark: int
    grps: _containers.RepeatedScalarFieldContainer[int]
    launcher: int
    game_type: int
    def __init__(self, ver: _Optional[int] = ..., apr: _Optional[int] = ..., ark: _Optional[int] = ..., grps: _Optional[_Iterable[int]] = ..., launcher: _Optional[int] = ..., game_type: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Party_SearchResults(_message.Message):
    __slots__ = ("entries",)
    class Entry(_message.Message):
        __slots__ = ("id", "grp", "game_type", "apr", "ark", "loc")
        ID_FIELD_NUMBER: _ClassVar[int]
        GRP_FIELD_NUMBER: _ClassVar[int]
        GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
        APR_FIELD_NUMBER: _ClassVar[int]
        ARK_FIELD_NUMBER: _ClassVar[int]
        LOC_FIELD_NUMBER: _ClassVar[int]
        id: int
        grp: int
        game_type: int
        apr: int
        ark: int
        loc: int
        def __init__(self, id: _Optional[int] = ..., grp: _Optional[int] = ..., game_type: _Optional[int] = ..., apr: _Optional[int] = ..., ark: _Optional[int] = ..., loc: _Optional[int] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Party_SearchResults.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Party_SearchResults.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_Party_Invite(_message.Message):
    __slots__ = ("accountid", "lobbyid")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    lobbyid: int
    def __init__(self, accountid: _Optional[int] = ..., lobbyid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_Account_RequestCoPlays(_message.Message):
    __slots__ = ("players", "servertime")
    class Player(_message.Message):
        __slots__ = ("accountid", "rtcoplay", "online")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        RTCOPLAY_FIELD_NUMBER: _ClassVar[int]
        ONLINE_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        rtcoplay: int
        online: bool
        def __init__(self, accountid: _Optional[int] = ..., rtcoplay: _Optional[int] = ..., online: bool = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    SERVERTIME_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_Account_RequestCoPlays.Player]
    servertime: int
    def __init__(self, players: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_Account_RequestCoPlays.Player, _Mapping]]] = ..., servertime: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientToGCRequestTicket(_message.Message):
    __slots__ = ("authorized_steam_id", "authorized_public_ip", "gameserver_steam_id", "gameserver_sdr_routing")
    AUTHORIZED_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    GAMESERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    GAMESERVER_SDR_ROUTING_FIELD_NUMBER: _ClassVar[int]
    authorized_steam_id: int
    authorized_public_ip: int
    gameserver_steam_id: int
    gameserver_sdr_routing: str
    def __init__(self, authorized_steam_id: _Optional[int] = ..., authorized_public_ip: _Optional[int] = ..., gameserver_steam_id: _Optional[int] = ..., gameserver_sdr_routing: _Optional[str] = ...) -> None: ...

class CMsgGCToClientSteamDatagramTicket(_message.Message):
    __slots__ = ("serialized_ticket",)
    SERIALIZED_TICKET_FIELD_NUMBER: _ClassVar[int]
    serialized_ticket: bytes
    def __init__(self, serialized_ticket: _Optional[bytes] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestOffers(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgGCCStrike15_v2_ClientRequestSouvenir(_message.Message):
    __slots__ = ("itemid", "matchid", "eventid")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    itemid: int
    matchid: int
    eventid: int
    def __init__(self, itemid: _Optional[int] = ..., matchid: _Optional[int] = ..., eventid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientAccountBalance(_message.Message):
    __slots__ = ("amount", "url")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    amount: int
    url: str
    def __init__(self, amount: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPartyJoinRelay(_message.Message):
    __slots__ = ("accountid", "lobbyid")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    lobbyid: int
    def __init__(self, accountid: _Optional[int] = ..., lobbyid: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPartyWarning(_message.Message):
    __slots__ = ("entries",)
    class Entry(_message.Message):
        __slots__ = ("accountid", "warntype")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        WARNTYPE_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        warntype: int
        def __init__(self, accountid: _Optional[int] = ..., warntype: _Optional[int] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_ClientPartyWarning.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_ClientPartyWarning.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_SetEventFavorite(_message.Message):
    __slots__ = ("eventid", "is_favorite")
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    IS_FAVORITE_FIELD_NUMBER: _ClassVar[int]
    eventid: int
    is_favorite: bool
    def __init__(self, eventid: _Optional[int] = ..., is_favorite: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_GetEventFavorites_Request(_message.Message):
    __slots__ = ("all_events",)
    ALL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    all_events: bool
    def __init__(self, all_events: bool = ...) -> None: ...

class CMsgGCCStrike15_v2_GetEventFavorites_Response(_message.Message):
    __slots__ = ("all_events", "json_favorites", "json_featured")
    ALL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    JSON_FAVORITES_FIELD_NUMBER: _ClassVar[int]
    JSON_FEATURED_FIELD_NUMBER: _ClassVar[int]
    all_events: bool
    json_favorites: str
    json_featured: str
    def __init__(self, all_events: bool = ..., json_favorites: _Optional[str] = ..., json_featured: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientPerfReport(_message.Message):
    __slots__ = ("entries",)
    class Entry(_message.Message):
        __slots__ = ("perfcounter", "length", "reference", "actual", "sourceid", "status")
        PERFCOUNTER_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        ACTUAL_FIELD_NUMBER: _ClassVar[int]
        SOURCEID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        perfcounter: int
        length: int
        reference: bytes
        actual: bytes
        sourceid: int
        status: int
        def __init__(self, perfcounter: _Optional[int] = ..., length: _Optional[int] = ..., reference: _Optional[bytes] = ..., actual: _Optional[bytes] = ..., sourceid: _Optional[int] = ..., status: _Optional[int] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCCStrike15_v2_ClientPerfReport.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCCStrike15_v2_ClientPerfReport.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCCStrike15_v2_ClientReportValidation(_message.Message):
    __slots__ = ("file_report", "command_line", "total_files", "internal_error", "trust_time", "count_pending", "count_completed", "process_id")
    FILE_REPORT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_LINE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    TRUST_TIME_FIELD_NUMBER: _ClassVar[int]
    COUNT_PENDING_FIELD_NUMBER: _ClassVar[int]
    COUNT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    file_report: str
    command_line: str
    total_files: int
    internal_error: int
    trust_time: int
    count_pending: int
    count_completed: int
    process_id: int
    def __init__(self, file_report: _Optional[str] = ..., command_line: _Optional[str] = ..., total_files: _Optional[int] = ..., internal_error: _Optional[int] = ..., trust_time: _Optional[int] = ..., count_pending: _Optional[int] = ..., count_completed: _Optional[int] = ..., process_id: _Optional[int] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientRefuseSecureMode(_message.Message):
    __slots__ = ("file_report",)
    FILE_REPORT_FIELD_NUMBER: _ClassVar[int]
    file_report: str
    def __init__(self, file_report: _Optional[str] = ...) -> None: ...

class CMsgGCCStrike15_v2_GC2ClientRequestValidation(_message.Message):
    __slots__ = ("full_report",)
    FULL_REPORT_FIELD_NUMBER: _ClassVar[int]
    full_report: bool
    def __init__(self, full_report: bool = ...) -> None: ...
