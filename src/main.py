"""
    機能名：入退室通知ボット猫 - 猫の集会場
"""

import discord

import commands.commands as commands
import const
from logger import LoggerService as loggerService
from utils import UtilsService as utilsService

# クライアント
client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_voice_state_update(
    member: discord.Member, before: discord.VoiceState, after: discord.VoiceState
):
    """
    ボイスチャンネルに入退出したタイミングで発火するイベント処理

    Args:
        member: 入退出したユーザーの情報
        before: 退室元ボイスチャンネルの情報
        after: 入室先ボイスチャンネルの情報
    """
    if before.channel != after.channel:
        notice_id = int(const.notification_channel_id)
        # 通知チャンネルが存在するサーバーを取得する
        guild: discord.Guild = utilsService.get_guild_by_channel_id(client, notice_id)
        if guild == None:
            # 通知チャンネルが存在するサーバーが見つからない
            loggerService.info("サーバーが見つかりませんでした。")
            return

        # 通知先チャンネル指定
        botRoom = client.get_channel(notice_id)

        # サーバーに存在するチャンネルIDを自動取得（新しく作成してもソースを修正する必要がない）
        announceChannelIds = []
        for channel in client.get_all_channels():
            channel_id = guild.get_channel(channel.id).id
            if channel != None:
                announceChannelIds.append(channel_id)

        # チャンネルIDが入っていることを確認する
        loggerService.debug(f"対象チャンネルID: {announceChannelIds}")

        if before.channel is not None and before.channel.id in announceChannelIds:
            # 退出メッセージ送信
            await botRoom.send(
                utilsService.random_message_select(
                    const.leaving_msg_list, before, member
                )
            )

        if after.channel is not None and after.channel.id in announceChannelIds:
            # 入室メッセージ送信
            await botRoom.send(
                utilsService.random_message_select(const.entry_msg_list, after, member)
            )


@client.event
async def on_message(message: discord.Message):
    """
    コマンドを受け取り、コマンドに見合った処理を実行します。\n
    注意：このイベントはDMでもサーバーの全テキストチャットでも反応します。

    Args:
        message: 受信したメッセージ情報
    """
    loggerService.debug(f"{message.content}")
    if message.content.startswith("!"):
        # コマンド接頭辞は`!`なので、`!`のテキストメッセージを取得する
        # コマンドパラメータは半角スペースで区切る
        input_command_and_parameters = message.content.split(" ")
        main_command = input_command_and_parameters.pop(0)
        await commands.core_commands(
            message, main_command, input_command_and_parameters
        )


@client.event
async def on_ready():
    """
    ボットが起動した時に発火するイベントです。
    """
    # 初期値：通常稼働モード
    bot_str = "稼働中にゃ！"
    bot_status = discord.Status.online

    # 稼働モードを取得
    if const.client_run_mode == "maintenance":
        # メンテナンスモード
        bot_str = "メンテナンス中にゃ！"
        bot_status = discord.Status.dnd

    await client.change_presence(
        status=bot_status,
        activity=discord.Activity(
            name=bot_str,
            type=discord.ActivityType.custom,
            state=bot_str,
            details=bot_str,
        ),
    )

    # 起動した日時をログに残す。
    loggerService.info(f"起動しました。")
    loggerService.info(f"bot name : {client.user.name}")
    loggerService.info(f"bot id : {client.user.id}")
    loggerService.info(f"discord py version : {discord.__version__}")


@client.event
async def on_connect():
    """
    ボットがサーバーに接続した時に発火するイベントです。
    """
    bot_str = "起動中..."
    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            name=bot_str,
            type=discord.ActivityType.custom,
            state=bot_str,
            details=bot_str,
        ),
    )

    # 接続した日時をログに残す。
    loggerService.info(f"正常に接続しました。")


client.run(const.client_id)
