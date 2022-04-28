from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message("Hi")
