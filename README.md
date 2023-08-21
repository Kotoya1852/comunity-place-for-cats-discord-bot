# community-place-for-cats-discord-bot

![GitHub issues](https://img.shields.io/github/issues/Kotoya1852/community-place-for-cats-discord-bot?logo=github)


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
※初回導入の場合は別途準備が必要です。[初回導入]()を参照してください。
1. お好みの場所に移動する
```
cd <お好みのディレクトリ>
```
2. Githubからソースをクローンする
```
git clone https://github.com/Kotoya1852/community-place-for-cats-discord-bot.git -b main
```
3. 環境変数を設定する
```
export DISCORD_CLIENT_ID={DiscordボットのクライアントID}
export DISCORD_NOTIFICATION_CANNEL_ID={入退室通知用テキストチャンネルID}
export DISCORD_MINECRAFT_CHANNEL_ID={マインクラフト用テキストチャンネルID}
export DISCORD_MINECRAFT_ROLE_ID={マインクラフト参加用ロールID}
export DEBUG_LOG_OUTPUT_FLAG=true （※デバッグログを出力する場合のみ、しない場合は`false`を指定しても良い）
```
※`.bash_profile`に追加した際は`reboot`で再起動することをオススメします。
4. 以下コマンドを実行して、仮想環境を構築する
```
pipenv install
```
5. ソースのあるディレクトリに移動する
```
cd src
```
6. 以下コマンドを実行して、ボットを起動する
```
nohup python3.10 main.py &
```
