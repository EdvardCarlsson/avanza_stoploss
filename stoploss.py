


import numpy as np
import yfinance as yf
import time
from avanza import Avanza, OrderType
from datetime import date
    
def sell(avanza, s1):

    # should be automated
    avanza.place_order(
        account_id='ACCOUNT_NUMBER',           
        order_book_id= "{}".format(s1[0]),
        order_type=OrderType.SELL,
        price=s1[1],   
        valid_until=date.today(),
        volume=s1[2])

def main():
    
    #authenticate 
    avanza = Avanza({
        'username': 'USERNAME',
        'password': 'PASSWORD',
        'totpSecret': 'TOTPSECRET'
        })
    
    # example of two stocks
    # y_name, av_id, sellprice, sellvolym
    kambi = ["KAMBI.ST", "482657", 500, 1]
    piedmont = ["PLL", "875182", 80, 1]
    lst = [kambi, piedmont]

    stks = {}
    for i in range(len(lst)):
        stks[lst[i][0]] = [lst[i][1], lst[i][2], lst[i][3]] 
        

    while(True):
        time.sleep(5)
        
        for stock in stks:
            if type(stks[stock]) is float:
                continue
            close = yf.download(tickers=stock, period='5m', interval='1m')             
            if close["Close"].iloc[-1] < stks[stock][1]:    
                sell(avanza, stks[stock])
                stks[stock] = np.nan
        

if __name__ == "__main__": 
    main()

