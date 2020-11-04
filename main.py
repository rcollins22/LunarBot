import robin_stocks as rs
import pandas as pd
import finnhub
import numpy as np
import matplotlib.pyplot as plt
from plotting import coin_info,select_chart,tickers
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

st = ta.trend.ema_indicator(coin_info[0][1], n=8, fillna=True)
mt = ta.trend.ema_indicator(coin_info[0][1], n=13, fillna=True)
xt = ta.trend.ema_indicator(coin_info[0][1], n=55, fillna=True)
lt = ta.trend.ema_indicator(coin_info[0][1], n=21, fillna=True)


series = [coin_info[0][1].rename('Price'), coin_info[0][2].rename('Dates'), st.rename('8 Day EMA'), mt.rename('13 Day EMA'), lt.rename('21 Day EMA'), xt.rename('55 Day EMA')]

coin_df = pd.concat(series, axis=1)

select_chart(tickers)
# for i in coin_df:

print(coin_df.head(100))

# rs.logout()
