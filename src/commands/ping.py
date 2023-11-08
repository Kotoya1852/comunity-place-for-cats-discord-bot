"""
!ping コマンド
"""

import discord


async def ping_command(
    message: discord.Message,
    client: discord.Client,
):
    """!pingコマンド処理"""
    # レイテンシーをメッセージに返信する。
    await message.reply(f"pingコマンド実行：ボット猫のPingは約{round(client.latency, 2)}秒です。")
    return
