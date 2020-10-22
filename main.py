import robin_stocks as rs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import config as c



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
        prices.append(x.get('close_price'))
        dates.append(x.get('begins_at'))
    
    dates = pd.Series(dates)
    dates = pd.to_datetime(dates)
    prices = pd.Series(prices)
    
    date_info.append({i:dates})
    price_info.append({i:prices})
    
    
print(dates)


#"COINBASE:BCH-USD"
#"BITFINEX:ADAUSD"

# print(rc.get_crypto_historicals('DOGE', interval='hour', span='week', bounds='24_7'))
print(tickers)
print(np.nan)
rs.logout()

def plotting(dates,price):
    plt.figure(figsize=(10,5))
    plt.title('test')
    plt.plot(dates, price, label="Closing prices")
    plt.yticks(np.arange(float(price.min()), float(price.max()),10))
    plt.legend()
    plt.show()

plotting(date_info[0].get('BTC'),price_info[0].get('BTC'))


# print(type(float(price_info[0].get('BTC').min())))