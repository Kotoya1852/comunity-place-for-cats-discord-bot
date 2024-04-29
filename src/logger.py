import datetime

from term_printer import Color, cprint

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
        cprint(f"{datetime.datetime.now()}:[info]:{message}")

    def debug(message: str):
        """
        デバッグログを出力します。
        環境変数の値で、ログファイルに出力するか決まります。

        Args:
            message: 出力メッセージ
        """
        if debug_log_output_flag == "true":
            # デバッグログ出力フラグがtrueの場合のみデバッグログを出力する
            cprint(f"{datetime.datetime.now()}:[debug]:{message}")

    def error(message: str):
        """
        エラーログを出力します。
        コンソール上、赤文字で出力される文字列を想定します。

        Args:
            message: 出力メッセージ
        """
        cprint(f"{datetime.datetime.now()}:[error]:{message}", attrs=[Color.RED])
