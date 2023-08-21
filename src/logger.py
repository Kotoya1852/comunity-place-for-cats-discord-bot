import datetime

from const import debug_log_output_flag


class LoggerService:
    """
    discordボット用ロガークラス
    """

    def info(message: str):
        """
        情報ログを出力します。
        これは、必ずログファイルに出力されます。

        Args:
            message: 出力メッセージ
        """
        print(f"{datetime.datetime.now()}:[info]:{message}")

    def debug(message: str):
        """
        デバッグログを出力します。
        環境変数の値で、ログファイルに出力するか決まります。

        Args:
            message: 出力メッセージ
        """
        if debug_log_output_flag == "true":
            # デバッグログ出力フラグがtrueの場合のみデバッグログを出力する
            print(f"{datetime.datetime.now()}:[debug]:{message}")
