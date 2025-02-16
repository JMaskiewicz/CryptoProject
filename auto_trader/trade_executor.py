import logging
from .exchange_api import ExchangeAPI
from .trade_logs import TradeLogs

logger = logging.getLogger(__name__)


class TradeExecutor:
    """
    Executes trades to convert mined coins into ETH.
    """

    def __init__(self, config):
        """
        :param config: dict containing trading-related config, e.g.:
            config["TRADE_PAIR"] = "XMR/ETH"
        """
        self.config = config
        self.exchange_api = ExchangeAPI(config)
        self.trade_logs = TradeLogs()

    def convert_to_eth(self, coin, amount):
        """
        Converts a given amount of `coin` into ETH.
        """
        trade_pair = self.config.get("TRADE_PAIR", f"{coin}/ETH")

        logger.info(f"Checking {coin} balance on exchange...")
        balance = self.exchange_api.get_balance(coin)

        if balance < amount:
            logger.warning(f"Requested {amount} {coin} but balance is {balance}. Setting amount to balance.")
            amount = balance

        logger.info(f"Creating sell order for {amount} {coin} on {trade_pair}")
        order_resp = self.exchange_api.create_order(
            symbol=trade_pair,
            side="sell",
            amount=amount,
            price=None  # market order in alpha version
        )

        self.trade_logs.log_trade(order_resp)
        return order_resp
