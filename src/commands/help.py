"""
!helpコマンド
"""

import discord


async def help_command(message: discord.Message):
    """!helpコマンド処理"""
    # 現在使用可能なコマンドをメッセージに返信する。
    commands = list(("`!ping`", "`!join イベント名`", "`!leave イベント名`", "`!info イベント名`"))
    commands_help = "\n".join(commands)
    await message.reply(f"helpコマンド実行：現在使用可能なコマンドは以下の通りです。\n{commands_help}")
    return
