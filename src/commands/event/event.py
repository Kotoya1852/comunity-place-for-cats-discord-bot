"""
イベントコマンドメイン関数
"""

import discord
import help
import info
import join
import leave


async def event_command(
    message: discord.Message,
    parameters: list[str],
) -> None:
    """!eventコマンド処理"""
    sub_command = parameters.pop(0)
    if sub_command == "join":
        # joinコマンド
        await join.join_command(message, parameters)
        return
    elif sub_command == "leave":
        # leaveコマンド
        await leave.leave_command(message, parameters)
        return
    elif sub_command == "info":
        # infoコマンド
        await info.info_command(message, parameters)
        return
    elif sub_command == "help":
        # helpコマンド
        await help.help_command(message)
        return
    else:
        # 存在しないコマンド
        # エラーメッセージをメッセージに返信する。
        await message.reply(
            f"サブコマンドリストに `{sub_command}` は存在しません。\n`!event help`を実行してコマンドを確認してください。"
        )
        return
