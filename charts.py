import robin_stocks as rs
import matplotlib.pyplot as plt
import requests
import finnhub
from config import finn_key
import ta

f=finnhub.Client(api_key=finn_key)



def plotting(dates,price):
    plt.figure(figsize=(10,5))
    plt.title('test')
    plt.plot(dates, price, label="Closing prices")
    plt.yticks(np.arange(price.min(), price.max(), step=((price.max()-price.min())/15.0)))
    plt.legend()
    plt.show()

def get_sr(symbol):
    
    f.support_resistance(symbol, '60')

    print(symbol + ' S/R levels are: ',levels )


# def graph(price,f1,f2,dates,symbol):

