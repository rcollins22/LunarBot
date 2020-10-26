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
coin_info=[]

for i in tickers:
    prices = []
    dates = []
    h = rc.get_crypto_historicals(i, interval='hour', span='month', bounds='24_7')
    for x in h:
        prices.append(float(x.get('close_price')))
        dates.append(x.get('begins_at'))
    
    dates = pd.Series(dates)
    dates = pd.to_datetime(dates)
    prices = pd.Series(prices)
    
    date_info.append({i:dates})
    price_info.append({i:prices})
    coin_info.append([i,prices,dates])
    
# print(coin_info)

#"COINBASE:BCH-USD"
#"BITFINEX:BSVUSD"

print(tickers)

def s_r(symbol):
    print(f.support_resistance(symbol, '60'))
    return f.support_resistance(symbol, '60')
   

# print(date_info[0].get('BTC'))
# sr = s_r("COINBASE:BTC-USD")




def plotting(dates,price,symbol,ticker):

    sr = s_r(ticker)
    chg= ((price.max()-price.min())/price.min())*100

    plt.figure(figsize=(10,6))
    plt.title('%s Analysis %s' % (symbol,chg) )
    plt.plot(dates, price, label="Closing prices")
    
    for lvl in sr.get('levels'):
        plt.hlines(lvl,dates.min(),dates.max(),colors='#A70F0F')
    
    plt.yticks(np.arange(price.min(), price.max(), step=((price.max()-price.min())/15.0)))
    plt.legend()
    plt.show()

for coin in coin_info:
    if coin[0] == 'BSV':
        ticker ='BITFINEX:BSVUSD'
    else:
        ticker = 'COINBASE:%s-USD' % coin[0]
    
    plotting(coin[2],coin[1],coin[0],ticker)




rs.logout()
