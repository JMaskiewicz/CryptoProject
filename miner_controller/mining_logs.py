import logging
import datetime
import os

logger = logging.getLogger(__name__)

class MiningLogs:
    """
    Handles logging for the mining processes.
    In a real setup, might write to a DB or external logging service.
    """

    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log_event(self, message):
        """
        Writes a mining event to a log file with timestamps.
        """
        filename = os.path.join(self.log_dir, "mining_events.log")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} - {message}\n"

        # Also log to Python logger
        logger.info(message)

        with open(filename, "a") as f:
            f.write(entry)
