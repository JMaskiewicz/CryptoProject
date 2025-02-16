from miner_controller.miner_manager import MinerManager
import keys.monero_keys as monero_keys

if __name__ == "__main__":
    config = {
        # Where XMRig is located on your PC
        "CPU_MINER_PATH": monero_keys.path,

        # The command-line arguments for XMRig
        "CPU_MINER_ARGS": [
            "-o", monero_keys.XMR_POOL,  # e.g. "pool.supportxmr.com:3333"
            "-u", monero_keys.XMR_WALLET,  # your wallet address
            "-p", monero_keys.XMR_PASS,  # typically "x"
        ],

        # For now, ignore GPU
        "GPU_MINER_PATH": None,
        "GPU_MINER_ARGS": []
    }

    manager = MinerManager(config)
    manager.start_mining()
