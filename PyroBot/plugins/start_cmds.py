import requests
import json
import time
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
#keys


# need variables
ok=["!",".","/",]

bbin = ['529750', '515462', '401658', '543816', '519479', '489504', '415285', '539150', '483698', '522974', '404942']

OWNER=[1808767615, 1007962272, 1237452850]

PREMIUM = [1868627711, 2104057670, 5050954667]

FREE = []
msg_count = 0
id_in_spam = []
# time variables
clock = 0
t=0

# the checker function
@Client.on_message(filters.command('cmds'))
def main_cmd(client, message):
  fname = message.from_user.first_name
  user_info = client.get_users(message.from_user.id)
  message.reply_text(f"**What you want to choose?**", reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Free Gates",
                        callback_data="gates1"
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "Premium Gates",
                        callback_data="charge"
                    ),
                ],
                [  # Second row
                    InlineKeyboardButton(  # Opens the inline interface
                        "Tools/Other",
                        callback_data="tools"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command(["start", "start@CardChkBot"], ok))
def start_cmd(client, message):
  fname = message.from_user.first_name
  user_info = client.get_users(message.from_user.id)
  message.reply_text(f"**Hy**\n\nWhich option you want to choose?", reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Free Gates",
                        callback_data="gates1"
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "Premium Gates",
                        callback_data="charge"
                    ),
                ],
                [  # Second row
                    InlineKeyboardButton(  # Opens the inline interface
                        "Tools/Other",
                        callback_data="tools"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("gates1"))
def freecmd(client, ok: CallbackQuery):
    ok.message.edit_text("**List commands:**\n\n**➣ Stripe Auth ✅\n`/sp cc|m|y|cvv`\n\nStripe 1$ ❌\n`/ch cc|m|y|cvv`**", reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Back",
                        callback_data="beck"
                    )
                ]
            ]
        )
    )

@Client.on_callback_query(filters.regex("charge"))
def paidcmd(client, ok: CallbackQuery):
    ok.message.edit_text("**List commands:**\n\nNo Commands", reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Back",
                        callback_data="beck"
                    )
                ]
            ]
        )
    )

@Client.on_callback_query(filters.regex("tools"))
def tool(client, ok: CallbackQuery):
    ok.message.edit_text("**List commands:**\n\n!bin - --Bin Look Up--", reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Back",
                        callback_data="beck"
                    )
                ]
            ]
        )
    )

@Client.on_callback_query(filters.regex("beck"))
def beck(client, ok: CallbackQuery):
    ok.message.edit_text(f"**Hy**\n\nWhich option you want to choose?", reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Free Gates",
                        callback_data="gates1"
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "Premium Gates",
                        callback_data="charge"
                    ),
                ],
                [  # Second row
                    InlineKeyboardButton(  # Opens the inline interface
                        "Tools/Other",
                        callback_data="tools"
                    )
                ]
            ]
        )
    )
