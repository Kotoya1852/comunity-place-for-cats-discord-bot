"""
!event helpコマンド
"""

import discord


async def help_command(message: discord.Message):
    """helpサブコマンド処理"""
    # 現在使用可能なイベントをメッセージに返信する。
    commands = list(
        (
            "`!event` ・・・ イベント管理を行います。サブコマンドを指定することが必須です。",
            "`!event join イベント名` ・・・ イベントに参加します",
            "`!event leave イベント名` ・・・ イベントから脱退します",
            "`!event info イベント名` ・・・ イベントの情報を出力します",
        )
    )
    commands_help = "\n".join(commands)
    await message.reply(f"helpコマンド実行：現在使用可能なコマンドは以下の通りです。\n{commands_help}")
    return
