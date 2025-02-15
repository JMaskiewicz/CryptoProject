import logging
import os
import subprocess
import signal

logger = logging.getLogger(__name__)

class CPUMiner:
    """
    Manages the CPU mining process using XMRig or another CPU miner.
    """

    def __init__(self, config):
        """
        :param config: dict containing config items like:
            config["CPU_MINER_PATH"]: path to the XMRig executable
            config["CPU_MINER_ARGS"]: additional arguments for XMRig
        """
        self.config = config
        self.process = None

    def start(self):
        """
        Starts the CPU miner process.
        """
        miner_path = self.config.get("CPU_MINER_PATH", "xmrig")
        miner_args = self.config.get("CPU_MINER_ARGS", [])

        try:
            cmd = [miner_path] + miner_args
            self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logger.info(f"CPU miner started with PID: {self.process.pid}")
        except Exception as e:
            logger.error(f"Failed to start CPU miner: {e}")

    def stop(self):
        """
        Stops the CPU miner process.
        """
        if self.process and self.process.poll() is None:
            logger.info(f"Stopping CPU miner with PID: {self.process.pid}")
            self.process.send_signal(signal.SIGINT)
            self.process.wait(timeout=10)
            logger.info("CPU miner stopped.")
        else:
            logger.info("CPU miner is not running.")

    def is_running(self):
        """
        Checks if the CPU miner process is still running.
        :return: bool
        """
        return self.process and (self.process.poll() is None)
