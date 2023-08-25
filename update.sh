#!/bin/bash

###
# discordボットを最新バージョンにアップデートするスクリプト
###

# 当シェルスクリプトファイルの場所まで移動
cd `dirname ${0}`

# 環境変数ファイルのバックアップファイルを一時ファイルとして作成する
cp set_environement.sh /tmp/set_environement.sh

# リポジトリをリセットする
git checkout .
git clean

# リポジトリをプルする
git pull

# バックアップファイル（一時ファイル）からリストアする
mv /tmp/set_environement.sh set_environement.sh

# 完了
echo Update completed!
