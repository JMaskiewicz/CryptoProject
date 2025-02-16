import logging
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
        """
        Starts CPU and GPU mining processes.
        """
        logger.info("Starting mining processes...")
        self.mining_logs.log_event("Starting CPU miner...")
        self.cpu_miner.start()

        self.mining_logs.log_event("Starting GPU miner...")
        self.gpu_miner.start()

        # Optionally, you can start the process_monitor in a separate thread.
        # For alpha version, we just call monitor() once or run it in the background.
        self.process_monitor.monitor()  # This might block if it's a while loop

    def stop_mining(self):
        """
        Stops CPU and GPU mining processes.
        """
        logger.info("Stopping mining processes...")
        self.mining_logs.log_event("Stopping CPU miner...")
        self.cpu_miner.stop()

        self.mining_logs.log_event("Stopping GPU miner...")
        self.gpu_miner.stop()

        logger.info("All mining processes have been stopped.")
