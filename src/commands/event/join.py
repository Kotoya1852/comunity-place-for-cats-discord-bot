"""
!joinコマンド
"""

import discord

import const


async def join_command(message: discord.Message, parameters: list[str]):
    """!joinコマンド処理"""
    # パラメータに指定されたイベントに参加します。
    try:
        event = parameters.pop(0)
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
