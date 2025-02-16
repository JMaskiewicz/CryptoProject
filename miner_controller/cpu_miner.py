import threading
import logging
import subprocess
import signal
import time

logger = logging.getLogger(__name__)

class CPUMiner:
    def __init__(self, config):
        self.config = config
        self.process = None
        self.reader_thread = None
        self.running = False

    def start(self):
        miner_path = self.config.get("CPU_MINER_PATH", "xmrig")
        miner_args = self.config.get("CPU_MINER_ARGS", [])
        cmd = [miner_path] + miner_args

        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            self.running = True
            logger.info(f"CPU miner started with PID: {self.process.pid}")

            self.reader_thread = threading.Thread(
                target=self._read_miner_output,
                daemon=True
            )
            self.reader_thread.start()

        except Exception as e:
            logger.error(f"Failed to start CPU miner: {e}")

    def is_running(self):
        """Check if the miner process is running."""
        return self.running and self.process and (self.process.poll() is None)

    def _read_miner_output(self):
        accepted_count = 0
        last_print_time = time.time()

        while self.running and self.process.poll() is None:
            line = self.process.stdout.readline()
            if not line:
                break
            if "accepted" in line:
                accepted_count += 1
            if time.time() - last_print_time > 60:
                logger.info(f"[XMRig Stats] Accepted shares so far: {accepted_count}")
                last_print_time = time.time()

            logger.info(f"[XMRig] {line.strip()}")

    def stop(self):
        if self.process and self.process.poll() is None:
            logger.info(f"Stopping CPU miner with PID: {self.process.pid}")
            self.running = False
            self.process.send_signal(signal.SIGINT)
            self.process.wait(timeout=10)
            logger.info("CPU miner stopped.")
        else:
            logger.info("CPU miner is not running.")
