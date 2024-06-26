# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13steammessages.proto\x1a google/protobuf/descriptor.proto\"\xf9\x02\n\x12\x43MsgProtoBufHeader\x12\x17\n\x0f\x63lient_steam_id\x18\x01 \x01(\x06\x12\x19\n\x11\x63lient_session_id\x18\x02 \x01(\x05\x12\x15\n\rsource_app_id\x18\x03 \x01(\r\x12+\n\rjob_id_source\x18\n \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12+\n\rjob_id_target\x18\x0b \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12\x17\n\x0ftarget_job_name\x18\x0c \x01(\t\x12\x12\n\x07\x65result\x18\r \x01(\x05:\x01\x32\x12\x15\n\rerror_message\x18\x0e \x01(\t\x12\n\n\x02ip\x18\x0f \x01(\r\x12\x44\n\ngc_msg_src\x18\xc8\x01 \x01(\x0e\x32\x11.GCProtoBufMsgSrc:\x1cGCProtoBufMsgSrc_Unspecified\x12\x1c\n\x13gc_dir_index_source\x18\xc9\x01 \x01(\r:\n\x80\xa6\x1d\x80\x02\x88\xa6\x1d\x80\x08\"z\n\rCMsgWebAPIKey\x12\x13\n\x06status\x18\x01 \x01(\r:\x03\x32\x35\x35\x12\x15\n\naccount_id\x18\x02 \x01(\r:\x01\x30\x12\x1d\n\x12publisher_group_id\x18\x03 \x01(\r:\x01\x30\x12\x0e\n\x06key_id\x18\x04 \x01(\r\x12\x0e\n\x06\x64omain\x18\x05 \x01(\t\"\xdd\x02\n\x0f\x43MsgHttpRequest\x12\x16\n\x0erequest_method\x18\x01 \x01(\r\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12/\n\x07headers\x18\x04 \x03(\x0b\x32\x1e.CMsgHttpRequest.RequestHeader\x12/\n\nget_params\x18\x05 \x03(\x0b\x32\x1b.CMsgHttpRequest.QueryParam\x12\x30\n\x0bpost_params\x18\x06 \x03(\x0b\x32\x1b.CMsgHttpRequest.QueryParam\x12\x0c\n\x04\x62ody\x18\x07 \x01(\x0c\x12\x18\n\x10\x61\x62solute_timeout\x18\x08 \x01(\r\x1a,\n\rRequestHeader\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a)\n\nQueryParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\xc6\x01\n\x11\x43MsgWebAPIRequest\x12\x17\n\x0fUNUSED_job_name\x18\x01 \x01(\t\x12\x16\n\x0einterface_name\x18\x02 \x01(\t\x12\x13\n\x0bmethod_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\r\x12\x1f\n\x07\x61pi_key\x18\x05 \x01(\x0b\x32\x0e.CMsgWebAPIKey\x12!\n\x07request\x18\x06 \x01(\x0b\x32\x10.CMsgHttpRequest\x12\x16\n\x0erouting_app_id\x18\x07 \x01(\r\"\x97\x01\n\x10\x43MsgHttpResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\r\x12\x31\n\x07headers\x18\x02 \x03(\x0b\x32 .CMsgHttpResponse.ResponseHeader\x12\x0c\n\x04\x62ody\x18\x03 \x01(\x0c\x1a-\n\x0eResponseHeader\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"@\n\x12\x43MsgAMFindAccounts\x12\x13\n\x0bsearch_type\x18\x01 \x01(\r\x12\x15\n\rsearch_string\x18\x02 \x01(\t\".\n\x1a\x43MsgAMFindAccountsResponse\x12\x10\n\x08steam_id\x18\x01 \x03(\x06\"\x90\x01\n\x12\x43MsgNotifyWatchdog\x12\x0e\n\x06source\x18\x01 \x01(\r\x12\x12\n\nalert_type\x18\x02 \x01(\r\x12\x19\n\x11\x61lert_destination\x18\x03 \x01(\r\x12\x10\n\x08\x63ritical\x18\x04 \x01(\x08\x12\x0c\n\x04time\x18\x05 \x01(\r\x12\r\n\x05\x61ppid\x18\x06 \x01(\r\x12\x0c\n\x04text\x18\x07 \x01(\t\"$\n\x11\x43MsgAMGetLicenses\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"P\n\x12\x43MsgPackageLicense\x12\x12\n\npackage_id\x18\x01 \x01(\r\x12\x14\n\x0ctime_created\x18\x02 \x01(\r\x12\x10\n\x08owner_id\x18\x03 \x01(\r\"Q\n\x19\x43MsgAMGetLicensesResponse\x12$\n\x07license\x18\x01 \x03(\x0b\x32\x13.CMsgPackageLicense\x12\x0e\n\x06result\x18\x02 \x01(\r\"J\n\x16\x43MsgAMGetUserGameStats\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x0f\n\x07game_id\x18\x02 \x01(\x06\x12\r\n\x05stats\x18\x03 \x03(\r\"\xea\x02\n\x1e\x43MsgAMGetUserGameStatsResponse\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x0f\n\x07game_id\x18\x02 \x01(\x06\x12\x12\n\x07\x65result\x18\x03 \x01(\x05:\x01\x32\x12\x34\n\x05stats\x18\x04 \x03(\x0b\x32%.CMsgAMGetUserGameStatsResponse.Stats\x12N\n\x12\x61\x63hievement_blocks\x18\x05 \x03(\x0b\x32\x32.CMsgAMGetUserGameStatsResponse.Achievement_Blocks\x1a,\n\x05Stats\x12\x0f\n\x07stat_id\x18\x01 \x01(\r\x12\x12\n\nstat_value\x18\x02 \x01(\r\x1a]\n\x12\x41\x63hievement_Blocks\x12\x16\n\x0e\x61\x63hievement_id\x18\x01 \x01(\r\x12\x1a\n\x12\x61\x63hievement_bit_id\x18\x02 \x01(\r\x12\x13\n\x0bunlock_time\x18\x03 \x01(\x07\">\n\x14\x43MsgGCGetCommandList\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x16\n\x0e\x63ommand_prefix\x18\x02 \x01(\t\"4\n\x1c\x43MsgGCGetCommandListResponse\x12\x14\n\x0c\x63ommand_name\x18\x01 \x03(\t\"\"\n\x12\x43GCMsgMemCachedGet\x12\x0c\n\x04keys\x18\x01 \x03(\t\"|\n\x1a\x43GCMsgMemCachedGetResponse\x12\x34\n\x06values\x18\x01 \x03(\x0b\x32$.CGCMsgMemCachedGetResponse.ValueTag\x1a(\n\x08ValueTag\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x0c\"g\n\x12\x43GCMsgMemCachedSet\x12)\n\x04keys\x18\x01 \x03(\x0b\x32\x1b.CGCMsgMemCachedSet.KeyPair\x1a&\n\x07KeyPair\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"%\n\x15\x43GCMsgMemCachedDelete\x12\x0c\n\x04keys\x18\x01 \x03(\t\"\x16\n\x14\x43GCMsgMemCachedStats\"\xb8\x02\n\x1c\x43GCMsgMemCachedStatsResponse\x12\x18\n\x10\x63urr_connections\x18\x01 \x01(\x04\x12\x0f\n\x07\x63md_get\x18\x02 \x01(\x04\x12\x0f\n\x07\x63md_set\x18\x03 \x01(\x04\x12\x11\n\tcmd_flush\x18\x04 \x01(\x04\x12\x10\n\x08get_hits\x18\x05 \x01(\x04\x12\x12\n\nget_misses\x18\x06 \x01(\x04\x12\x13\n\x0b\x64\x65lete_hits\x18\x07 \x01(\x04\x12\x15\n\rdelete_misses\x18\x08 \x01(\x04\x12\x12\n\nbytes_read\x18\t \x01(\x04\x12\x15\n\rbytes_written\x18\n \x01(\x04\x12\x16\n\x0elimit_maxbytes\x18\x0b \x01(\x04\x12\x12\n\ncurr_items\x18\x0c \x01(\x04\x12\x11\n\tevictions\x18\r \x01(\x04\x12\r\n\x05\x62ytes\x18\x0e \x01(\x04\"(\n\x0e\x43GCMsgSQLStats\x12\x16\n\x0eschema_catalog\x18\x01 \x01(\r\"\x9b\x02\n\x16\x43GCMsgSQLStatsResponse\x12\x0f\n\x07threads\x18\x01 \x01(\r\x12\x19\n\x11threads_connected\x18\x02 \x01(\r\x12\x16\n\x0ethreads_active\x18\x03 \x01(\r\x12\x1c\n\x14operations_submitted\x18\x04 \x01(\r\x12$\n\x1cprepared_statements_executed\x18\x05 \x01(\r\x12(\n non_prepared_statements_executed\x18\x06 \x01(\r\x12\x18\n\x10\x64\x65\x61\x64lock_retries\x18\x07 \x01(\r\x12%\n\x1doperations_timed_out_in_queue\x18\x08 \x01(\r\x12\x0e\n\x06\x65rrors\x18\t \x01(\r\"i\n\x14\x43MsgAMAddFreeLicense\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x11\n\tip_public\x18\x02 \x01(\r\x12\x11\n\tpackageid\x18\x03 \x01(\r\x12\x1a\n\x12store_country_code\x18\x04 \x01(\t\"c\n\x1c\x43MsgAMAddFreeLicenseResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x1e\n\x16purchase_result_detail\x18\x02 \x01(\x05\x12\x0f\n\x07transid\x18\x03 \x01(\x06\"\"\n\x13\x43GCMsgGetIPLocation\x12\x0b\n\x03ips\x18\x01 \x03(\x07\"p\n\x0f\x43IPLocationInfo\x12\n\n\x02ip\x18\x01 \x01(\r\x12\x10\n\x08latitude\x18\x02 \x01(\x02\x12\x11\n\tlongitude\x18\x03 \x01(\x02\x12\x0f\n\x07\x63ountry\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x0c\n\x04\x63ity\x18\x06 \x01(\t\">\n\x1b\x43GCMsgGetIPLocationResponse\x12\x1f\n\x05infos\x18\x01 \x03(\x0b\x32\x10.CIPLocationInfo\"?\n\x17\x43GCMsgSystemStatsSchema\x12\x11\n\tgc_app_id\x18\x01 \x01(\r\x12\x11\n\tschema_kv\x18\x02 \x01(\x0c\"\x16\n\x14\x43GCMsgGetSystemStats\"\xc5\x02\n\x1c\x43GCMsgGetSystemStatsResponse\x12\x11\n\tgc_app_id\x18\x01 \x01(\r\x12\x10\n\x08stats_kv\x18\x02 \x01(\x0c\x12\x13\n\x0b\x61\x63tive_jobs\x18\x03 \x01(\r\x12\x15\n\ryielding_jobs\x18\x04 \x01(\r\x12\x15\n\ruser_sessions\x18\x05 \x01(\r\x12\x1c\n\x14game_server_sessions\x18\x06 \x01(\r\x12\x10\n\x08socaches\x18\x07 \x01(\r\x12\x1a\n\x12socaches_to_unload\x18\x08 \x01(\r\x12\x18\n\x10socaches_loading\x18\t \x01(\r\x12\x17\n\x0fwriteback_queue\x18\n \x01(\r\x12\x15\n\rsteamid_locks\x18\x0b \x01(\r\x12\x13\n\x0blogon_queue\x18\x0c \x01(\r\x12\x12\n\nlogon_jobs\x18\r \x01(\r\"\xe2\x02\n\x0f\x43MsgAMSendEmail\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x16\n\x0e\x65mail_msg_type\x18\x02 \x01(\r\x12\x14\n\x0c\x65mail_format\x18\x03 \x01(\r\x12I\n\x13persona_name_tokens\x18\x05 \x03(\x0b\x32,.CMsgAMSendEmail.PersonaNameReplacementToken\x12\x11\n\tsource_gc\x18\x06 \x01(\r\x12\x31\n\x06tokens\x18\x07 \x03(\x0b\x32!.CMsgAMSendEmail.ReplacementToken\x1a;\n\x10ReplacementToken\x12\x12\n\ntoken_name\x18\x01 \x01(\t\x12\x13\n\x0btoken_value\x18\x02 \x01(\t\x1a\x42\n\x1bPersonaNameReplacementToken\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x12\n\ntoken_name\x18\x02 \x01(\t\"-\n\x17\x43MsgAMSendEmailResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\"j\n\x16\x43MsgGCGetEmailTemplate\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x16\n\x0e\x65mail_msg_type\x18\x02 \x01(\r\x12\x12\n\nemail_lang\x18\x03 \x01(\x05\x12\x14\n\x0c\x65mail_format\x18\x04 \x01(\x05\"_\n\x1e\x43MsgGCGetEmailTemplateResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\x12\x17\n\x0ftemplate_exists\x18\x02 \x01(\x08\x12\x10\n\x08template\x18\x03 \x01(\t\"\x84\x01\n\x17\x43MsgAMGrantGuestPasses2\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x12\n\npackage_id\x18\x02 \x01(\r\x12\x17\n\x0fpasses_to_grant\x18\x03 \x01(\x05\x12\x1a\n\x12\x64\x61ys_to_expiration\x18\x04 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x05 \x01(\x05\"P\n\x1f\x43MsgAMGrantGuestPasses2Response\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x19\n\x0epasses_granted\x18\x02 \x01(\x05:\x01\x30\"L\n\x1e\x43GCSystemMsg_GetAccountDetails\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r:\n\x80\xa6\x1d\x80\x01\x88\xa6\x1d\x80\x04\"\xb1\x07\n\'CGCSystemMsg_GetAccountDetails_Response\x12\x1d\n\x12\x65result_deprecated\x18\x01 \x01(\r:\x01\x32\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x02 \x01(\t\x12\x14\n\x0cpersona_name\x18\x03 \x01(\t\x12\x19\n\x11is_profile_public\x18\x04 \x01(\x08\x12\x1b\n\x13is_inventory_public\x18\x05 \x01(\x08\x12\x15\n\ris_vac_banned\x18\x07 \x01(\x08\x12\x15\n\ris_cyber_cafe\x18\x08 \x01(\x08\x12\x19\n\x11is_school_account\x18\t \x01(\x08\x12\x12\n\nis_limited\x18\n \x01(\x08\x12\x15\n\ris_subscribed\x18\x0b \x01(\x08\x12\x0f\n\x07package\x18\x0c \x01(\r\x12\x1d\n\x15is_free_trial_account\x18\r \x01(\x08\x12\x1d\n\x15\x66ree_trial_expiration\x18\x0e \x01(\r\x12\x17\n\x0fis_low_violence\x18\x0f \x01(\x08\x12\x1e\n\x16is_account_locked_down\x18\x10 \x01(\x08\x12\x1b\n\x13is_community_banned\x18\x11 \x01(\x08\x12\x17\n\x0fis_trade_banned\x18\x12 \x01(\x08\x12\x1c\n\x14trade_ban_expiration\x18\x13 \x01(\r\x12\x11\n\taccountid\x18\x14 \x01(\r\x12\x1b\n\x13suspension_end_time\x18\x15 \x01(\r\x12\x10\n\x08\x63urrency\x18\x16 \x01(\t\x12\x13\n\x0bsteam_level\x18\x17 \x01(\r\x12\x14\n\x0c\x66riend_count\x18\x18 \x01(\r\x12\x1d\n\x15\x61\x63\x63ount_creation_time\x18\x19 \x01(\r\x12\x1d\n\x15is_steamguard_enabled\x18\x1b \x01(\x08\x12\x19\n\x11is_phone_verified\x18\x1c \x01(\x08\x12\"\n\x1ais_two_factor_auth_enabled\x18\x1d \x01(\x08\x12\x1f\n\x17two_factor_enabled_time\x18\x1e \x01(\r\x12\x1f\n\x17phone_verification_time\x18\x1f \x01(\r\x12\x10\n\x08phone_id\x18! \x01(\x04\x12\x1c\n\x14is_phone_identifying\x18\" \x01(\x08\x12\x1a\n\x12rt_identity_linked\x18# \x01(\r\x12\x15\n\rrt_birth_date\x18$ \x01(\r\x12\x18\n\x10txn_country_code\x18% \x01(\t:\n\x80\xa6\x1d\x80\x01\x88\xa6\x1d\x80\x04\")\n\x15\x43MsgGCGetPersonaNames\x12\x10\n\x08steamids\x18\x01 \x03(\x06\"\xbe\x01\n\x1e\x43MsgGCGetPersonaNames_Response\x12\x46\n\x11succeeded_lookups\x18\x01 \x03(\x0b\x32+.CMsgGCGetPersonaNames_Response.PersonaName\x12\x1e\n\x16\x66\x61iled_lookup_steamids\x18\x02 \x03(\x06\x1a\x34\n\x0bPersonaName\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x14\n\x0cpersona_name\x18\x02 \x01(\t\"D\n\x15\x43MsgGCCheckFriendship\x12\x14\n\x0csteamid_left\x18\x01 \x01(\x06\x12\x15\n\rsteamid_right\x18\x02 \x01(\x06\"K\n\x1e\x43MsgGCCheckFriendship_Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x18\n\x10\x66ound_friendship\x18\x02 \x01(\x08\"\xc8\x01\n\x1b\x43MsgGCMsgMasterSetDirectory\x12\x18\n\x10master_dir_index\x18\x01 \x01(\r\x12/\n\x03\x64ir\x18\x02 \x03(\x0b\x32\".CMsgGCMsgMasterSetDirectory.SubGC\x1a^\n\x05SubGC\x12\x11\n\tdir_index\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x62ox\x18\x03 \x01(\t\x12\x14\n\x0c\x63ommand_line\x18\x04 \x01(\t\x12\x11\n\tgc_binary\x18\x05 \x01(\t\":\n$CMsgGCMsgMasterSetDirectory_Response\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"=\n(CMsgGCMsgWebAPIJobRequestForwardResponse\x12\x11\n\tdir_index\x18\x01 \x01(\r\"8\n%CGCSystemMsg_GetPurchaseTrust_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\xad\x01\n&CGCSystemMsg_GetPurchaseTrust_Response\x12\"\n\x1ahas_prior_purchase_history\x18\x01 \x01(\x08\x12%\n\x1dhas_no_recent_password_resets\x18\x02 \x01(\x08\x12\x1e\n\x16is_wallet_cash_trusted\x18\x03 \x01(\x08\x12\x18\n\x10time_all_trusted\x18\x04 \x01(\r\"\x8f\x01\n\x1d\x43MsgGCHAccountVacStatusChange\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x1b\n\x13rtime_vacban_starts\x18\x03 \x01(\r\x12\x15\n\ris_banned_now\x18\x04 \x01(\x08\x12\x18\n\x10is_banned_future\x18\x05 \x01(\x08\".\n\x1b\x43MsgGCGetPartnerAccountLink\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\x84\x01\n$CMsgGCGetPartnerAccountLink_Response\x12\x0c\n\x04pwid\x18\x01 \x01(\r\x12\x0f\n\x07nexonid\x18\x02 \x01(\r\x12\x10\n\x08\x61geclass\x18\x03 \x01(\x05\x12\x19\n\x0bid_verified\x18\x04 \x01(\x08:\x04true\x12\x10\n\x08is_adult\x18\x05 \x01(\x08\"\xbd\x02\n\x11\x43MsgGCRoutingInfo\x12\x11\n\tdir_index\x18\x01 \x03(\r\x12\x38\n\x06method\x18\x02 \x01(\x0e\x32 .CMsgGCRoutingInfo.RoutingMethod:\x06RANDOM\x12;\n\x08\x66\x61llback\x18\x03 \x01(\x0e\x32 .CMsgGCRoutingInfo.RoutingMethod:\x07\x44ISCARD\x12\x16\n\x0eprotobuf_field\x18\x04 \x01(\r\x12\x14\n\x0cwebapi_param\x18\x05 \x01(\t\"p\n\rRoutingMethod\x12\n\n\x06RANDOM\x10\x00\x12\x0b\n\x07\x44ISCARD\x10\x01\x12\x12\n\x0e\x43LIENT_STEAMID\x10\x02\x12\x19\n\x15PROTOBUF_FIELD_UINT64\x10\x03\x12\x17\n\x13WEBAPI_PARAM_UINT64\x10\x04\"\xb5\x01\n\x1f\x43MsgGCMsgMasterSetWebAPIRouting\x12\x37\n\x07\x65ntries\x18\x01 \x03(\x0b\x32&.CMsgGCMsgMasterSetWebAPIRouting.Entry\x1aY\n\x05\x45ntry\x12\x16\n\x0einterface_name\x18\x01 \x01(\t\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12#\n\x07routing\x18\x03 \x01(\x0b\x32\x12.CMsgGCRoutingInfo\"\xa0\x01\n\"CMsgGCMsgMasterSetClientMsgRouting\x12:\n\x07\x65ntries\x18\x01 \x03(\x0b\x32).CMsgGCMsgMasterSetClientMsgRouting.Entry\x1a>\n\x05\x45ntry\x12\x10\n\x08msg_type\x18\x01 \x01(\r\x12#\n\x07routing\x18\x02 \x01(\x0b\x32\x12.CMsgGCRoutingInfo\">\n(CMsgGCMsgMasterSetWebAPIRouting_Response\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"A\n+CMsgGCMsgMasterSetClientMsgRouting_Response\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"\x9c\x02\n\x13\x43MsgGCMsgSetOptions\x12,\n\x07options\x18\x01 \x03(\x0e\x32\x1b.CMsgGCMsgSetOptions.Option\x12<\n\x11\x63lient_msg_ranges\x18\x02 \x03(\x0b\x32!.CMsgGCMsgSetOptions.MessageRange\x1a)\n\x0cMessageRange\x12\x0b\n\x03low\x18\x01 \x02(\r\x12\x0c\n\x04high\x18\x02 \x02(\r\"n\n\x06Option\x12\x18\n\x14NOTIFY_USER_SESSIONS\x10\x00\x12\x1a\n\x16NOTIFY_SERVER_SESSIONS\x10\x01\x12\x17\n\x13NOTIFY_ACHIEVEMENTS\x10\x02\x12\x15\n\x11NOTIFY_VAC_ACTION\x10\x03\"\xf2\x02\n\x14\x43MsgGCHUpdateSession\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x0e\n\x06online\x18\x03 \x01(\x08\x12\x17\n\x0fserver_steam_id\x18\x04 \x01(\x06\x12\x13\n\x0bserver_addr\x18\x05 \x01(\r\x12\x13\n\x0bserver_port\x18\x06 \x01(\r\x12\x0f\n\x07os_type\x18\x07 \x01(\r\x12\x13\n\x0b\x63lient_addr\x18\x08 \x01(\r\x12\x36\n\x0c\x65xtra_fields\x18\t \x03(\x0b\x32 .CMsgGCHUpdateSession.ExtraField\x12\x10\n\x08owner_id\x18\n \x01(\x06\x12\x18\n\x10\x63m_session_sysid\x18\x0b \x01(\r\x12\x1d\n\x15\x63m_session_identifier\x18\x0c \x01(\r\x12\x11\n\tdepot_ids\x18\r \x03(\r\x1a)\n\nExtraField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xec\x01\n$CMsgNotificationOfSuspiciousActivity\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12W\n\x12multiple_instances\x18\x03 \x01(\x0b\x32;.CMsgNotificationOfSuspiciousActivity.MultipleGameInstances\x1aK\n\x15MultipleGameInstances\x12\x1a\n\x12\x61pp_instance_count\x18\x01 \x01(\r\x12\x16\n\x0eother_steamids\x18\x02 \x03(\x06\"\xf2\x04\n\x16\x43MsgDPPartnerMicroTxns\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07gc_name\x18\x02 \x01(\t\x12\x34\n\x07partner\x18\x03 \x01(\x0b\x32#.CMsgDPPartnerMicroTxns.PartnerInfo\x12=\n\x0ctransactions\x18\x04 \x03(\x0b\x32\'.CMsgDPPartnerMicroTxns.PartnerMicroTxn\x1a\xdb\x02\n\x0fPartnerMicroTxn\x12\x11\n\tinit_time\x18\x01 \x01(\r\x12\x18\n\x10last_update_time\x18\x02 \x01(\r\x12\x0e\n\x06txn_id\x18\x03 \x01(\x04\x12\x12\n\naccount_id\x18\x04 \x01(\r\x12\x11\n\tline_item\x18\x05 \x01(\r\x12\x0f\n\x07item_id\x18\x06 \x01(\x04\x12\x11\n\tdef_index\x18\x07 \x01(\r\x12\r\n\x05price\x18\x08 \x01(\x04\x12\x0b\n\x03tax\x18\t \x01(\x04\x12\x11\n\tprice_usd\x18\n \x01(\x04\x12\x0f\n\x07tax_usd\x18\x0b \x01(\x04\x12\x15\n\rpurchase_type\x18\x0c \x01(\r\x12\x16\n\x0esteam_txn_type\x18\r \x01(\r\x12\x14\n\x0c\x63ountry_code\x18\x0e \x01(\t\x12\x13\n\x0bregion_code\x18\x0f \x01(\t\x12\x10\n\x08quantity\x18\x10 \x01(\x05\x12\x14\n\x0cref_trans_id\x18\x11 \x01(\x04\x1a\x65\n\x0bPartnerInfo\x12\x12\n\npartner_id\x18\x01 \x01(\r\x12\x14\n\x0cpartner_name\x18\x02 \x01(\t\x12\x15\n\rcurrency_code\x18\x03 \x01(\t\x12\x15\n\rcurrency_name\x18\x04 \x01(\t\"\xfe\x02\n\x1e\x43MsgDPPartnerMicroTxnsResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\x12J\n\neerrorcode\x18\x02 \x01(\x0e\x32*.CMsgDPPartnerMicroTxnsResponse.EErrorCode:\nk_MsgValid\"\xfb\x01\n\nEErrorCode\x12\x0e\n\nk_MsgValid\x10\x00\x12\x15\n\x11k_MsgInvalidAppID\x10\x01\x12\x1b\n\x17k_MsgInvalidPartnerInfo\x10\x02\x12\x17\n\x13k_MsgNoTransactions\x10\x03\x12\x13\n\x0fk_MsgSQLFailure\x10\x04\x12\x1f\n\x1bk_MsgPartnerInfoDiscrepancy\x10\x05\x12 \n\x1ck_MsgTransactionInsertFailed\x10\x07\x12\x17\n\x13k_MsgAlreadyRunning\x10\x08\x12\x1f\n\x1bk_MsgInvalidTransactionData\x10\t*\xb6\x01\n\x10GCProtoBufMsgSrc\x12 \n\x1cGCProtoBufMsgSrc_Unspecified\x10\x00\x12\x1f\n\x1bGCProtoBufMsgSrc_FromSystem\x10\x01\x12 \n\x1cGCProtoBufMsgSrc_FromSteamID\x10\x02\x12\x1b\n\x17GCProtoBufMsgSrc_FromGC\x10\x03\x12 \n\x1cGCProtoBufMsgSrc_ReplySystem\x10\x04:9\n\tkey_field\x12\x1d.google.protobuf.FieldOptions\x18\xe0\xd4\x03 \x01(\x08:\x05\x66\x61lse:A\n\x12msgpool_soft_limit\x12\x1f.google.protobuf.MessageOptions\x18\xe0\xd4\x03 \x01(\x05:\x02\x33\x32:B\n\x12msgpool_hard_limit\x12\x1f.google.protobuf.MessageOptions\x18\xe1\xd4\x03 \x01(\x05:\x03\x33\x38\x34\x42\x05H\x01\x80\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\200\001\000'
  _globals['_CMSGPROTOBUFHEADER']._options = None
  _globals['_CMSGPROTOBUFHEADER']._serialized_options = b'\200\246\035\200\002\210\246\035\200\010'
  _globals['_CGCSYSTEMMSG_GETACCOUNTDETAILS']._options = None
  _globals['_CGCSYSTEMMSG_GETACCOUNTDETAILS']._serialized_options = b'\200\246\035\200\001\210\246\035\200\004'
  _globals['_CGCSYSTEMMSG_GETACCOUNTDETAILS_RESPONSE']._options = None
  _globals['_CGCSYSTEMMSG_GETACCOUNTDETAILS_RESPONSE']._serialized_options = b'\200\246\035\200\001\210\246\035\200\004'
  _globals['_GCPROTOBUFMSGSRC']._serialized_start=9939
  _globals['_GCPROTOBUFMSGSRC']._serialized_end=10121
  _globals['_CMSGPROTOBUFHEADER']._serialized_start=58
  _globals['_CMSGPROTOBUFHEADER']._serialized_end=435
  _globals['_CMSGWEBAPIKEY']._serialized_start=437
  _globals['_CMSGWEBAPIKEY']._serialized_end=559
  _globals['_CMSGHTTPREQUEST']._serialized_start=562
  _globals['_CMSGHTTPREQUEST']._serialized_end=911
  _globals['_CMSGHTTPREQUEST_REQUESTHEADER']._serialized_start=824
  _globals['_CMSGHTTPREQUEST_REQUESTHEADER']._serialized_end=868
  _globals['_CMSGHTTPREQUEST_QUERYPARAM']._serialized_start=870
  _globals['_CMSGHTTPREQUEST_QUERYPARAM']._serialized_end=911
  _globals['_CMSGWEBAPIREQUEST']._serialized_start=914
  _globals['_CMSGWEBAPIREQUEST']._serialized_end=1112
  _globals['_CMSGHTTPRESPONSE']._serialized_start=1115
  _globals['_CMSGHTTPRESPONSE']._serialized_end=1266
  _globals['_CMSGHTTPRESPONSE_RESPONSEHEADER']._serialized_start=1221
  _globals['_CMSGHTTPRESPONSE_RESPONSEHEADER']._serialized_end=1266
  _globals['_CMSGAMFINDACCOUNTS']._serialized_start=1268
  _globals['_CMSGAMFINDACCOUNTS']._serialized_end=1332
  _globals['_CMSGAMFINDACCOUNTSRESPONSE']._serialized_start=1334
  _globals['_CMSGAMFINDACCOUNTSRESPONSE']._serialized_end=1380
  _globals['_CMSGNOTIFYWATCHDOG']._serialized_start=1383
  _globals['_CMSGNOTIFYWATCHDOG']._serialized_end=1527
  _globals['_CMSGAMGETLICENSES']._serialized_start=1529
  _globals['_CMSGAMGETLICENSES']._serialized_end=1565
  _globals['_CMSGPACKAGELICENSE']._serialized_start=1567
  _globals['_CMSGPACKAGELICENSE']._serialized_end=1647
  _globals['_CMSGAMGETLICENSESRESPONSE']._serialized_start=1649
  _globals['_CMSGAMGETLICENSESRESPONSE']._serialized_end=1730
  _globals['_CMSGAMGETUSERGAMESTATS']._serialized_start=1732
  _globals['_CMSGAMGETUSERGAMESTATS']._serialized_end=1806
  _globals['_CMSGAMGETUSERGAMESTATSRESPONSE']._serialized_start=1809
  _globals['_CMSGAMGETUSERGAMESTATSRESPONSE']._serialized_end=2171
  _globals['_CMSGAMGETUSERGAMESTATSRESPONSE_STATS']._serialized_start=2032
  _globals['_CMSGAMGETUSERGAMESTATSRESPONSE_STATS']._serialized_end=2076
  _globals['_CMSGAMGETUSERGAMESTATSRESPONSE_ACHIEVEMENT_BLOCKS']._serialized_start=2078
  _globals['_CMSGAMGETUSERGAMESTATSRESPONSE_ACHIEVEMENT_BLOCKS']._serialized_end=2171
  _globals['_CMSGGCGETCOMMANDLIST']._serialized_start=2173
  _globals['_CMSGGCGETCOMMANDLIST']._serialized_end=2235
  _globals['_CMSGGCGETCOMMANDLISTRESPONSE']._serialized_start=2237
  _globals['_CMSGGCGETCOMMANDLISTRESPONSE']._serialized_end=2289
  _globals['_CGCMSGMEMCACHEDGET']._serialized_start=2291
  _globals['_CGCMSGMEMCACHEDGET']._serialized_end=2325
  _globals['_CGCMSGMEMCACHEDGETRESPONSE']._serialized_start=2327
  _globals['_CGCMSGMEMCACHEDGETRESPONSE']._serialized_end=2451
  _globals['_CGCMSGMEMCACHEDGETRESPONSE_VALUETAG']._serialized_start=2411
  _globals['_CGCMSGMEMCACHEDGETRESPONSE_VALUETAG']._serialized_end=2451
  _globals['_CGCMSGMEMCACHEDSET']._serialized_start=2453
  _globals['_CGCMSGMEMCACHEDSET']._serialized_end=2556
  _globals['_CGCMSGMEMCACHEDSET_KEYPAIR']._serialized_start=2518
  _globals['_CGCMSGMEMCACHEDSET_KEYPAIR']._serialized_end=2556
  _globals['_CGCMSGMEMCACHEDDELETE']._serialized_start=2558
  _globals['_CGCMSGMEMCACHEDDELETE']._serialized_end=2595
  _globals['_CGCMSGMEMCACHEDSTATS']._serialized_start=2597
  _globals['_CGCMSGMEMCACHEDSTATS']._serialized_end=2619
  _globals['_CGCMSGMEMCACHEDSTATSRESPONSE']._serialized_start=2622
  _globals['_CGCMSGMEMCACHEDSTATSRESPONSE']._serialized_end=2934
  _globals['_CGCMSGSQLSTATS']._serialized_start=2936
  _globals['_CGCMSGSQLSTATS']._serialized_end=2976
  _globals['_CGCMSGSQLSTATSRESPONSE']._serialized_start=2979
  _globals['_CGCMSGSQLSTATSRESPONSE']._serialized_end=3262
  _globals['_CMSGAMADDFREELICENSE']._serialized_start=3264
  _globals['_CMSGAMADDFREELICENSE']._serialized_end=3369
  _globals['_CMSGAMADDFREELICENSERESPONSE']._serialized_start=3371
  _globals['_CMSGAMADDFREELICENSERESPONSE']._serialized_end=3470
  _globals['_CGCMSGGETIPLOCATION']._serialized_start=3472
  _globals['_CGCMSGGETIPLOCATION']._serialized_end=3506
  _globals['_CIPLOCATIONINFO']._serialized_start=3508
  _globals['_CIPLOCATIONINFO']._serialized_end=3620
  _globals['_CGCMSGGETIPLOCATIONRESPONSE']._serialized_start=3622
  _globals['_CGCMSGGETIPLOCATIONRESPONSE']._serialized_end=3684
  _globals['_CGCMSGSYSTEMSTATSSCHEMA']._serialized_start=3686
  _globals['_CGCMSGSYSTEMSTATSSCHEMA']._serialized_end=3749
  _globals['_CGCMSGGETSYSTEMSTATS']._serialized_start=3751
  _globals['_CGCMSGGETSYSTEMSTATS']._serialized_end=3773
  _globals['_CGCMSGGETSYSTEMSTATSRESPONSE']._serialized_start=3776
  _globals['_CGCMSGGETSYSTEMSTATSRESPONSE']._serialized_end=4101
  _globals['_CMSGAMSENDEMAIL']._serialized_start=4104
  _globals['_CMSGAMSENDEMAIL']._serialized_end=4458
  _globals['_CMSGAMSENDEMAIL_REPLACEMENTTOKEN']._serialized_start=4331
  _globals['_CMSGAMSENDEMAIL_REPLACEMENTTOKEN']._serialized_end=4390
  _globals['_CMSGAMSENDEMAIL_PERSONANAMEREPLACEMENTTOKEN']._serialized_start=4392
  _globals['_CMSGAMSENDEMAIL_PERSONANAMEREPLACEMENTTOKEN']._serialized_end=4458
  _globals['_CMSGAMSENDEMAILRESPONSE']._serialized_start=4460
  _globals['_CMSGAMSENDEMAILRESPONSE']._serialized_end=4505
  _globals['_CMSGGCGETEMAILTEMPLATE']._serialized_start=4507
  _globals['_CMSGGCGETEMAILTEMPLATE']._serialized_end=4613
  _globals['_CMSGGCGETEMAILTEMPLATERESPONSE']._serialized_start=4615
  _globals['_CMSGGCGETEMAILTEMPLATERESPONSE']._serialized_end=4710
  _globals['_CMSGAMGRANTGUESTPASSES2']._serialized_start=4713
  _globals['_CMSGAMGRANTGUESTPASSES2']._serialized_end=4845
  _globals['_CMSGAMGRANTGUESTPASSES2RESPONSE']._serialized_start=4847
  _globals['_CMSGAMGRANTGUESTPASSES2RESPONSE']._serialized_end=4927
  _globals['_CGCSYSTEMMSG_GETACCOUNTDETAILS']._serialized_start=4929
  _globals['_CGCSYSTEMMSG_GETACCOUNTDETAILS']._serialized_end=5005
  _globals['_CGCSYSTEMMSG_GETACCOUNTDETAILS_RESPONSE']._serialized_start=5008
  _globals['_CGCSYSTEMMSG_GETACCOUNTDETAILS_RESPONSE']._serialized_end=5953
  _globals['_CMSGGCGETPERSONANAMES']._serialized_start=5955
  _globals['_CMSGGCGETPERSONANAMES']._serialized_end=5996
  _globals['_CMSGGCGETPERSONANAMES_RESPONSE']._serialized_start=5999
  _globals['_CMSGGCGETPERSONANAMES_RESPONSE']._serialized_end=6189
  _globals['_CMSGGCGETPERSONANAMES_RESPONSE_PERSONANAME']._serialized_start=6137
  _globals['_CMSGGCGETPERSONANAMES_RESPONSE_PERSONANAME']._serialized_end=6189
  _globals['_CMSGGCCHECKFRIENDSHIP']._serialized_start=6191
  _globals['_CMSGGCCHECKFRIENDSHIP']._serialized_end=6259
  _globals['_CMSGGCCHECKFRIENDSHIP_RESPONSE']._serialized_start=6261
  _globals['_CMSGGCCHECKFRIENDSHIP_RESPONSE']._serialized_end=6336
  _globals['_CMSGGCMSGMASTERSETDIRECTORY']._serialized_start=6339
  _globals['_CMSGGCMSGMASTERSETDIRECTORY']._serialized_end=6539
  _globals['_CMSGGCMSGMASTERSETDIRECTORY_SUBGC']._serialized_start=6445
  _globals['_CMSGGCMSGMASTERSETDIRECTORY_SUBGC']._serialized_end=6539
  _globals['_CMSGGCMSGMASTERSETDIRECTORY_RESPONSE']._serialized_start=6541
  _globals['_CMSGGCMSGMASTERSETDIRECTORY_RESPONSE']._serialized_end=6599
  _globals['_CMSGGCMSGWEBAPIJOBREQUESTFORWARDRESPONSE']._serialized_start=6601
  _globals['_CMSGGCMSGWEBAPIJOBREQUESTFORWARDRESPONSE']._serialized_end=6662
  _globals['_CGCSYSTEMMSG_GETPURCHASETRUST_REQUEST']._serialized_start=6664
  _globals['_CGCSYSTEMMSG_GETPURCHASETRUST_REQUEST']._serialized_end=6720
  _globals['_CGCSYSTEMMSG_GETPURCHASETRUST_RESPONSE']._serialized_start=6723
  _globals['_CGCSYSTEMMSG_GETPURCHASETRUST_RESPONSE']._serialized_end=6896
  _globals['_CMSGGCHACCOUNTVACSTATUSCHANGE']._serialized_start=6899
  _globals['_CMSGGCHACCOUNTVACSTATUSCHANGE']._serialized_end=7042
  _globals['_CMSGGCGETPARTNERACCOUNTLINK']._serialized_start=7044
  _globals['_CMSGGCGETPARTNERACCOUNTLINK']._serialized_end=7090
  _globals['_CMSGGCGETPARTNERACCOUNTLINK_RESPONSE']._serialized_start=7093
  _globals['_CMSGGCGETPARTNERACCOUNTLINK_RESPONSE']._serialized_end=7225
  _globals['_CMSGGCROUTINGINFO']._serialized_start=7228
  _globals['_CMSGGCROUTINGINFO']._serialized_end=7545
  _globals['_CMSGGCROUTINGINFO_ROUTINGMETHOD']._serialized_start=7433
  _globals['_CMSGGCROUTINGINFO_ROUTINGMETHOD']._serialized_end=7545
  _globals['_CMSGGCMSGMASTERSETWEBAPIROUTING']._serialized_start=7548
  _globals['_CMSGGCMSGMASTERSETWEBAPIROUTING']._serialized_end=7729
  _globals['_CMSGGCMSGMASTERSETWEBAPIROUTING_ENTRY']._serialized_start=7640
  _globals['_CMSGGCMSGMASTERSETWEBAPIROUTING_ENTRY']._serialized_end=7729
  _globals['_CMSGGCMSGMASTERSETCLIENTMSGROUTING']._serialized_start=7732
  _globals['_CMSGGCMSGMASTERSETCLIENTMSGROUTING']._serialized_end=7892
  _globals['_CMSGGCMSGMASTERSETCLIENTMSGROUTING_ENTRY']._serialized_start=7830
  _globals['_CMSGGCMSGMASTERSETCLIENTMSGROUTING_ENTRY']._serialized_end=7892
  _globals['_CMSGGCMSGMASTERSETWEBAPIROUTING_RESPONSE']._serialized_start=7894
  _globals['_CMSGGCMSGMASTERSETWEBAPIROUTING_RESPONSE']._serialized_end=7956
  _globals['_CMSGGCMSGMASTERSETCLIENTMSGROUTING_RESPONSE']._serialized_start=7958
  _globals['_CMSGGCMSGMASTERSETCLIENTMSGROUTING_RESPONSE']._serialized_end=8023
  _globals['_CMSGGCMSGSETOPTIONS']._serialized_start=8026
  _globals['_CMSGGCMSGSETOPTIONS']._serialized_end=8310
  _globals['_CMSGGCMSGSETOPTIONS_MESSAGERANGE']._serialized_start=8157
  _globals['_CMSGGCMSGSETOPTIONS_MESSAGERANGE']._serialized_end=8198
  _globals['_CMSGGCMSGSETOPTIONS_OPTION']._serialized_start=8200
  _globals['_CMSGGCMSGSETOPTIONS_OPTION']._serialized_end=8310
  _globals['_CMSGGCHUPDATESESSION']._serialized_start=8313
  _globals['_CMSGGCHUPDATESESSION']._serialized_end=8683
  _globals['_CMSGGCHUPDATESESSION_EXTRAFIELD']._serialized_start=8642
  _globals['_CMSGGCHUPDATESESSION_EXTRAFIELD']._serialized_end=8683
  _globals['_CMSGNOTIFICATIONOFSUSPICIOUSACTIVITY']._serialized_start=8686
  _globals['_CMSGNOTIFICATIONOFSUSPICIOUSACTIVITY']._serialized_end=8922
  _globals['_CMSGNOTIFICATIONOFSUSPICIOUSACTIVITY_MULTIPLEGAMEINSTANCES']._serialized_start=8847
  _globals['_CMSGNOTIFICATIONOFSUSPICIOUSACTIVITY_MULTIPLEGAMEINSTANCES']._serialized_end=8922
  _globals['_CMSGDPPARTNERMICROTXNS']._serialized_start=8925
  _globals['_CMSGDPPARTNERMICROTXNS']._serialized_end=9551
  _globals['_CMSGDPPARTNERMICROTXNS_PARTNERMICROTXN']._serialized_start=9101
  _globals['_CMSGDPPARTNERMICROTXNS_PARTNERMICROTXN']._serialized_end=9448
  _globals['_CMSGDPPARTNERMICROTXNS_PARTNERINFO']._serialized_start=9450
  _globals['_CMSGDPPARTNERMICROTXNS_PARTNERINFO']._serialized_end=9551
  _globals['_CMSGDPPARTNERMICROTXNSRESPONSE']._serialized_start=9554
  _globals['_CMSGDPPARTNERMICROTXNSRESPONSE']._serialized_end=9936
  _globals['_CMSGDPPARTNERMICROTXNSRESPONSE_EERRORCODE']._serialized_start=9685
  _globals['_CMSGDPPARTNERMICROTXNSRESPONSE_EERRORCODE']._serialized_end=9936
# @@protoc_insertion_point(module_scope)
