import random
import redis
import logging
from threading import Thread
import httpx
import time


class BinanceRedisClient(Thread):

    def __init__(self, currency, period):
        Thread.__init__(self)
        self.currency = currency
        self.period = period
        self.url = f"https://api.binance.com/api/v3/avgPrice"
        self.r = redis.Redis(host='localhost', port=6379)
        self.count = 0

    def run(self):
        while True:
            logging.info("Getting response for REDIS")
            response = httpx.get(self.url, params={"symbol": f"{self.currency}"}).json()
            print(f"Random number from REDIS Thread: {random.randint(1, 10)}")
            self.r.set(f"New_entry REDIS {self.count}", response["price"])
            self.count += 1

            time.sleep(self.period)

