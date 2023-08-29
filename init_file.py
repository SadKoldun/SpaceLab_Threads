import logging
from tortoise import Tortoise


def init_log():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)


async def init_database():
    await Tortoise.init(db_url="sqlite://db2.sqlite3", modules={"models": ["models"]})
    await Tortoise.generate_schemas()
