import robin_stocks as rs
import pandas as pd
import numpy as np
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
    if i.get('tradability') == 'tradable':
        s = i.get('symbol')[:-4]
        tickers.append(s)


for i in tickers:
    rc.get_crypto_historicals(i, interval='hour', span='week', bounds='24_7')




# print(rc.get_crypto_historicals('DOGE', interval='hour', span='week', bounds='24_7'))
print(tickers)
print(np.nan)
rs.logout()