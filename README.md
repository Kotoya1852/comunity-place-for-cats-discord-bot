# community-place-for-cats-discord-bot

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/downloads/release/python-3100/)
[![GitHub](https://img.shields.io/github/license/Kotoya1852/community-place-for-cats-discord-bot)](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Kotoya1852/community-place-for-cats-discord-bot?logo=github)](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/issues?q=is%3Aissue+is%3Aopen+)
[![GitHub release (with filter)](https://img.shields.io/github/v/release/Kotoya1852/community-place-for-cats-discord-bot)](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/releases/latest)
[![Static Badge](https://img.shields.io/badge/Visual_Stadio_Code-download-blue?logo=visual-studio-code)](https://azure.microsoft.com/ja-jp/products/visual-studio-code)

> **Warning**<br>
> This document is only available in Japanese.

## 概要
猫の集会場オーナーボット猫のソースコード
[discord.py](https://discordpy.readthedocs.io/ja/latest/) を使用したボット。

## 機能一覧
- 特定サーバーの全ボイスチャンネルの入退室通知
- 先頭に`!`が付いたメッセージをコマンドとして扱った処理の実行
  - ボットのPing値測定結果出力
  - ボットが許容するコマンド一覧出力
  - イベントの参加・辞退
  - イベント情報を出力

## 導入方法
※既に[初回導入](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/wiki/%E5%88%9D%E6%9C%9F%E5%B0%8E%E5%85%A5)を実施済であることが条件です。
1. お好みの場所に移動する
```
cd <お好みのディレクトリ>
```
2. Githubからソースをクローンする
```
git clone https://github.com/Kotoya1852/community-place-for-cats-discord-bot.git -b main
```
3. リポジトリ内に移動する
```
cd community-place-for-cats-discord-bot
```
4. 環境変数を設定するため、environment_values.txtを修正する
```
vi environment_values.txt
```
```
DISCORD_CLIENT_ID=DiscordボットのクライアントID
DISCORD_NOTIFICATION_CANNEL_ID=入退室通知用テキストチャンネルID
DISCORD_MINECRAFT_CHANNEL_ID=マインクラフト用テキストチャンネルID
DISCORD_MINECRAFT_ROLE_ID=マインクラフト参加用ロールID
DEBUG_LOG_OUTPUT_FLAG=true （※デバッグログを出力する場合のみ、しない場合は`false`を指定しても良い）
```
5. ボットを動かす
```
bash startup.sh
```

## ボットのアップデート方法
※既に導入済であることが前提
1. アップデートスクリプトを実行
```
bash update.sh
```
2. ボットを動かす
```
bash startup.sh
```
