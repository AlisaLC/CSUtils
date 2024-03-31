from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GCProtoBufMsgSrc(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GCProtoBufMsgSrc_Unspecified: _ClassVar[GCProtoBufMsgSrc]
    GCProtoBufMsgSrc_FromSystem: _ClassVar[GCProtoBufMsgSrc]
    GCProtoBufMsgSrc_FromSteamID: _ClassVar[GCProtoBufMsgSrc]
    GCProtoBufMsgSrc_FromGC: _ClassVar[GCProtoBufMsgSrc]
    GCProtoBufMsgSrc_ReplySystem: _ClassVar[GCProtoBufMsgSrc]
GCProtoBufMsgSrc_Unspecified: GCProtoBufMsgSrc
GCProtoBufMsgSrc_FromSystem: GCProtoBufMsgSrc
GCProtoBufMsgSrc_FromSteamID: GCProtoBufMsgSrc
GCProtoBufMsgSrc_FromGC: GCProtoBufMsgSrc
GCProtoBufMsgSrc_ReplySystem: GCProtoBufMsgSrc
KEY_FIELD_FIELD_NUMBER: _ClassVar[int]
key_field: _descriptor.FieldDescriptor
MSGPOOL_SOFT_LIMIT_FIELD_NUMBER: _ClassVar[int]
msgpool_soft_limit: _descriptor.FieldDescriptor
MSGPOOL_HARD_LIMIT_FIELD_NUMBER: _ClassVar[int]
msgpool_hard_limit: _descriptor.FieldDescriptor

class CMsgProtoBufHeader(_message.Message):
    __slots__ = ("client_steam_id", "client_session_id", "source_app_id", "job_id_source", "job_id_target", "target_job_name", "eresult", "error_message", "ip", "gc_msg_src", "gc_dir_index_source")
    CLIENT_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_APP_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    GC_MSG_SRC_FIELD_NUMBER: _ClassVar[int]
    GC_DIR_INDEX_SOURCE_FIELD_NUMBER: _ClassVar[int]
    client_steam_id: int
    client_session_id: int
    source_app_id: int
    job_id_source: int
    job_id_target: int
    target_job_name: str
    eresult: int
    error_message: str
    ip: int
    gc_msg_src: GCProtoBufMsgSrc
    gc_dir_index_source: int
    def __init__(self, client_steam_id: _Optional[int] = ..., client_session_id: _Optional[int] = ..., source_app_id: _Optional[int] = ..., job_id_source: _Optional[int] = ..., job_id_target: _Optional[int] = ..., target_job_name: _Optional[str] = ..., eresult: _Optional[int] = ..., error_message: _Optional[str] = ..., ip: _Optional[int] = ..., gc_msg_src: _Optional[_Union[GCProtoBufMsgSrc, str]] = ..., gc_dir_index_source: _Optional[int] = ...) -> None: ...

class CMsgWebAPIKey(_message.Message):
    __slots__ = ("status", "account_id", "publisher_group_id", "key_id", "domain")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    status: int
    account_id: int
    publisher_group_id: int
    key_id: int
    domain: str
    def __init__(self, status: _Optional[int] = ..., account_id: _Optional[int] = ..., publisher_group_id: _Optional[int] = ..., key_id: _Optional[int] = ..., domain: _Optional[str] = ...) -> None: ...

class CMsgHttpRequest(_message.Message):
    __slots__ = ("request_method", "hostname", "url", "headers", "get_params", "post_params", "body", "absolute_timeout")
    class RequestHeader(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class QueryParam(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: bytes
        def __init__(self, name: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    REQUEST_METHOD_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    GET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    POST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    request_method: int
    hostname: str
    url: str
    headers: _containers.RepeatedCompositeFieldContainer[CMsgHttpRequest.RequestHeader]
    get_params: _containers.RepeatedCompositeFieldContainer[CMsgHttpRequest.QueryParam]
    post_params: _containers.RepeatedCompositeFieldContainer[CMsgHttpRequest.QueryParam]
    body: bytes
    absolute_timeout: int
    def __init__(self, request_method: _Optional[int] = ..., hostname: _Optional[str] = ..., url: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[CMsgHttpRequest.RequestHeader, _Mapping]]] = ..., get_params: _Optional[_Iterable[_Union[CMsgHttpRequest.QueryParam, _Mapping]]] = ..., post_params: _Optional[_Iterable[_Union[CMsgHttpRequest.QueryParam, _Mapping]]] = ..., body: _Optional[bytes] = ..., absolute_timeout: _Optional[int] = ...) -> None: ...

class CMsgWebAPIRequest(_message.Message):
    __slots__ = ("UNUSED_job_name", "interface_name", "method_name", "version", "api_key", "request", "routing_app_id")
    UNUSED_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ROUTING_APP_ID_FIELD_NUMBER: _ClassVar[int]
    UNUSED_job_name: str
    interface_name: str
    method_name: str
    version: int
    api_key: CMsgWebAPIKey
    request: CMsgHttpRequest
    routing_app_id: int
    def __init__(self, UNUSED_job_name: _Optional[str] = ..., interface_name: _Optional[str] = ..., method_name: _Optional[str] = ..., version: _Optional[int] = ..., api_key: _Optional[_Union[CMsgWebAPIKey, _Mapping]] = ..., request: _Optional[_Union[CMsgHttpRequest, _Mapping]] = ..., routing_app_id: _Optional[int] = ...) -> None: ...

class CMsgHttpResponse(_message.Message):
    __slots__ = ("status_code", "headers", "body")
    class ResponseHeader(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    headers: _containers.RepeatedCompositeFieldContainer[CMsgHttpResponse.ResponseHeader]
    body: bytes
    def __init__(self, status_code: _Optional[int] = ..., headers: _Optional[_Iterable[_Union[CMsgHttpResponse.ResponseHeader, _Mapping]]] = ..., body: _Optional[bytes] = ...) -> None: ...

class CMsgAMFindAccounts(_message.Message):
    __slots__ = ("search_type", "search_string")
    SEARCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    search_type: int
    search_string: str
    def __init__(self, search_type: _Optional[int] = ..., search_string: _Optional[str] = ...) -> None: ...

class CMsgAMFindAccountsResponse(_message.Message):
    __slots__ = ("steam_id",)
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steam_id: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgNotifyWatchdog(_message.Message):
    __slots__ = ("source", "alert_type", "alert_destination", "critical", "time", "appid", "text")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALERT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    source: int
    alert_type: int
    alert_destination: int
    critical: bool
    time: int
    appid: int
    text: str
    def __init__(self, source: _Optional[int] = ..., alert_type: _Optional[int] = ..., alert_destination: _Optional[int] = ..., critical: bool = ..., time: _Optional[int] = ..., appid: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgAMGetLicenses(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CMsgPackageLicense(_message.Message):
    __slots__ = ("package_id", "time_created", "owner_id")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    package_id: int
    time_created: int
    owner_id: int
    def __init__(self, package_id: _Optional[int] = ..., time_created: _Optional[int] = ..., owner_id: _Optional[int] = ...) -> None: ...

class CMsgAMGetLicensesResponse(_message.Message):
    __slots__ = ("license", "result")
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    license: _containers.RepeatedCompositeFieldContainer[CMsgPackageLicense]
    result: int
    def __init__(self, license: _Optional[_Iterable[_Union[CMsgPackageLicense, _Mapping]]] = ..., result: _Optional[int] = ...) -> None: ...

class CMsgAMGetUserGameStats(_message.Message):
    __slots__ = ("steam_id", "game_id", "stats")
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    game_id: int
    stats: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steam_id: _Optional[int] = ..., game_id: _Optional[int] = ..., stats: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgAMGetUserGameStatsResponse(_message.Message):
    __slots__ = ("steam_id", "game_id", "eresult", "stats", "achievement_blocks")
    class Stats(_message.Message):
        __slots__ = ("stat_id", "stat_value")
        STAT_ID_FIELD_NUMBER: _ClassVar[int]
        STAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        stat_id: int
        stat_value: int
        def __init__(self, stat_id: _Optional[int] = ..., stat_value: _Optional[int] = ...) -> None: ...
    class Achievement_Blocks(_message.Message):
        __slots__ = ("achievement_id", "achievement_bit_id", "unlock_time")
        ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ACHIEVEMENT_BIT_ID_FIELD_NUMBER: _ClassVar[int]
        UNLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
        achievement_id: int
        achievement_bit_id: int
        unlock_time: int
        def __init__(self, achievement_id: _Optional[int] = ..., achievement_bit_id: _Optional[int] = ..., unlock_time: _Optional[int] = ...) -> None: ...
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENT_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    game_id: int
    eresult: int
    stats: _containers.RepeatedCompositeFieldContainer[CMsgAMGetUserGameStatsResponse.Stats]
    achievement_blocks: _containers.RepeatedCompositeFieldContainer[CMsgAMGetUserGameStatsResponse.Achievement_Blocks]
    def __init__(self, steam_id: _Optional[int] = ..., game_id: _Optional[int] = ..., eresult: _Optional[int] = ..., stats: _Optional[_Iterable[_Union[CMsgAMGetUserGameStatsResponse.Stats, _Mapping]]] = ..., achievement_blocks: _Optional[_Iterable[_Union[CMsgAMGetUserGameStatsResponse.Achievement_Blocks, _Mapping]]] = ...) -> None: ...

class CMsgGCGetCommandList(_message.Message):
    __slots__ = ("app_id", "command_prefix")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_PREFIX_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    command_prefix: str
    def __init__(self, app_id: _Optional[int] = ..., command_prefix: _Optional[str] = ...) -> None: ...

class CMsgGCGetCommandListResponse(_message.Message):
    __slots__ = ("command_name",)
    COMMAND_NAME_FIELD_NUMBER: _ClassVar[int]
    command_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, command_name: _Optional[_Iterable[str]] = ...) -> None: ...

class CGCMsgMemCachedGet(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ...) -> None: ...

class CGCMsgMemCachedGetResponse(_message.Message):
    __slots__ = ("values",)
    class ValueTag(_message.Message):
        __slots__ = ("found", "value")
        FOUND_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        found: bool
        value: bytes
        def __init__(self, found: bool = ..., value: _Optional[bytes] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[CGCMsgMemCachedGetResponse.ValueTag]
    def __init__(self, values: _Optional[_Iterable[_Union[CGCMsgMemCachedGetResponse.ValueTag, _Mapping]]] = ...) -> None: ...

class CGCMsgMemCachedSet(_message.Message):
    __slots__ = ("keys",)
    class KeyPair(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: bytes
        def __init__(self, name: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[CGCMsgMemCachedSet.KeyPair]
    def __init__(self, keys: _Optional[_Iterable[_Union[CGCMsgMemCachedSet.KeyPair, _Mapping]]] = ...) -> None: ...

class CGCMsgMemCachedDelete(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ...) -> None: ...

class CGCMsgMemCachedStats(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGCMsgMemCachedStatsResponse(_message.Message):
    __slots__ = ("curr_connections", "cmd_get", "cmd_set", "cmd_flush", "get_hits", "get_misses", "delete_hits", "delete_misses", "bytes_read", "bytes_written", "limit_maxbytes", "curr_items", "evictions", "bytes")
    CURR_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    CMD_GET_FIELD_NUMBER: _ClassVar[int]
    CMD_SET_FIELD_NUMBER: _ClassVar[int]
    CMD_FLUSH_FIELD_NUMBER: _ClassVar[int]
    GET_HITS_FIELD_NUMBER: _ClassVar[int]
    GET_MISSES_FIELD_NUMBER: _ClassVar[int]
    DELETE_HITS_FIELD_NUMBER: _ClassVar[int]
    DELETE_MISSES_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_MAXBYTES_FIELD_NUMBER: _ClassVar[int]
    CURR_ITEMS_FIELD_NUMBER: _ClassVar[int]
    EVICTIONS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    curr_connections: int
    cmd_get: int
    cmd_set: int
    cmd_flush: int
    get_hits: int
    get_misses: int
    delete_hits: int
    delete_misses: int
    bytes_read: int
    bytes_written: int
    limit_maxbytes: int
    curr_items: int
    evictions: int
    bytes: int
    def __init__(self, curr_connections: _Optional[int] = ..., cmd_get: _Optional[int] = ..., cmd_set: _Optional[int] = ..., cmd_flush: _Optional[int] = ..., get_hits: _Optional[int] = ..., get_misses: _Optional[int] = ..., delete_hits: _Optional[int] = ..., delete_misses: _Optional[int] = ..., bytes_read: _Optional[int] = ..., bytes_written: _Optional[int] = ..., limit_maxbytes: _Optional[int] = ..., curr_items: _Optional[int] = ..., evictions: _Optional[int] = ..., bytes: _Optional[int] = ...) -> None: ...

class CGCMsgSQLStats(_message.Message):
    __slots__ = ("schema_catalog",)
    SCHEMA_CATALOG_FIELD_NUMBER: _ClassVar[int]
    schema_catalog: int
    def __init__(self, schema_catalog: _Optional[int] = ...) -> None: ...

class CGCMsgSQLStatsResponse(_message.Message):
    __slots__ = ("threads", "threads_connected", "threads_active", "operations_submitted", "prepared_statements_executed", "non_prepared_statements_executed", "deadlock_retries", "operations_timed_out_in_queue", "errors")
    THREADS_FIELD_NUMBER: _ClassVar[int]
    THREADS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    THREADS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_SUBMITTED_FIELD_NUMBER: _ClassVar[int]
    PREPARED_STATEMENTS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    NON_PREPARED_STATEMENTS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    DEADLOCK_RETRIES_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_TIMED_OUT_IN_QUEUE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    threads: int
    threads_connected: int
    threads_active: int
    operations_submitted: int
    prepared_statements_executed: int
    non_prepared_statements_executed: int
    deadlock_retries: int
    operations_timed_out_in_queue: int
    errors: int
    def __init__(self, threads: _Optional[int] = ..., threads_connected: _Optional[int] = ..., threads_active: _Optional[int] = ..., operations_submitted: _Optional[int] = ..., prepared_statements_executed: _Optional[int] = ..., non_prepared_statements_executed: _Optional[int] = ..., deadlock_retries: _Optional[int] = ..., operations_timed_out_in_queue: _Optional[int] = ..., errors: _Optional[int] = ...) -> None: ...

class CMsgAMAddFreeLicense(_message.Message):
    __slots__ = ("steamid", "ip_public", "packageid", "store_country_code")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    IP_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    STORE_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    ip_public: int
    packageid: int
    store_country_code: str
    def __init__(self, steamid: _Optional[int] = ..., ip_public: _Optional[int] = ..., packageid: _Optional[int] = ..., store_country_code: _Optional[str] = ...) -> None: ...

class CMsgAMAddFreeLicenseResponse(_message.Message):
    __slots__ = ("eresult", "purchase_result_detail", "transid")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_RESULT_DETAIL_FIELD_NUMBER: _ClassVar[int]
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    purchase_result_detail: int
    transid: int
    def __init__(self, eresult: _Optional[int] = ..., purchase_result_detail: _Optional[int] = ..., transid: _Optional[int] = ...) -> None: ...

class CGCMsgGetIPLocation(_message.Message):
    __slots__ = ("ips",)
    IPS_FIELD_NUMBER: _ClassVar[int]
    ips: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ips: _Optional[_Iterable[int]] = ...) -> None: ...

class CIPLocationInfo(_message.Message):
    __slots__ = ("ip", "latitude", "longitude", "country", "state", "city")
    IP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ip: int
    latitude: float
    longitude: float
    country: str
    state: str
    city: str
    def __init__(self, ip: _Optional[int] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., country: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...

class CGCMsgGetIPLocationResponse(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[CIPLocationInfo]
    def __init__(self, infos: _Optional[_Iterable[_Union[CIPLocationInfo, _Mapping]]] = ...) -> None: ...

class CGCMsgSystemStatsSchema(_message.Message):
    __slots__ = ("gc_app_id", "schema_kv")
    GC_APP_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KV_FIELD_NUMBER: _ClassVar[int]
    gc_app_id: int
    schema_kv: bytes
    def __init__(self, gc_app_id: _Optional[int] = ..., schema_kv: _Optional[bytes] = ...) -> None: ...

class CGCMsgGetSystemStats(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGCMsgGetSystemStatsResponse(_message.Message):
    __slots__ = ("gc_app_id", "stats_kv", "active_jobs", "yielding_jobs", "user_sessions", "game_server_sessions", "socaches", "socaches_to_unload", "socaches_loading", "writeback_queue", "steamid_locks", "logon_queue", "logon_jobs")
    GC_APP_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_KV_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_JOBS_FIELD_NUMBER: _ClassVar[int]
    YIELDING_JOBS_FIELD_NUMBER: _ClassVar[int]
    USER_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    SOCACHES_FIELD_NUMBER: _ClassVar[int]
    SOCACHES_TO_UNLOAD_FIELD_NUMBER: _ClassVar[int]
    SOCACHES_LOADING_FIELD_NUMBER: _ClassVar[int]
    WRITEBACK_QUEUE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_LOCKS_FIELD_NUMBER: _ClassVar[int]
    LOGON_QUEUE_FIELD_NUMBER: _ClassVar[int]
    LOGON_JOBS_FIELD_NUMBER: _ClassVar[int]
    gc_app_id: int
    stats_kv: bytes
    active_jobs: int
    yielding_jobs: int
    user_sessions: int
    game_server_sessions: int
    socaches: int
    socaches_to_unload: int
    socaches_loading: int
    writeback_queue: int
    steamid_locks: int
    logon_queue: int
    logon_jobs: int
    def __init__(self, gc_app_id: _Optional[int] = ..., stats_kv: _Optional[bytes] = ..., active_jobs: _Optional[int] = ..., yielding_jobs: _Optional[int] = ..., user_sessions: _Optional[int] = ..., game_server_sessions: _Optional[int] = ..., socaches: _Optional[int] = ..., socaches_to_unload: _Optional[int] = ..., socaches_loading: _Optional[int] = ..., writeback_queue: _Optional[int] = ..., steamid_locks: _Optional[int] = ..., logon_queue: _Optional[int] = ..., logon_jobs: _Optional[int] = ...) -> None: ...

class CMsgAMSendEmail(_message.Message):
    __slots__ = ("steamid", "email_msg_type", "email_format", "persona_name_tokens", "source_gc", "tokens")
    class ReplacementToken(_message.Message):
        __slots__ = ("token_name", "token_value")
        TOKEN_NAME_FIELD_NUMBER: _ClassVar[int]
        TOKEN_VALUE_FIELD_NUMBER: _ClassVar[int]
        token_name: str
        token_value: str
        def __init__(self, token_name: _Optional[str] = ..., token_value: _Optional[str] = ...) -> None: ...
    class PersonaNameReplacementToken(_message.Message):
        __slots__ = ("steamid", "token_name")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        TOKEN_NAME_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        token_name: str
        def __init__(self, steamid: _Optional[int] = ..., token_name: _Optional[str] = ...) -> None: ...
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GC_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    email_msg_type: int
    email_format: int
    persona_name_tokens: _containers.RepeatedCompositeFieldContainer[CMsgAMSendEmail.PersonaNameReplacementToken]
    source_gc: int
    tokens: _containers.RepeatedCompositeFieldContainer[CMsgAMSendEmail.ReplacementToken]
    def __init__(self, steamid: _Optional[int] = ..., email_msg_type: _Optional[int] = ..., email_format: _Optional[int] = ..., persona_name_tokens: _Optional[_Iterable[_Union[CMsgAMSendEmail.PersonaNameReplacementToken, _Mapping]]] = ..., source_gc: _Optional[int] = ..., tokens: _Optional[_Iterable[_Union[CMsgAMSendEmail.ReplacementToken, _Mapping]]] = ...) -> None: ...

class CMsgAMSendEmailResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgGCGetEmailTemplate(_message.Message):
    __slots__ = ("app_id", "email_msg_type", "email_lang", "email_format")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_LANG_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    email_msg_type: int
    email_lang: int
    email_format: int
    def __init__(self, app_id: _Optional[int] = ..., email_msg_type: _Optional[int] = ..., email_lang: _Optional[int] = ..., email_format: _Optional[int] = ...) -> None: ...

class CMsgGCGetEmailTemplateResponse(_message.Message):
    __slots__ = ("eresult", "template_exists", "template")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_EXISTS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    template_exists: bool
    template: str
    def __init__(self, eresult: _Optional[int] = ..., template_exists: bool = ..., template: _Optional[str] = ...) -> None: ...

class CMsgAMGrantGuestPasses2(_message.Message):
    __slots__ = ("steam_id", "package_id", "passes_to_grant", "days_to_expiration", "action")
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PASSES_TO_GRANT_FIELD_NUMBER: _ClassVar[int]
    DAYS_TO_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    package_id: int
    passes_to_grant: int
    days_to_expiration: int
    action: int
    def __init__(self, steam_id: _Optional[int] = ..., package_id: _Optional[int] = ..., passes_to_grant: _Optional[int] = ..., days_to_expiration: _Optional[int] = ..., action: _Optional[int] = ...) -> None: ...

class CMsgAMGrantGuestPasses2Response(_message.Message):
    __slots__ = ("eresult", "passes_granted")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PASSES_GRANTED_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    passes_granted: int
    def __init__(self, eresult: _Optional[int] = ..., passes_granted: _Optional[int] = ...) -> None: ...

class CGCSystemMsg_GetAccountDetails(_message.Message):
    __slots__ = ("steamid", "appid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    appid: int
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CGCSystemMsg_GetAccountDetails_Response(_message.Message):
    __slots__ = ("eresult_deprecated", "account_name", "persona_name", "is_profile_public", "is_inventory_public", "is_vac_banned", "is_cyber_cafe", "is_school_account", "is_limited", "is_subscribed", "package", "is_free_trial_account", "free_trial_expiration", "is_low_violence", "is_account_locked_down", "is_community_banned", "is_trade_banned", "trade_ban_expiration", "accountid", "suspension_end_time", "currency", "steam_level", "friend_count", "account_creation_time", "is_steamguard_enabled", "is_phone_verified", "is_two_factor_auth_enabled", "two_factor_enabled_time", "phone_verification_time", "phone_id", "is_phone_identifying", "rt_identity_linked", "rt_birth_date", "txn_country_code")
    ERESULT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PROFILE_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IS_INVENTORY_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IS_VAC_BANNED_FIELD_NUMBER: _ClassVar[int]
    IS_CYBER_CAFE_FIELD_NUMBER: _ClassVar[int]
    IS_SCHOOL_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_LIMITED_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_TRIAL_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    FREE_TRIAL_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    IS_LOW_VIOLENCE_FIELD_NUMBER: _ClassVar[int]
    IS_ACCOUNT_LOCKED_DOWN_FIELD_NUMBER: _ClassVar[int]
    IS_COMMUNITY_BANNED_FIELD_NUMBER: _ClassVar[int]
    IS_TRADE_BANNED_FIELD_NUMBER: _ClassVar[int]
    TRADE_BAN_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    STEAM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    FRIEND_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_STEAMGUARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_TWO_FACTOR_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_ENABLED_TIME_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    PHONE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_IDENTIFYING_FIELD_NUMBER: _ClassVar[int]
    RT_IDENTITY_LINKED_FIELD_NUMBER: _ClassVar[int]
    RT_BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    TXN_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    eresult_deprecated: int
    account_name: str
    persona_name: str
    is_profile_public: bool
    is_inventory_public: bool
    is_vac_banned: bool
    is_cyber_cafe: bool
    is_school_account: bool
    is_limited: bool
    is_subscribed: bool
    package: int
    is_free_trial_account: bool
    free_trial_expiration: int
    is_low_violence: bool
    is_account_locked_down: bool
    is_community_banned: bool
    is_trade_banned: bool
    trade_ban_expiration: int
    accountid: int
    suspension_end_time: int
    currency: str
    steam_level: int
    friend_count: int
    account_creation_time: int
    is_steamguard_enabled: bool
    is_phone_verified: bool
    is_two_factor_auth_enabled: bool
    two_factor_enabled_time: int
    phone_verification_time: int
    phone_id: int
    is_phone_identifying: bool
    rt_identity_linked: int
    rt_birth_date: int
    txn_country_code: str
    def __init__(self, eresult_deprecated: _Optional[int] = ..., account_name: _Optional[str] = ..., persona_name: _Optional[str] = ..., is_profile_public: bool = ..., is_inventory_public: bool = ..., is_vac_banned: bool = ..., is_cyber_cafe: bool = ..., is_school_account: bool = ..., is_limited: bool = ..., is_subscribed: bool = ..., package: _Optional[int] = ..., is_free_trial_account: bool = ..., free_trial_expiration: _Optional[int] = ..., is_low_violence: bool = ..., is_account_locked_down: bool = ..., is_community_banned: bool = ..., is_trade_banned: bool = ..., trade_ban_expiration: _Optional[int] = ..., accountid: _Optional[int] = ..., suspension_end_time: _Optional[int] = ..., currency: _Optional[str] = ..., steam_level: _Optional[int] = ..., friend_count: _Optional[int] = ..., account_creation_time: _Optional[int] = ..., is_steamguard_enabled: bool = ..., is_phone_verified: bool = ..., is_two_factor_auth_enabled: bool = ..., two_factor_enabled_time: _Optional[int] = ..., phone_verification_time: _Optional[int] = ..., phone_id: _Optional[int] = ..., is_phone_identifying: bool = ..., rt_identity_linked: _Optional[int] = ..., rt_birth_date: _Optional[int] = ..., txn_country_code: _Optional[str] = ...) -> None: ...

class CMsgGCGetPersonaNames(_message.Message):
    __slots__ = ("steamids",)
    STEAMIDS_FIELD_NUMBER: _ClassVar[int]
    steamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCGetPersonaNames_Response(_message.Message):
    __slots__ = ("succeeded_lookups", "failed_lookup_steamids")
    class PersonaName(_message.Message):
        __slots__ = ("steamid", "persona_name")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        persona_name: str
        def __init__(self, steamid: _Optional[int] = ..., persona_name: _Optional[str] = ...) -> None: ...
    SUCCEEDED_LOOKUPS_FIELD_NUMBER: _ClassVar[int]
    FAILED_LOOKUP_STEAMIDS_FIELD_NUMBER: _ClassVar[int]
    succeeded_lookups: _containers.RepeatedCompositeFieldContainer[CMsgGCGetPersonaNames_Response.PersonaName]
    failed_lookup_steamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, succeeded_lookups: _Optional[_Iterable[_Union[CMsgGCGetPersonaNames_Response.PersonaName, _Mapping]]] = ..., failed_lookup_steamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgGCCheckFriendship(_message.Message):
    __slots__ = ("steamid_left", "steamid_right")
    STEAMID_LEFT_FIELD_NUMBER: _ClassVar[int]
    STEAMID_RIGHT_FIELD_NUMBER: _ClassVar[int]
    steamid_left: int
    steamid_right: int
    def __init__(self, steamid_left: _Optional[int] = ..., steamid_right: _Optional[int] = ...) -> None: ...

class CMsgGCCheckFriendship_Response(_message.Message):
    __slots__ = ("success", "found_friendship")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FOUND_FRIENDSHIP_FIELD_NUMBER: _ClassVar[int]
    success: bool
    found_friendship: bool
    def __init__(self, success: bool = ..., found_friendship: bool = ...) -> None: ...

class CMsgGCMsgMasterSetDirectory(_message.Message):
    __slots__ = ("master_dir_index", "dir")
    class SubGC(_message.Message):
        __slots__ = ("dir_index", "name", "box", "command_line", "gc_binary")
        DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        BOX_FIELD_NUMBER: _ClassVar[int]
        COMMAND_LINE_FIELD_NUMBER: _ClassVar[int]
        GC_BINARY_FIELD_NUMBER: _ClassVar[int]
        dir_index: int
        name: str
        box: str
        command_line: str
        gc_binary: str
        def __init__(self, dir_index: _Optional[int] = ..., name: _Optional[str] = ..., box: _Optional[str] = ..., command_line: _Optional[str] = ..., gc_binary: _Optional[str] = ...) -> None: ...
    MASTER_DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    master_dir_index: int
    dir: _containers.RepeatedCompositeFieldContainer[CMsgGCMsgMasterSetDirectory.SubGC]
    def __init__(self, master_dir_index: _Optional[int] = ..., dir: _Optional[_Iterable[_Union[CMsgGCMsgMasterSetDirectory.SubGC, _Mapping]]] = ...) -> None: ...

class CMsgGCMsgMasterSetDirectory_Response(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgGCMsgWebAPIJobRequestForwardResponse(_message.Message):
    __slots__ = ("dir_index",)
    DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
    dir_index: int
    def __init__(self, dir_index: _Optional[int] = ...) -> None: ...

class CGCSystemMsg_GetPurchaseTrust_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CGCSystemMsg_GetPurchaseTrust_Response(_message.Message):
    __slots__ = ("has_prior_purchase_history", "has_no_recent_password_resets", "is_wallet_cash_trusted", "time_all_trusted")
    HAS_PRIOR_PURCHASE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    HAS_NO_RECENT_PASSWORD_RESETS_FIELD_NUMBER: _ClassVar[int]
    IS_WALLET_CASH_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    TIME_ALL_TRUSTED_FIELD_NUMBER: _ClassVar[int]
    has_prior_purchase_history: bool
    has_no_recent_password_resets: bool
    is_wallet_cash_trusted: bool
    time_all_trusted: int
    def __init__(self, has_prior_purchase_history: bool = ..., has_no_recent_password_resets: bool = ..., is_wallet_cash_trusted: bool = ..., time_all_trusted: _Optional[int] = ...) -> None: ...

class CMsgGCHAccountVacStatusChange(_message.Message):
    __slots__ = ("steam_id", "app_id", "rtime_vacban_starts", "is_banned_now", "is_banned_future")
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    RTIME_VACBAN_STARTS_FIELD_NUMBER: _ClassVar[int]
    IS_BANNED_NOW_FIELD_NUMBER: _ClassVar[int]
    IS_BANNED_FUTURE_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    app_id: int
    rtime_vacban_starts: int
    is_banned_now: bool
    is_banned_future: bool
    def __init__(self, steam_id: _Optional[int] = ..., app_id: _Optional[int] = ..., rtime_vacban_starts: _Optional[int] = ..., is_banned_now: bool = ..., is_banned_future: bool = ...) -> None: ...

class CMsgGCGetPartnerAccountLink(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CMsgGCGetPartnerAccountLink_Response(_message.Message):
    __slots__ = ("pwid", "nexonid", "ageclass", "id_verified", "is_adult")
    PWID_FIELD_NUMBER: _ClassVar[int]
    NEXONID_FIELD_NUMBER: _ClassVar[int]
    AGECLASS_FIELD_NUMBER: _ClassVar[int]
    ID_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_ADULT_FIELD_NUMBER: _ClassVar[int]
    pwid: int
    nexonid: int
    ageclass: int
    id_verified: bool
    is_adult: bool
    def __init__(self, pwid: _Optional[int] = ..., nexonid: _Optional[int] = ..., ageclass: _Optional[int] = ..., id_verified: bool = ..., is_adult: bool = ...) -> None: ...

class CMsgGCRoutingInfo(_message.Message):
    __slots__ = ("dir_index", "method", "fallback", "protobuf_field", "webapi_param")
    class RoutingMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RANDOM: _ClassVar[CMsgGCRoutingInfo.RoutingMethod]
        DISCARD: _ClassVar[CMsgGCRoutingInfo.RoutingMethod]
        CLIENT_STEAMID: _ClassVar[CMsgGCRoutingInfo.RoutingMethod]
        PROTOBUF_FIELD_UINT64: _ClassVar[CMsgGCRoutingInfo.RoutingMethod]
        WEBAPI_PARAM_UINT64: _ClassVar[CMsgGCRoutingInfo.RoutingMethod]
    RANDOM: CMsgGCRoutingInfo.RoutingMethod
    DISCARD: CMsgGCRoutingInfo.RoutingMethod
    CLIENT_STEAMID: CMsgGCRoutingInfo.RoutingMethod
    PROTOBUF_FIELD_UINT64: CMsgGCRoutingInfo.RoutingMethod
    WEBAPI_PARAM_UINT64: CMsgGCRoutingInfo.RoutingMethod
    DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_FIELD_NUMBER: _ClassVar[int]
    PROTOBUF_FIELD_FIELD_NUMBER: _ClassVar[int]
    WEBAPI_PARAM_FIELD_NUMBER: _ClassVar[int]
    dir_index: _containers.RepeatedScalarFieldContainer[int]
    method: CMsgGCRoutingInfo.RoutingMethod
    fallback: CMsgGCRoutingInfo.RoutingMethod
    protobuf_field: int
    webapi_param: str
    def __init__(self, dir_index: _Optional[_Iterable[int]] = ..., method: _Optional[_Union[CMsgGCRoutingInfo.RoutingMethod, str]] = ..., fallback: _Optional[_Union[CMsgGCRoutingInfo.RoutingMethod, str]] = ..., protobuf_field: _Optional[int] = ..., webapi_param: _Optional[str] = ...) -> None: ...

class CMsgGCMsgMasterSetWebAPIRouting(_message.Message):
    __slots__ = ("entries",)
    class Entry(_message.Message):
        __slots__ = ("interface_name", "method_name", "routing")
        INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
        ROUTING_FIELD_NUMBER: _ClassVar[int]
        interface_name: str
        method_name: str
        routing: CMsgGCRoutingInfo
        def __init__(self, interface_name: _Optional[str] = ..., method_name: _Optional[str] = ..., routing: _Optional[_Union[CMsgGCRoutingInfo, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCMsgMasterSetWebAPIRouting.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCMsgMasterSetWebAPIRouting.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCMsgMasterSetClientMsgRouting(_message.Message):
    __slots__ = ("entries",)
    class Entry(_message.Message):
        __slots__ = ("msg_type", "routing")
        MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
        ROUTING_FIELD_NUMBER: _ClassVar[int]
        msg_type: int
        routing: CMsgGCRoutingInfo
        def __init__(self, msg_type: _Optional[int] = ..., routing: _Optional[_Union[CMsgGCRoutingInfo, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgGCMsgMasterSetClientMsgRouting.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgGCMsgMasterSetClientMsgRouting.Entry, _Mapping]]] = ...) -> None: ...

class CMsgGCMsgMasterSetWebAPIRouting_Response(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgGCMsgMasterSetClientMsgRouting_Response(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgGCMsgSetOptions(_message.Message):
    __slots__ = ("options", "client_msg_ranges")
    class Option(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFY_USER_SESSIONS: _ClassVar[CMsgGCMsgSetOptions.Option]
        NOTIFY_SERVER_SESSIONS: _ClassVar[CMsgGCMsgSetOptions.Option]
        NOTIFY_ACHIEVEMENTS: _ClassVar[CMsgGCMsgSetOptions.Option]
        NOTIFY_VAC_ACTION: _ClassVar[CMsgGCMsgSetOptions.Option]
    NOTIFY_USER_SESSIONS: CMsgGCMsgSetOptions.Option
    NOTIFY_SERVER_SESSIONS: CMsgGCMsgSetOptions.Option
    NOTIFY_ACHIEVEMENTS: CMsgGCMsgSetOptions.Option
    NOTIFY_VAC_ACTION: CMsgGCMsgSetOptions.Option
    class MessageRange(_message.Message):
        __slots__ = ("low", "high")
        LOW_FIELD_NUMBER: _ClassVar[int]
        HIGH_FIELD_NUMBER: _ClassVar[int]
        low: int
        high: int
        def __init__(self, low: _Optional[int] = ..., high: _Optional[int] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_MSG_RANGES_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedScalarFieldContainer[CMsgGCMsgSetOptions.Option]
    client_msg_ranges: _containers.RepeatedCompositeFieldContainer[CMsgGCMsgSetOptions.MessageRange]
    def __init__(self, options: _Optional[_Iterable[_Union[CMsgGCMsgSetOptions.Option, str]]] = ..., client_msg_ranges: _Optional[_Iterable[_Union[CMsgGCMsgSetOptions.MessageRange, _Mapping]]] = ...) -> None: ...

class CMsgGCHUpdateSession(_message.Message):
    __slots__ = ("steam_id", "app_id", "online", "server_steam_id", "server_addr", "server_port", "os_type", "client_addr", "extra_fields", "owner_id", "cm_session_sysid", "cm_session_identifier", "depot_ids")
    class ExtraField(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ADDR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELDS_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    CM_SESSION_SYSID_FIELD_NUMBER: _ClassVar[int]
    CM_SESSION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DEPOT_IDS_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    app_id: int
    online: bool
    server_steam_id: int
    server_addr: int
    server_port: int
    os_type: int
    client_addr: int
    extra_fields: _containers.RepeatedCompositeFieldContainer[CMsgGCHUpdateSession.ExtraField]
    owner_id: int
    cm_session_sysid: int
    cm_session_identifier: int
    depot_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steam_id: _Optional[int] = ..., app_id: _Optional[int] = ..., online: bool = ..., server_steam_id: _Optional[int] = ..., server_addr: _Optional[int] = ..., server_port: _Optional[int] = ..., os_type: _Optional[int] = ..., client_addr: _Optional[int] = ..., extra_fields: _Optional[_Iterable[_Union[CMsgGCHUpdateSession.ExtraField, _Mapping]]] = ..., owner_id: _Optional[int] = ..., cm_session_sysid: _Optional[int] = ..., cm_session_identifier: _Optional[int] = ..., depot_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgNotificationOfSuspiciousActivity(_message.Message):
    __slots__ = ("steamid", "appid", "multiple_instances")
    class MultipleGameInstances(_message.Message):
        __slots__ = ("app_instance_count", "other_steamids")
        APP_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        OTHER_STEAMIDS_FIELD_NUMBER: _ClassVar[int]
        app_instance_count: int
        other_steamids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, app_instance_count: _Optional[int] = ..., other_steamids: _Optional[_Iterable[int]] = ...) -> None: ...
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    appid: int
    multiple_instances: CMsgNotificationOfSuspiciousActivity.MultipleGameInstances
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ..., multiple_instances: _Optional[_Union[CMsgNotificationOfSuspiciousActivity.MultipleGameInstances, _Mapping]] = ...) -> None: ...

class CMsgDPPartnerMicroTxns(_message.Message):
    __slots__ = ("appid", "gc_name", "partner", "transactions")
    class PartnerMicroTxn(_message.Message):
        __slots__ = ("init_time", "last_update_time", "txn_id", "account_id", "line_item", "item_id", "def_index", "price", "tax", "price_usd", "tax_usd", "purchase_type", "steam_txn_type", "country_code", "region_code", "quantity", "ref_trans_id")
        INIT_TIME_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        TXN_ID_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        LINE_ITEM_FIELD_NUMBER: _ClassVar[int]
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        DEF_INDEX_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        TAX_FIELD_NUMBER: _ClassVar[int]
        PRICE_USD_FIELD_NUMBER: _ClassVar[int]
        TAX_USD_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STEAM_TXN_TYPE_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        REF_TRANS_ID_FIELD_NUMBER: _ClassVar[int]
        init_time: int
        last_update_time: int
        txn_id: int
        account_id: int
        line_item: int
        item_id: int
        def_index: int
        price: int
        tax: int
        price_usd: int
        tax_usd: int
        purchase_type: int
        steam_txn_type: int
        country_code: str
        region_code: str
        quantity: int
        ref_trans_id: int
        def __init__(self, init_time: _Optional[int] = ..., last_update_time: _Optional[int] = ..., txn_id: _Optional[int] = ..., account_id: _Optional[int] = ..., line_item: _Optional[int] = ..., item_id: _Optional[int] = ..., def_index: _Optional[int] = ..., price: _Optional[int] = ..., tax: _Optional[int] = ..., price_usd: _Optional[int] = ..., tax_usd: _Optional[int] = ..., purchase_type: _Optional[int] = ..., steam_txn_type: _Optional[int] = ..., country_code: _Optional[str] = ..., region_code: _Optional[str] = ..., quantity: _Optional[int] = ..., ref_trans_id: _Optional[int] = ...) -> None: ...
    class PartnerInfo(_message.Message):
        __slots__ = ("partner_id", "partner_name", "currency_code", "currency_name")
        PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
        PARTNER_NAME_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_NAME_FIELD_NUMBER: _ClassVar[int]
        partner_id: int
        partner_name: str
        currency_code: str
        currency_name: str
        def __init__(self, partner_id: _Optional[int] = ..., partner_name: _Optional[str] = ..., currency_code: _Optional[str] = ..., currency_name: _Optional[str] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    GC_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    gc_name: str
    partner: CMsgDPPartnerMicroTxns.PartnerInfo
    transactions: _containers.RepeatedCompositeFieldContainer[CMsgDPPartnerMicroTxns.PartnerMicroTxn]
    def __init__(self, appid: _Optional[int] = ..., gc_name: _Optional[str] = ..., partner: _Optional[_Union[CMsgDPPartnerMicroTxns.PartnerInfo, _Mapping]] = ..., transactions: _Optional[_Iterable[_Union[CMsgDPPartnerMicroTxns.PartnerMicroTxn, _Mapping]]] = ...) -> None: ...

class CMsgDPPartnerMicroTxnsResponse(_message.Message):
    __slots__ = ("eresult", "eerrorcode")
    class EErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        k_MsgValid: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
        k_MsgInvalidAppID: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
        k_MsgInvalidPartnerInfo: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
        k_MsgNoTransactions: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
        k_MsgSQLFailure: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
        k_MsgPartnerInfoDiscrepancy: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
        k_MsgTransactionInsertFailed: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
        k_MsgAlreadyRunning: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
        k_MsgInvalidTransactionData: _ClassVar[CMsgDPPartnerMicroTxnsResponse.EErrorCode]
    k_MsgValid: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgInvalidAppID: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgInvalidPartnerInfo: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgNoTransactions: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgSQLFailure: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgPartnerInfoDiscrepancy: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgTransactionInsertFailed: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgAlreadyRunning: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    k_MsgInvalidTransactionData: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    EERRORCODE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    eerrorcode: CMsgDPPartnerMicroTxnsResponse.EErrorCode
    def __init__(self, eresult: _Optional[int] = ..., eerrorcode: _Optional[_Union[CMsgDPPartnerMicroTxnsResponse.EErrorCode, str]] = ...) -> None: ...
