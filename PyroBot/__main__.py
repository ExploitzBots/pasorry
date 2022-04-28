import os
import logging
import pyrogram
from decouple import config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# vars
APP_ID = "5689646"
API_HASH = "895de5ae804308803c19814afabb0de7"
BOT_TOKEN = "5205589679:AAFlYLOb1TJ0uihGnCgWwASf6_8_i4ClEP0"

if __name__ == "__main__" :
    print("Starting Bot...")
    plugins = dict(root="PyroBot/plugins")
    b1 = pyrogram.Client(
        "S1",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    b1.run()
