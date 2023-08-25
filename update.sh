#!/bin/bash

###
# discordボットを最新バージョンにアップデートするスクリプト
###

# 当シェルスクリプトファイルの場所まで移動
cd `dirname ${0}`

# 環境変数ファイルのバックアップファイルを一時ファイルとして作成する
cp set_environment.sh /tmp/set_environment.sh

# リポジトリをリセットする
git checkout .
git clean

# リポジトリをプルする
git pull

# バックアップファイル（一時ファイル）からリストアする
mv /tmp/set_environment.sh set_environment.sh

# 完了
echo Update completed!
