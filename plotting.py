import robin_stocks as rs
import pandas as pd
import finnhub
import numpy as np
import matplotlib.pyplot as plt
from plotting import *
import config as c
import ta
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


coin_info = []


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

    coin_info.append([i,prices,dates])
    

#"COINBASE:BCH-USD"
#"BITFINEX:BSVUSD"


def s_r(symbol):
    print(f.support_resistance(symbol, '60'))
    return f.support_resistance(symbol, '60')
   




def plotting(dates,price,symbol,ticker):

    sr = s_r(ticker)
    chg= round(((price.max()-price.min())/price.min())*100,2)

    plt.figure(figsize=(14,10))
    plt.title('%s Analysis %s' % (symbol,chg) )
    plt.plot(dates, price, label="Closing prices")
    t = ta.trend.ema_indicator(price, n=12, fillna=False)
    l = ta.trend.ema_indicator(price, n=26, fillna=False)
    # z = ta.trend.ema_indicator(coin[1], n=55, fillna=False)
    # plt.plot(dates,z,label=' 55 EMA', color='#B60404')
    plt.plot(dates,t,label='12 EMA', color='#1D8319')
    plt.plot(dates,l,label='26 EMA', color='#F39839')
    for lvl in sr.get('levels'):
        plt.hlines(lvl,dates.min(),dates.max(),colors='#4B4473')
    
    plt.yticks(np.arange(price.min(), price.max(), step=((price.max()-price.min())/15.0)))
    plt.legend()
    plt.show()

def prnt_tick(tickers):
    for i in tickers:
        print('Ticker:  %s' % i)

prnt_tick(tickers)

def select_chart(tickers):
    plot_chart = input('Which Coin Would you like to plot')

    while plot_chart not in tickers:
        print('Coin not found, Try again')
        prnt_tick(tickers)
        plot_chart = input('Which Coin Would you like to plot')
    else:
        if plot_chart == 'BSV':
            ticker ='BITFINEX:BSVUSD'
            for x in coin_info:
                if plot_chart == x[0]:
                    plotting(x[2],x[1],x[0],ticker)
        else:
            ticker = 'COINBASE:%s-USD' % plot_chart
            for x in coin_info:
                if plot_chart == x[0]:
                    plotting(x[2],x[1],x[0],ticker)    


#------------------------------------------------------------------------------------------------------------

# # print(rc.get_crypto_positions(info='name'))

# st = ta.trend.ema_indicator(coin_info[0][1], n=8, fillna=True)
# mt = ta.trend.ema_indicator(coin_info[0][1], n=13, fillna=True)
# xt = ta.trend.ema_indicator(coin_info[0][1], n=55, fillna=True)


# lt = ta.trend.ema_indicator(coin_info[0][1], n=21, fillna=True)

# series = [coin_info[0][1].rename('Price'), coin_info[0][2].rename('Dates'), st.rename('8 Day EMA'), mt.rename('13 Day EMA'), lt.rename('21 Day EMA'), xt.rename('55 Day EMA')]

# coin_df = pd.concat(series, axis=1)
# print(coin_df.loc[5,'Dates'])

# coin_df['Signal'] = 0.0

# coin_df['Signal'] = np.where(coin_df['8 Day EMA']>coin_df['55 Day EMA'],1.0,0.0)

# plt.figure(figsize = (20,10))
# # plot close price, short-term and long-term moving averages 
# coin_df['Price'].plot(color = 'k', label= 'Close Price') 
# coin_df['8 Day EMA'].plot(color = 'b',label = '8') 
# coin_df['55 Day EMA'].plot(color = 'g', label = '55')
# # plot ‘buy’ signals
# for i in range(len(coin_df)):
#     idx=0
#     if coin_df.loc[idx,'Signal'] != coin_df.loc[idx+1,'Signal']:
#         if coin_df.loc[idx,'Signal'] > coin_df.loc[idx+1,'Signal']:
#             plt.plot(coin_df.loc[idx,'Dates'],coin_df.loc[idx,'Price'],marker = 'v')
#         else:
#             plt.plot(coin_df.loc[idx,'Dates'],coin_df.loc[idx,'Price'],marker = '^')


# plt.ylabel('Price in Rupees', fontsize = 15 )
# plt.xlabel('Date', fontsize = 15 )
# plt.title('Buy/Sell', fontsize = 20)
# plt.legend()
# plt.grid()
# plt.show()
     
# select = input('To plot charts press 1, otherwise press enter to logout')
# select_chart(tickers)

# if select == 1:
#     select_chart(tickers)

#------------------------------------------------------------------------------------------------------------
