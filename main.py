import robin_stocks as rs
import pandas as pd
import finnhub
import numpy as np
import matplotlib.pyplot as plt
import config as c



f=finnhub.Client(api_key=c.finn_key)
rc = rs.crypto

rs.login(
    username=c.un,
    password=c.pw,
    expiresIn=86400,
    by_sms=True
)

info = rc.get_crypto_currency_pairs()

tickers=[]
for i in info:
    if i.get('tradability') == 'tradable' and i.get('symbol') != 'DOGE-USD':
        s = i.get('symbol')[:-4]
        tickers.append(s)


date_info = []
price_info = []

for i in tickers:
    prices = []
    dates = []
    h = rc.get_crypto_historicals(i, interval='hour', span='week', bounds='24_7')
    for x in h:
        prices.append(float(x.get('close_price')))
        dates.append(x.get('begins_at'))
    
    dates = pd.Series(dates)
    dates = pd.to_datetime(dates)
    print(dates)
    dates=dates.values
    prices = pd.Series(prices)
    # prices = prices.values
    
    date_info.append({i:dates})
    price_info.append({i:prices})
    
    

#"COINBASE:BCH-USD"
#"BITFINEX:ADAUSD"

print(tickers)

def s_r(symbol):
    print(f.support_resistance(symbol, '60'))
   



def plotting(dates,price):
    plt.figure(figsize=(10,5))
    plt.title('test')
    plt.plot(dates, price, label="Closing prices")
    plt.yticks(np.arange(price.min(), price.max(), step=((price.max()-price.min())/15.0)))
    plt.legend()
    plt.show()

# plotting(date_info[0].get('BTC'),price_info[0].get('BTC'))

s_r("COINBASE:BTC-USD")
rs.logout()
# print(type(float(price_info[0].get('BTC').min())))