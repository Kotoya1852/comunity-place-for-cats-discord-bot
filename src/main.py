"""
    機能名：入退室通知ボット猫 - 猫の集会場
    作成者：Kotoya
    作成日：不明
    更新履歴：
        Version 1
        ----------
        v1.0 ; Kotoya ; 2021/08/31; 新規作成
        v1.1 ; Kotoya ; 更新日不明 ; 修正内容不明
        v1.2 ; Kotoya ; 2022/08/04; 新しくチャンネルを作成しても自動で通知対象になるように修正
        v1.3 ; Kotoya ; 2022/08/31; 一部ユーザーに対して通知内容が改変されるようになりました

        Version 2
        ----------
        v2.0 ; Kotoya ; 2023/07/23; 全ユーザーの通知メッセージがランダムで改変されるようになりました
                                    コマンド機能を追加（!ping）
                                    ボットステータスを追加（固定文字 `稼働中にゃ！`）
        v2.1 ; Kotoya ; 2023/07/30; 入室時に通知が来ないバグを修正
                                    コマンドを追加（!help）
        v2.2 ; Kotoya ; 2023/08/11; ボットステータスのプレゼンス情報をカスタムアクティビティクラスに修正しました。（これ以降、`プレイ中`が削除される）
                                    イベント参加・辞退コマンドを追加（!join / !leave）
                                    イベント情報取得コマンドを追加（!info）
        chore; Kotoya ; 2023/08/??; 環境に関するリテラル値を環境変数から取得するよう修正
                                    Githubで公開し、publicにソースが閲覧できるよう整備
                                        → これ以降の更新履歴をGithubで管理する。
"""

import discord
import datetime

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
        # 通知先チャンネル指定
        botRoom = client.get_channel(const.notification_channel_id)

        # チャンネルIDを自動取得（新しく作成してもソースを修正する必要がない）
        announceChannelIds = []
        for channel in client.get_all_channels():
            announceChannelIds.append(channel.id)

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
    loggerService.debug(f"{datetime.datetime.now()}:{message.content}")
    if message.content.startswith("!"):
        # コマンド接頭辞は`!`なので、`!`のテキストメッセージを取得する
        # コマンドパラメータは半角スペースで区切る
        input_command_and_parameters = message.content.split(" ")
        input_command = input_command_and_parameters.pop(0)
        if input_command == "!ping":
            # pingコマンド
            # レイテンシーをメッセージに返信する。
            await message.reply(f"pingコマンド実行：ボット猫のPingは約{round(client.latency, 2)}秒です。")
            return
        elif input_command == "!help":
            # helpコマンド
            # 現在使用可能なコマンドをメッセージに返信する。
            commands = list(
                ("`!ping`", "`!join イベント名`", "`!leave イベント名`", "`!info イベント名`")
            )
            commands_help = "\n".join(commands)
            await message.reply(f"helpコマンド実行：現在使用可能なコマンドは以下の通りです。\n{commands_help}")
            return
        elif input_command == "!join":
            # joinコマンド
            # パラメータに指定されたイベントに参加します。
            try:
                event = input_command_and_parameters.pop(0)
                if event == "minecraft":
                    # サーバー情報取得
                    guild = message.guild
                    # ロール情報取得
                    role = discord.utils.get(guild.roles, id=const.minecraft_role_id)
                    # 特定のロールが付与されているか
                    if message.author.get_role(role.id) is not None:
                        await message.reply(f"既に参加済です。")
                        return
                    # 特定のロールを付与する
                    await message.author.add_roles(role)
                    # 結果を返却する
                    await message.reply(f"イベント`{event}`の参加を受諾しました。")
                    return
                else:
                    # 存在しないイベント
                    await message.reply(f"イベント`{event}`は存在しません。")
            except IndexError:
                # イベントが指定されなかった
                # イベントリストを表示
                events = ["minecraft"]
                event_help = "\n".join(events)
                await message.reply(f"現在参加できるイベントは以下の通りです。\n{event_help}")
                return
        elif input_command == "!leave":
            # leaveコマンド
            # パラメータに指定されたイベントを辞退します。
            try:
                event = input_command_and_parameters.pop(0)
                if event == "minecraft":
                    # サーバー情報取得
                    guild = message.guild
                    # ロール情報取得
                    role = discord.utils.get(guild.roles, id=const.minecraft_role_id)
                    # 特定のロールが付与されているか
                    if message.author.get_role(role.id) is None:
                        await message.reply(f"イベント`{event}`は参加していません。")
                        return
                    # 特定のロールを除去する
                    await message.author.remove_roles(role)
                    # 結果を返却する
                    await message.reply(f"イベント`{event}`の参加を辞退しました。")
                    return
                else:
                    await message.reply(f"イベント`{event}`は参加していません。")
                    return
            except IndexError:
                # イベントが指定されなかった
                await message.reply("辞退するイベントを指定してください。")
                return
        elif input_command == "!info":
            # infoコマンド
            # パラメータに指定されたイベントの情報を返信します。
            try:
                event = input_command_and_parameters.pop(0)
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
        else:
            # 存在しないコマンド
            # エラーメッセージをメッセージに返信する。
            await message.reply(
                f"コマンドリストに `{input_command}` は存在しません。\n`!help`を実行してコマンドを確認してください。"
            )
            return


@client.event
async def on_ready():
    """
    ボットが起動した時に発火するイベントです。
    """
    bot_str = "稼働中にゃ！"
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            name=bot_str,
            type=discord.ActivityType.custom,
            state=bot_str,
            details=bot_str,
        ),
    )

    # 起動した日時をログに残す。
    loggerService.info(f"{datetime.datetime.now()} : 起動しました。")
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
    loggerService.info(f"{datetime.datetime.now()} : 正常に接続しました。")


client.run(const.client_id)
