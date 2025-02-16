import logging
import datetime
import os

logger = logging.getLogger(__name__)

class TradeLogs:
    """
    Logs all trade operations.
    """

    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log_trade(self, trade_data):
        """
        Writes trade details to a log file.
        :param trade_data: dict with trade info
        """
        filename = os.path.join(self.log_dir, "trade_history.log")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log to console as well
        logger.info(f"Trade executed: {trade_data}")

        log_entry = f"{timestamp} - {trade_data}\n"
        with open(filename, "a") as f:
            f.write(log_entry)
