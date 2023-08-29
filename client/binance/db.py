import asyncio
import logging
from threading import Thread
import httpx
import time
from models import TokenPrices


class BinanceDbClient(Thread):

    def __init__(self, currency, period):
        Thread.__init__(self)
        self.currency = currency
        self.period = period
        self.url = f"https://api.binance.com/api/v3/avgPrice"

    def run(self):
        while True:
            logging.info("Getting response for DATABASE")
            r = httpx.get(self.url, params={"symbol": f"{self.currency}"}).json()
            time_out = time.strftime("%H:%M:%S", time.localtime())
            print(f"Current time from SQLDB Thread:  {time_out}")
            new_price = TokenPrices(
                name_token=self.currency, price=r['price'], data=time_out
            )

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(new_price.save())

            time.sleep(self.period)

