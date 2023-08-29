FROM python:3.10.12-slim-buster

# 環境変数取得
ARG DISCORD_CLIENT_ID
ARG DISCORD_CLIENT_RUN_MODE
ARG DISCORD_NOTIFICATION_CANNEL_ID
ARG DISCORD_MINECRAFT_CHANNEL_ID
ARG DISCORD_MINECRAFT_ROLE_ID
ARG DEBUG_LOG_OUTPUT_FLAG

# pipenv インストール
RUN python3 -m pip install --no-cache-dir --disable-pip-version-check pipenv

# 環境変数設定
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PIPENV_VENV_IN_PROJECT=1 \
    TZ=Asia/Tokyo \
    DISCORD_CLIENT_ID=$DISCORD_CLIENT_ID \
    DISCORD_CLIENT_RUN_MODE=$DISCORD_CLIENT_RUN_MODE \
    DISCORD_NOTIFICATION_CANNEL_ID=$DISCORD_NOTIFICATION_CANNEL_ID \
    DISCORD_MINECRAFT_CHANNEL_ID=$DISCORD_MINECRAFT_CHANNEL_ID \
    DISCORD_MINECRAFT_ROLE_ID=$DISCORD_MINECRAFT_ROLE_ID \
    DEBUG_LOG_OUTPUT_FLAG=$DEBUG_LOG_OUTPUT_FLAG

# 変数指定
ARG project_name="community-place-for-cats-discord-bot"
ARG application_name="src"

# 作業ディレクトリ作成
RUN mkdir -p /code/$project_name/$application_name

WORKDIR /code/$project_name
COPY ./Pipfile /code/$project_name
WORKDIR /code/$project_name/$application_name
COPY ./$application_name /code/$project_name/$application_name

WORKDIR /code/$project_name

# 仮想環境インストール
RUN pipenv install

WORKDIR /code/$project_name/$application_name

# ボット起動
ENTRYPOINT ["pipenv", "run", "python3", "-u", "main.py"]
