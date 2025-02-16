import logging
import time

logger = logging.getLogger(__name__)

class ProcessMonitor:
    """
    Monitors the CPU and GPU miner processes and restarts them if they crash.
    """

    def __init__(self, cpu_miner, gpu_miner, check_interval=30):
        """
        :param cpu_miner: CPUMiner instance
        :param gpu_miner: GPUMiner instance
        :param check_interval: how often to check if processes are alive (seconds)
        """
        self.cpu_miner = cpu_miner
        self.gpu_miner = gpu_miner
        self.check_interval = check_interval
        self._running = True

    def monitor(self):
        logger.info("ProcessMonitor started.")
        while self._running:
            # Check CPU only if CPU_ENABLED
            if self.cpu_miner and self.config.get("CPU_ENABLED", True):
                if not self.cpu_miner.is_running():
                    logger.warning("CPU miner not running! Restarting...")
                    self.cpu_miner.start()

            # Check GPU only if GPU_ENABLED
            if self.gpu_miner and self.config.get("GPU_ENABLED", False):
                if not self.gpu_miner.is_running():
                    logger.warning("GPU miner not running! Restarting...")
                    self.gpu_miner.start()

            time.sleep(self.check_interval)

    def stop_monitoring(self):
        """
        Stops the monitoring loop.
        """
        self._running = False
        logger.info("ProcessMonitor stopped.")
