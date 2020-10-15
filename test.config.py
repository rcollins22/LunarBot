# 1. COPY AND RENAME THE COPY TO 'config.py'

# 2. REPLACE 'username' AND 'password' WITH YOUR CREDENTIALS


import robin_stocks as rs

rs.login(
    username='change this to your username',  #to be changed
    password='change this to you password',    #to be changed
    expiresIn=86400,                        #sets expiration time to 1 day (24hrs). The max Robinhood offers
    by_sms=True                 #2 factor authentication by either SMS if True, otherwise by email if False.
)

print(rs)