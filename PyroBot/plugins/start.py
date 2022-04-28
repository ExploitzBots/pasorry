from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, message):
    await message.reply_text(text="Hy",reply_to_message_id=message.message_id)
