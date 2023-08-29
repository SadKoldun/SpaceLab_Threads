from tortoise import run_async
from client.binance.db import BinanceDbClient
from client.binance.redis_db import BinanceRedisClient
from init_file import init_log, init_database


run_async(init_database())
init_log()


binance_btc_db_client = BinanceDbClient(
    currency="BTCUSDT", period=5
)
binance_ltc_redis_client = BinanceRedisClient(
    currency="ETHBTC", period=3
)

binance_btc_db_client.start()
binance_ltc_redis_client.start()
