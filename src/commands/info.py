"""
!infoコマンド
"""

import discord

import const
from utils import UtilsService as utilsService


async def info_command(message: discord.Message, parameters: list[str]):
    """!infoコマンド処理"""
    # パラメータに指定されたイベントの情報を返信します。
    try:
        event = parameters.pop(0)
        if event == "minecraft":
            # バリデーションチェック
            # チャンネルIDチェック
            message_id = message.channel.id
            if message_id != const.minecraft_channel_id:
                # テキストチャンネルIDが一致しない
                await message.reply(
                    f"このテキストチャンネルでは回答できません。\n`{event}`用のテキストチャンネルでコマンドを実行してください。"
                )
                return
            # ロールmessage.author.get_チェック
            guild = message.guild
            member = guild.get_member(message.author.id)
            if member == None:
                # メンバーの情報を取得することに失敗した
                await message.reply(f"あなたの情報を取得することに失敗しました。管理者に連絡してください。")
                return
            role = member.get_role(const.minecraft_role_id)
            if role is None:
                # ロールが見つからない
                await message.reply(
                    f"あなたに情報を開示する権限がありません。\nイベント`{event}`に参加してください。`!join {event}`"
                )
                return

            # 情報を返信します。
            ip_addr = utilsService.get_global_ip_address_by_me()
            await message.reply(
                f"【アクセス情報】\nサーバーアドレス：{ip_addr}:25565\nDynmap：{ip_addr}:8123"
            )
            return
        else:
            # 存在しないイベント
            await message.reply(f"イベント`{event}`について開示できる情報がありません。")
    except IndexError:
        # イベントが指定されなかった
        await message.reply("取得したい情報のイベント名を指定してください。")
        return
