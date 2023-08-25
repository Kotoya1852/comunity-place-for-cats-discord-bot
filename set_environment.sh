#!/bin/bash

#####
# 環境変数設定スクリプト
#####

# discord environments valiables
export DISCORD_CLIENT_ID=クライアントID
export DISCORD_NOTIFICATION_CANNEL_ID=入退室通知用チャンネルID
export DISCORD_MINECRAFT_CHANNEL_ID=マインクラフト通知用チャンネルID
export DISCORD_MINECRAFT_ROLE_ID=マインクラフトロールID
export DEBUG_LOG_OUTPUT_FLAG=false
export DISCORD_CLIENT_RUN_MODE=normal_run

printenv DISCORD_CLIENT_ID
printenv DISCORD_NOTIFICATION_CANNEL_ID
printenv DISCORD_MINECRAFT_CHANNEL_ID
printenv DISCORD_MINECRAFT_ROLE_ID
printenv DEBUG_LOG_OUTPUT_FLAG
printenv DISCORD_CLIENT_RUN_MODE
