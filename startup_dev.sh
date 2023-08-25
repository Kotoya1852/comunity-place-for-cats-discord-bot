#!/bin/bash

#####
# discordボットを起動するスクリプト
#####

# 環境変数設定
source set_environment.sh

# 当シェルスクリプトファイルの場所まで移動
NOW_DIR=`dirname ${0}`
cd $NOW_DIR

IMAGE_TAG="discord-bot:latest"

# 対象のdockerコンテナを全て停止、削除
CONTAINER_ID=`docker ps -f ancestor=$IMAGE_TAG -a --format {{.ID}}`
echo containerId: $CONTAINER_ID

if [ -n "$CONTAINER_ID" ]; then
    # 既にコンテナが存在する場合、停止してから削除する
    docker stop $CONTAINER_ID
    docker rm $CONTAINER_ID
fi

# 対象のdockerイメージを全て削除
LATEST_IMAGE_ID=`docker images $IMAGE_TAG --format {{.ID}}`
echo dockerId: $LATEST_IMAGE_ID

if [ -n "$LATEST_IMAGE_ID" ]; then
    # 既にイメージが存在する場合、削除する
    docker image rm $LATEST_IMAGE_ID
fi

# 環境変数をコンテナに渡す
DISCORD_CLIENT_ID=`printenv DISCORD_CLIENT_ID`
DISCORD_CLIENT_RUN_MODE=`printenv DISCORD_CLIENT_RUN_MODE`
DISCORD_NOTIFICATION_CANNEL_ID=`printenv DISCORD_NOTIFICATION_CANNEL_ID`
DISCORD_MINECRAFT_CHANNEL_ID=`printenv DISCORD_MINECRAFT_CHANNEL_ID`
DISCORD_MINECRAFT_ROLE_ID=`printenv DISCORD_MINECRAFT_ROLE_ID`
DEBUG_LOG_OUTPUT_FLAG=`printenv DEBUG_LOG_OUTPUT_FLAG`

ENV_OPTION_BUILD=" "
if [ -n "$DISCORD_CLIENT_ID" ]; then
    # クライアントID
    ENV_OPTION_BUILD+=" --build-arg DISCORD_CLIENT_ID="
    ENV_OPTION_BUILD+=$DISCORD_CLIENT_ID
    ENV_OPTION_BUILD+=" "
fi

if [ -n "$DISCORD_CLIENT_RUN_MODE" ]; then
    # クライアント稼働モード
    ENV_OPTION_BUILD+=" --build-arg DISCORD_CLIENT_RUN_MODE="
    ENV_OPTION_BUILD+=$DISCORD_CLIENT_RUN_MODE
    ENV_OPTION_BUILD+=" "
fi

if [ -n "$DISCORD_NOTIFICATION_CANNEL_ID" ]; then
    # 入退室通知チャンネルID
    ENV_OPTION_BUILD+=" --build-arg DISCORD_NOTIFICATION_CANNEL_ID="
    ENV_OPTION_BUILD+=$DISCORD_NOTIFICATION_CANNEL_ID
    ENV_OPTION_BUILD+=" "
fi

if [ -n "$DISCORD_MINECRAFT_CHANNEL_ID" ]; then
    # マインクラフト用チャンネルID
    ENV_OPTION_BUILD+=" --build-arg DISCORD_MINECRAFT_CHANNEL_ID="
    ENV_OPTION_BUILD+=$DISCORD_MINECRAFT_CHANNEL_ID
    ENV_OPTION_BUILD+=" "
fi

if [ -n "$DISCORD_MINECRAFT_ROLE_ID" ]; then
    # マインクラフト参加ロールID
    ENV_OPTION_BUILD+=" --build-arg DISCORD_MINECRAFT_ROLE_ID="
    ENV_OPTION_BUILD+=$DISCORD_MINECRAFT_ROLE_ID
    ENV_OPTION_BUILD+=" "
fi

if [ -n "$DEBUG_LOG_OUTPUT_FLAG" ]; then
    # デバッグログ出力フラグ
    ENV_OPTION_BUILD+=" --build-arg DEBUG_LOG_OUTPUT_FLAG="
    ENV_OPTION_BUILD+=$DEBUG_LOG_OUTPUT_FLAG
    ENV_OPTION_BUILD+=" "
fi

# イメージビルドを行う
echo docker build --progress=plain --no-cache=true -t $IMAGE_TAG . $ENV_OPTION_BUILD
docker build --progress=plain --no-cache=true -t $IMAGE_TAG . $ENV_OPTION_BUILD

# コンテナ実行を行う
docker run -d $IMAGE_TAG
