import logging


logging.basicConfig(
    filename="logs/recovery.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


class RecoveryLogger:

    @staticmethod
    def log_failure(message):
        logging.error(message)

    @staticmethod
    def log_recovery(message):
        logging.info(message)