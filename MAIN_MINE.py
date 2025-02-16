from miner_controller.miner_manager import MinerManager
import keys.monero_keys as monero_keys

if __name__ == "__main__":
    config = {
        "CPU_ENABLED": True,
        "CPU_MINER_PATH": monero_keys.path,
        "CPU_MINER_ARGS": [
            "-o", monero_keys.XMR_POOL,
            "-u", monero_keys.XMR_WALLET,
            "-p", monero_keys.XMR_PASSWORD
        ],

        "GPU_ENABLED": False,
        "GPU_MINER_PATH": None,
        "GPU_MINER_ARGS": []
    }

    manager = MinerManager(config)
    manager.start_mining()
