"""
!versionコマンド
"""

import platform

import discord

import __init__ as this


async def version_command(message: discord.Message):
    """!versionコマンド処理"""
    # 現在使用中のソフトウェアバージョンを出力する
    commands = list(
        (
            f"猫ボット：v{this.__version__}",
            f"Python：v{platform.python_version()}",
            f"discord.py：v{discord.__version__}",
        )
    )
    commands_help = "\n".join(commands)
    await message.reply(f"versionコマンド実行\n{commands_help}")
    return
