import numpy as np
import pandas as pd
from binance.client import Client

api_key = 'votre_clef_api' 
api_secret = 'votre_secret_api'

client = Client(api_key, api_secret)

def get_market_data(symbol):
    bars = client.get_historical_klines(symbol, "5m", "100 days ago UTC")
    df = pd.DataFrame(bars, columns = ['time', 'open', 'high', 'low', 'close', 'volume']) 
    return df

def is_red_candle(candle):
    return candle['close'] < candle['open']

def trade_strategy(df):
    last_candle = df.iloc[-1]
    if is_red_candle(last_candle):
        print("Place order for PUT option")
    else:
        print("Place order for CALL option")
        
symbol = 'ETHUSDT'
bars = get_market_data(symbol)
trade_strategy(bars)