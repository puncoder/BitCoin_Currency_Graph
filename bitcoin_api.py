# Python 3.0 + version only
import requests
import json

bitcoin_api = 'https://api.coindesk.com/v1/bpi/currentprice.json'   # Bitcoin rate API
usd_in = 'https://api.fixer.io/latest?symbols=USD,INR&base=USD'     # Currency conversion API

res_bitcoin_api = requests.get(bitcoin_api).text
res_rate_usd_inr = requests.get(usd_in).text

rate = json.loads(res_rate_usd_inr)['rates']['INR']

data_dict = json.loads(res_bitcoin_api)
time = data_dict['time']['updated']

price_usd = data_dict['bpi']['USD']['rate_float']
price_inr = price_usd * rate

print(f'Time : {time}')
print(f'Bitcoin Price (USD) :: %.03f USD' % price_usd)
print(f'Bitcoin Price (INR) :: %.03f INR' % price_inr)
