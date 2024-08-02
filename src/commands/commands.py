"""
コマンド関連メイン関数
"""

import discord
import event.event as event
import help
import ping


async def core_commands(
    message: discord.Message,
    client: discord.Client,
    command: str,
    parameters: list[str],
) -> None:
    """
    コマンドコア関数

    Args:
        message: 受信したメッセージ
        client: ボット猫のクライアント
        command: メインコマンド（先頭に`!`が付与されている）
        parameters: コマンドに付与されたパラメータ
    """
    if command == "!ping":
        # pingコマンド
        await ping.ping_command(message, client)
        return
    elif command == "!help":
        # helpコマンド
        await help.help_command(message)
        return
    elif command == "!event":
        # joinコマンド
        await event.event_command(message, parameters)
        return
    else:
        # 存在しないコマンド
        # エラーメッセージをメッセージに返信する。
        await message.reply(
            f"コマンドリストに `{command}` は存在しません。\n`!help`を実行してコマンドを確認してください。"
        )
        return
