import logging
import subprocess
import signal

logger = logging.getLogger(__name__)

class GPUMiner:
    """
    Manages the GPU mining process using NBMiner or another GPU miner.
    """

    def __init__(self, config):
        """
        :param config: dict containing config items like:
            config["GPU_MINER_PATH"]: path to NBMiner executable
            config["GPU_MINER_ARGS"]: additional arguments for NBMiner
        """
        self.config = config
        self.process = None

    def start(self):
        """
        Starts the GPU miner process.
        """
        miner_path = self.config.get("GPU_MINER_PATH", "nbminer")
        miner_args = self.config.get("GPU_MINER_ARGS", [])

        try:
            cmd = [miner_path] + miner_args
            self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logger.info(f"GPU miner started with PID: {self.process.pid}")
        except Exception as e:
            logger.error(f"Failed to start GPU miner: {e}")

    def stop(self):
        """
        Stops the GPU miner process.
        """
        if self.process and self.process.poll() is None:
            logger.info(f"Stopping GPU miner with PID: {self.process.pid}")
            self.process.send_signal(signal.SIGINT)
            self.process.wait(timeout=10)
            logger.info("GPU miner stopped.")
        else:
            logger.info("GPU miner is not running.")

    def is_running(self):
        """
        Checks if the GPU miner process is still running.
        :return: bool
        """
        return self.process and (self.process.poll() is None)
