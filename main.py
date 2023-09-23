from tortoise import run_async
from client.binance.db import BinanceDbClient
from client.binance.redis_db import BinanceRedisClient
from init_file import init_log, init_database

# Инициализация базы данных SQLite3
run_async(init_database())

# Инициализация логгера
init_log()

# Запуск отдельного потока для базы данных SQLite3
binance_btc_db_client = BinanceDbClient(
    currency="BTCUSDT", period=5
)
binance_btc_db_client.start()

# Запуск отдельного потока для базы данных Redis
binance_ltc_redis_client = BinanceRedisClient(
    currency="ETHBTC", period=3
)
binance_ltc_redis_client.start()
