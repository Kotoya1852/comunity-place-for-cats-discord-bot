"""
定数値、環境変数管理
"""

import os

############
# 定数値    #
############

# 置換定数
channel_name: str = "$channel_name$"
""" チャンネル名置き換え文字列 """
display_name: str = "$display_name$"
""" 表示名置き換え文字列 """


# メッセージリスト
entry_msg_list = list(
    (
        f"**{channel_name}** に、__{display_name}__  が入室しました！",
        f"**{channel_name}** に、__{display_name}__  が入ってきた！にゃおん！",
        f"あ、**{channel_name}** に、__{display_name}__  がきました！",
    )
)
""" 入室メッセージリスト """


leaving_msg_list = list(
    (
        f"**{channel_name}** から、__{display_name}__  が退出しました！",
        f"**{channel_name}** から、__{display_name}__  が出ていった！にゃおん！",
        f"わーお！**{channel_name}** から、__{display_name}__  がいなくなった！",
    )
)
""" 退室メッセージリスト """


############
# 環境変数  #
############

# discordボットクライアントID
client_id = os.getenv("DISCORD_CLIENT_ID")
""" discordボットクライアントID """


# テキストチャンネルID
notification_channel_id = os.getenv("DISCORD_NOTIFICATION_CANNEL_ID")
""" 入退室通知チャンネルID """
minecraft_channel_id = os.getenv("DISCORD_MINECRAFT_CHANNEL_ID")
""" マインクラフト用チャンネルID """


# ロールID
minecraft_role_id = os.getenv("DISCORD_MINECRAFT_ROLE_ID")
""" マインクラフト参加ロールID """


# デバッグログ出力値
debug_log_output_flag = os.getenv("DEBUG_LOG_OUTPUT_FLAG")
""" デバッグログ出力フラグ """
