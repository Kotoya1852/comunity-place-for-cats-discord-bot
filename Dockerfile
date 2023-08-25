FROM python:3.10.12-alpine3.18

# 仮想環境インストール
RUN pipenv install

# 仮想環境シェル起動
RUN pipenv shell

# ディレクトリ移動
RUN cd /src

# ボット起動
RUN python main.py
