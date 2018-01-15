# Fetches the Bitcoin rate for all the countries mention in the API and saves in a CSV file, in same directory.
import json
import requests

country_list_api = 'https://api.coindesk.com/v1/bpi/supported-currencies.json'
country_rate_api = 'https://api.coindesk.com/v1/bpi/currentprice/{country_code}.json'

# fetching all the country currency codes
currency_json = json.loads(requests.get(country_list_api).text)
country_currency_codes = [item['currency'] for item in currency_json]

# fetching all the country price using the rate api.
full_data = dict()

for code in country_currency_codes:
    code_dict = dict()
    code_dict['country_code'] = code
    full_data[code] = dict()
    url = country_rate_api.format(**code_dict)
    text_res = requests.get(url).text
    res_dict = json.loads(text_res)
    full_data[code]['time'] = res_dict['time']['updated']
    full_data[code]['description'] = res_dict['bpi'][code]['description']
    full_data[code]['rate_float'] = res_dict['bpi'][code]['rate_float']
    print(f"\t{full_data[code]['description']} :: {full_data[code]['rate_float']} {code}")


# Once all the data is stored in DICT, save it to the file
print('Writing data in file .. ')
with open('Currency_list.csv', 'w', encoding= 'UTF-8') as file:
    file.write(f"Time,{full_data[code]['time']}\n")
    for code in sorted(full_data):
        file.write(f"{full_data[code]['description']},{full_data[code]['rate_float']},{code},\n")

input('Successful...')






