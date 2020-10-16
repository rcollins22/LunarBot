import robin_stocks as rs
import config as c


rc = rs.crypto

rs.login(
    username=c.un,
    password=c.pw,
    expiresIn=86400,
    by_sms=True
)

info = rc.get_crypto_currency_pairs()


for i in info:
    if i.get('tradability') == 'tradable':
        print(i.get('symbol'))

print(rc.get_crypto_positions())

rs.logout()