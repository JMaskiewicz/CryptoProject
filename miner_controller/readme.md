# Miner Controller

## Overview
The `miner_controller` package manages the lifecycle of the mining processes (CPU and GPU). It starts, stops, monitors, and logs these mining processes.

## Components

1. **miner_manager.py**  
   - Coordinates when to start or stop mining.  
   - Interacts with `cpu_miner.py` and `gpu_miner.py`.

2. **cpu_miner.py**  
   - Manages CPU mining via XMRig (or another CPU miner).  
   - Contains functions to launch, monitor, and stop the CPU miner process.

3. **gpu_miner.py**  
   - Manages GPU mining via NBMiner (or another GPU miner).  
   - Contains functions to launch, monitor, and stop the GPU miner process.

4. **process_monitor.py**  
   - Continuously checks if the mining processes are still running.  
   - Automatically restarts them if they crash or exit unexpectedly.

5. **mining_logs.py**  
   - Handles logging of mining-related events and stats.  
   - In a real-world scenario, it might connect to a database or logging system (e.g., ELK Stack, Datadog).

## How to Use
1. **Install Dependencies**  
   - Ensure you have Python 3.9+ installed.  
   - `pip install -r requirements.txt` (if using a shared project requirements file).

2. **Set Configuration**  
   - Edit your `config/` files or `.env` with paths to your miner executables and any additional mining arguments.  
   - For CPU mining (XMRig), provide path/arguments.  
   - For GPU mining (NBMiner), provide path/arguments.

3. **Run the Miner**  
   - Typically orchestrated by a higher-level script (e.g. `run.py`) or via `miner_manager.start_mining()`.
   - Mining should start automatically.  
   - Monitor logs or console output to confirm it’s running.

4. **Stop the Miner**  
   - Call `miner_manager.stop_mining()` or kill the process externally.

5. **Monitoring**  
   - The `process_monitor` can be invoked to automatically detect if a miner crashed and restart.

---

## **CPU Miner**: XMRig Quick Setup
- Download the XMRig binary suitable for your OS.
- Provide the path to the binary and any arguments (pool URL, wallet address, etc.) in your `.env` or config.

## **GPU Miner**: NBMiner Quick Setup
- Download NBMiner and adjust your config to include the path to the binary.
- Configure your pool, wallet, and any overclock/power settings in the `.env` or dedicated config file.

---

## **Example Commands**
- `python run.py` (if your main script controls everything including start_mining).
- Logs are stored via `mining_logs.py`, so check the `logs/` directory if you configured it to write there.

---

## **Important Notes**
- This alpha version is not optimized for large-scale mining.
- For stable operation, you’d want a process manager like `supervisor`, `systemd`, or Docker containers.
- **Security**: Always keep your wallet credentials and private keys safe. Do **not** commit them to version control.
