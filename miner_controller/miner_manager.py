import logging
import time
from miner_controller.cpu_miner import CPUMiner
from miner_controller.gpu_miner import GPUMiner
from miner_controller.process_monitor import ProcessMonitor
from miner_controller.mining_logs import MiningLogs

logger = logging.getLogger(__name__)


class MinerManager:
    """
    Coordinates the start/stop of mining processes for CPU and GPU.
    """

    def __init__(self, config):
        """
        :param config: dict containing configuration and paths for mining
        """
        self.config = config
        self.cpu_miner = CPUMiner(config)
        self.gpu_miner = GPUMiner(config)
        self.mining_logs = MiningLogs()
        self.process_monitor = ProcessMonitor(self.cpu_miner, self.gpu_miner)

    def start_mining(self):
        logger.info("Starting mining processes...")

        if self.config.get("CPU_ENABLED", True):
            self.mining_logs.log_event("Starting CPU miner...")
            self.cpu_miner.start()

        if self.config.get("GPU_ENABLED", False):
            self.mining_logs.log_event("Starting GPU miner...")
            self.gpu_miner.start()

        self.process_monitor.monitor()

    def stop_mining(self):
        logger.info("Stopping mining processes...")

        if self.config.get("CPU_ENABLED", True):
            self.mining_logs.log_event("Stopping CPU miner...")
            self.cpu_miner.stop()

        if self.config.get("GPU_ENABLED", False):
            self.mining_logs.log_event("Stopping GPU miner...")
            self.gpu_miner.stop()

        logger.info("All mining processes have been stopped.")