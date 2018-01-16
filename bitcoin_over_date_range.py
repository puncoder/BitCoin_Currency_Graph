# Fetches the Bitcoin rate from a given range of date. plot and saves it in same directory.
# Author : AMiT Yadav
# Mail for any suggestions or bug : theamitcoder@gmail.com

import json
import os
import sys
import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('font', size=6)

def main():
    start_date, start_month, start_year = start_date_list
    end_date, end_month, end_year = end_date_list

    date_dict = dict()
    date_dict['START_DATE'] = "{:4d}-{:02d}-{:02d}".format(start_year, start_month, start_date)
    date_dict['END_DATE'] = "{:4d}-{:02d}-{:02d}".format(end_year, end_month, end_date)

    bitcoin_month_data_api = 'https://api.coindesk.com/v1/bpi/historical/close.json?start={START_DATE}&end={END_DATE}'
    bitcoin_month_data_api = bitcoin_month_data_api.format(**date_dict)

    try:

        data_list = str(json.loads(requests.get(bitcoin_month_data_api).text)['bpi'])[1:-1].split(',')

        rate_list = [float(item.split(':')[1]) for item in data_list]

        test_dates = pd.date_range(start=pd.datetime(start_year, start_month, start_date),
                                   end=pd.datetime(end_year, end_month, end_date))

        plt.plot(test_dates, rate_list)
        fig_name = f"{date_dict['START_DATE']}_TO_{date_dict['END_DATE']}.jpg"
        plt.xlabel('DATE', fontsize=18)
        plt.ylabel('PRICE (USD)', fontsize=16)
        plt.savefig(fig_name)

        plt.show()
    except Exception as e:
        input('Invalid date range..')
        sys.exit(1)


if __name__ == '__main__':
    os.system('color 0D')
    start_Date = input('Enter the start date (DD-MM-YYYY format) :: ').strip()
    end_Date = input('Enter the end date (DD-MM-YYYY format) :: ').strip()

    try:
        start_date_list = list(map(int,start_Date.split('-')))
        end_date_list = list(map(int, end_Date.split('-')))

    except Exception as e:
        input('Enter a correct date format DD-MM-YYYY , ex :: 15-12-2017')
        sys.exit(1)
    if len(start_date_list) == 3 and len(end_date_list) == 3:
        main()

    else:
        input('Enter a correct date format DD-MM-YYYY , ex :: 15-12-2017')
        sys.exit(1)
