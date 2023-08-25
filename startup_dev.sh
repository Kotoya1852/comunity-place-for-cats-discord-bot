#!/bin/bash

#####
# discordボットを起動するスクリプト
#####

# 当シェルスクリプトファイルの場所まで移動
cd dirname ${0}

IMAGE_TAG="discord-bot:latest"

LATEST_IMAGE_ID=`docker images $IMAGE_TAG --format {{.ID}}`

if [ $LATEST_IMAGE_ID != "" ]; then
    # 既にイメージが存在する場合、削除する
    docker image rm $LATEST_IMAGE_ID
fi

# イメージビルドを行う
docker build . -t $IMAGE_TAG

# コンテナ実行を行う
docker run $IMAGE_TAG -d --env-file environemnt_values_dev.txt
