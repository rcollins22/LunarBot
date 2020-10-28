import robin_stocks as rs
import pandas as pd
import finnhub
import numpy as np
import matplotlib.pyplot as plt
from plotting import coin_info
import config as c
import ta



f=finnhub.Client(api_key=c.finn_key)


# rs.login(
#     username=c.un,
#     password=c.pw,
#     expiresIn=86400,
#     by_sms=True
# )
# rc = rs.crypto

# print(rc.get_crypto_positions(info='name'))

st = ta.trend.ema_indicator(coin_info[0][1], n=8, fillna=True)
mt = ta.trend.ema_indicator(coin_info[0][1], n=13, fillna=True)
xt = ta.trend.ema_indicator(coin_info[0][1], n=55, fillna=True)


lt = ta.trend.ema_indicator(coin_info[0][1], n=21, fillna=True)

series = [coin_info[0][1].rename('Price'), coin_info[0][2].rename('Dates'), st.rename('8 Day EMA'), mt.rename('13 Day EMA'), lt.rename('21 Day EMA'), xt.rename('55 Day EMA')]

coin_df = pd.concat(series, axis=1)

coin_df['Signal'] = 0.0

coin_df['Signal'] = np.where(coin_df['8 Day EMA']>coin_df['55 Day EMA'],1.0,0.0)

plt.figure(figsize = (20,10))
# plot close price, short-term and long-term moving averages 
coin_df['Price'].plot(color = 'k', label= 'Close Price') 
coin_df['8 Day EMA'].plot(color = 'b',label = '8') 
coin_df['55 Day EMA'].plot(color = 'g', label = '55')
# plot ‘buy’ signals
for i in range(len(coin_df)):
    if coin_df.loc[i,'Signal'] != coin_df.loc[i+1,'Signal']:
        if coin_df.loc[i,'Signal'] > coin_df.loc[i+1,'Signal']:
            plt.plot(coin_df.loc[i,'date'],coin_df.loc[i,'Price'],marker = 'v')
        else:
            plt.plot(coin_df.loc[i,'date'],coin_df.loc[i,'Price'],marker = '^')


plt.ylabel('Price in Rupees', fontsize = 15 )
plt.xlabel('Date', fontsize = 15 )
plt.title('Buy/Sell', fontsize = 20)
plt.legend()
plt.grid()
plt.show()

# for i in coin_df:

print(coin_df.head(100))

# rs.logout()
