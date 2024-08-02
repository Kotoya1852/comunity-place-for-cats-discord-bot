"""
!leaveコマンド
"""

import discord

import const


async def leave_command(message: discord.Message, parameters: list[str]):
    """!leaveコマンド処理"""
    # パラメータに指定されたイベントを辞退します。
    try:
        event = parameters.pop(0)
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
