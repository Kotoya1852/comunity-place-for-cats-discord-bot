"""
!helpコマンド
"""

import discord


async def help_command(message: discord.Message):
    """!helpコマンド処理"""
    # 現在使用可能なコマンドをメッセージに返信する。
    commands = list(
        (
            "`!ping` ・・・ ボットのPingを計測します",
            "`!event` ・・・ イベント管理を行います",
        )
    )
    commands_help = "\n".join(commands)
    await message.reply(f"helpコマンド実行：現在使用可能なコマンドは以下の通りです。\n{commands_help}")
    return
