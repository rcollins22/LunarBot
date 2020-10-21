import robin_stocks as rs
import matplotlib.pyplot as plt
import requests
from config import finn_key





def get_sr(symbol):
    url = 'https://finnhub.io/api/v1/scan/support-resistance?symbol=%s&resolution=D&token=%s' % (symbol,finn_key)
    payload = {}
    headers = {
    'Cookie': '__cfduid=d87ca348f6d8449fdfa644aec4b3ca8361602800210'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    raw = response.json()
    levels = raw.get('levels')

    print(symbol + 'S/R levels are: ',levels )


def graph(price,f1,f2,dates,symbol):

