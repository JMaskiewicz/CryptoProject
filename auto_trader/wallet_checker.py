import logging
import time
from .trade_executor import TradeExecutor

logger = logging.getLogger(__name__)

class WalletChecker:
    """
    Monitors a wallet for new mining rewards and triggers trades.
    """

    def __init__(self, config):
        """
        :param config: dict containing wallet details:
            config["WALLET_ADDRESS"]
            config["CHECK_INTERVAL"]
            etc.
        """
        self.config = config
        self.trade_executor = TradeExecutor(config)
        self._running = True

    def check_wallet_for_rewards(self):
        """
        Mock function to check if there are new rewards.
        In a real environment, you'd query the blockchain or an API.
        """
        logger.info("Checking wallet for new rewards (mocked).")
        # Suppose we detect 1.23 new coins
        new_coins = 1.23
        return new_coins

    def run(self):
        """
        Periodically checks for new rewards and triggers a trade to ETH.
        """
        logger.info("WalletChecker started.")
        while self._running:
            new_coins = self.check_wallet_for_rewards()
            if new_coins > 0:
                logger.info(f"Detected {new_coins} newly mined coins.")
                self.trade_executor.convert_to_eth(coin="XMR", amount=new_coins)
            time.sleep(self.config.get("CHECK_INTERVAL", 600))

    def stop(self):
        self._running = False
        logger.info("WalletChecker stopped.")
