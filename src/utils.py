import random

import discord
import requests

from const import channel_name, display_name
from logger import LoggerService as loggerService


class UtilsService:
    """
    discordボットを動かす際に仕様する共通部品クラス
    """

    def random_message_select(
        msg_list,
        channel_info: discord.VoiceState,
        member: discord.Member,
    ) -> str:
        """
        通知メッセージをランダムで生成します。

        Args:
            msg_list: メッセージ候補リスト
            channel_info: チャンネル情報
            member: ユーザー情報
        """
        # 通知メッセージテンプレートをランダムで選択
        msg_len = len(msg_list)
        ran_int = random.randint(0, msg_len - 1)

        # 通知メッセージテンプレートに引数を設定して返却
        message = (
            msg_list[ran_int]
            .replace(channel_name, channel_info.channel.name)
            .replace(display_name, member.display_name)
        )
        loggerService.debug(message)
        return message

    def get_global_ip_address_by_me():
        """
        このサーバーのIPアドレスを取得します。
        """
        res = requests.get("https://checkip.amazonaws.com/")
        return res.text

    def get_guild_by_channel_id(
        client: discord.Client, channel_id: int
    ) -> discord.Guild | None:
        """
        チャンネルIDからギルドを取得します。

        Args:
            client: discordクライアント
            channel_id: チャンネルID（テキストチャンネルやボイスチャンネルのID）
        """
        target_channel = None
        for channel in client.get_all_channels():
            loggerService.debug(
                f"{channel.id} == {channel_id}: {channel.id == channel_id}"
            )
            if channel.id == channel_id:
                target_channel = channel
                loggerService.debug(f"検索対象チャンネル：{channel}")
                loggerService.debug(f"target_channel：{target_channel}")

        if target_channel == None:
            loggerService.debug("チャンネルが見つかりませんでした。")
            return None

        loggerService.debug(f"対象チャンネルのギルド：{target_channel.guild}")
        return target_channel.guild
