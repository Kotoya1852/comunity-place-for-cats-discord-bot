#!/bin/bash

###
# discordボットを最新バージョンにアップデートするスクリプト
###

# 当シェルスクリプトファイルの場所まで移動
cd dirname ${0}

# 環境変数ファイルのバックアップファイルを一時ファイルとして作成する
copy environment_values.txt /tmp/environment_values.txt

# リポジトリをリセットする
git checkout .
git clean

# リポジトリをプルする
git pull

# バックアップファイル（一時ファイル）からリストアする
move /tmp/environment_values.txt environment_values.txt

# 完了
echo Update completed!
