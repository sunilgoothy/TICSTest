#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import datetime as dt
import time
import sqlite3
import os

# #### Connect to Sqlite

# In[8]:


conn = sqlite3.connect("data/stocks.db3")


# ### Enter Evaluation date and scrip name

# In[9]:


scrip = 'NIFTY SEP FUT'
eval_date = '2020-09-11'


# In[10]:


def Intraday_5min_strategy(df):
    #Parameters
    STOPLOSS = 25
    SMA6_dead_band = 10
    start_time = dt.datetime.strptime("09:20", "%H:%M").time()
    close_time = dt.datetime.strptime("15:15", "%H:%M").time()
    entry_close_time = dt.datetime.strptime("15:00", "%H:%M").time()  

    #Other Variables
    SELL = False
    BUY = False
    SELL_PRICE = 0
    BUY_PRICE = 0
    GAIN_POINTS = 0
    SELL_STOPLOSS = 0
    BUY_STOPLOSS = 0
    Total_Signals = 0
    Total_Sell_Signal = 0
    Total_Buy_Signal = 0
    print("\n\nScan Results:")
    print("Time\t\t\t", "Close\t\t", "SMA6\t\t", "SIGNAL\t", "TYPE\t\t",  "Points\t",)
    
    for row in df.itertuples():
        SMA6_upper_band = row.SMA6 + SMA6_dead_band
        SMA6_lower_band = row.SMA6 - SMA6_dead_band
        
        # SELL STOPLOSS
        if row.Index.time() >= start_time and row.Index.time() <= close_time: 
            points = 0
            if SELL and row.Close > SELL_STOPLOSS:
                SELL = False
                BUY = False
                Total_Signals += 1
                Total_Buy_Signal += 1
                points = SELL_PRICE - row.Close
                GAIN_POINTS = GAIN_POINTS + points
                SELL_PRICE = 0
                print(row.Index, "\t",  row.Close, "\t", round(row.SMA6,2), "BUY\t", "SELL STOPLOSS\t", round(points,2))
            
            # BUY STOPLOSS
            points = 0
            if BUY and row.Close < BUY_STOPLOSS:
                points = row.Close - BUY_PRICE
                GAIN_POINTS = GAIN_POINTS + points
                BUY_PRICE = 0
                SELL = False
                BUY = False
                Total_Signals += 1
                Total_Sell_Signal += 1
                print(row.Index, "\t",  row.Close, "\t", round(row.SMA6,2), "\t", "SELL\t", "BUY STOPLOSS\t", round(points,2))
            
            # SELL ENTRY
            points = 0
            if row.Close < SMA6_lower_band and                     row.Index.time() < entry_close_time and                     SELL is False:
                SELL_PRICE = row.Close
                SELL_STOPLOSS = SELL_PRICE + STOPLOSS
                if BUY_PRICE > 0:
                    points = SELL_PRICE - BUY_PRICE
                    GAIN_POINTS = GAIN_POINTS + points
                SELL = True
                BUY = False
                Total_Sell_Signal += 1
                Total_Signals += 1
                print(row.Index, "\t",  row.Close, "\t", round(row.SMA6,2),  "\t", "SELL\t", "SELL ENTRY\t", round(points,2))
             
            # BUY ENTRY
            points = 0
            if row.Close > SMA6_upper_band and                     row.Index.time() < entry_close_time and                     BUY is False:
                BUY_PRICE = row.Close
                BUY_STOPLOSS = BUY_PRICE - STOPLOSS
                if SELL_PRICE > 0:
                    points = SELL_PRICE - BUY_PRICE
                    GAIN_POINTS = GAIN_POINTS + points
                BUY = True
                SELL = False
                Total_Buy_Signal += 1
                Total_Signals += 1
                print(row.Index, "\t", row.Close,  "\t", round(row.SMA6,2),  "\t", "BUY\t", "BUY ENTRY\t", round(points,2))
            
            # DAY Close
            points = 0    
            if row.Index.time() >= close_time:
                if SELL:
                    SELL = False
                    BUY = False
                    Total_Signals += 1
                    Total_Buy_Signal += 1
                    points = SELL_PRICE - row.Close
                    GAIN_POINTS = GAIN_POINTS + points
                    SELL_PRICE = 0
                    print(row.Index, "\t",  row.Close, "\t", round(row.SMA6,2),  "\t", "BUY\t", "BUY DAYCLOSE\t", round(points,2))

                if BUY:
                    SELL = False
                    BUY = False
                    Total_Signals += 1
                    Total_Buy_Signal += 1
                    points = row.Close - BUY_PRICE
                    GAIN_POINTS = GAIN_POINTS + points
                    SELL_PRICE = 0
                    print(row.Index, "\t",  row.Close, "\t", round(row.SMA6,2),  "\t", "SELL\t", "SELL DAYCLOSE\t", round(points,2))
                    
                    
    
    print("\n\nTotal Signals:\t\t", Total_Signals)
    print("Total Sell Signals:\t", Total_Sell_Signal)
    print("Total Buy Signals:\t", Total_Buy_Signal)
    print("Total Points Gained:\t", round(GAIN_POINTS,2))


# In[11]:


def start_intraday_monitor(scrip, eval_date):
    sql_stmt = f"select * from Intraday where scrip = '{scrip}' and timestamp > '{eval_date}'"
    df = pd.read_sql_query(sql_stmt, conn, parse_dates=['timestamp'])
    
    # Set timestamp as index
    df.set_index('timestamp', inplace=True)
    
    # Resample data for every 5 min
    df = df.resample('5T').first()
    
    # Apply rolling mean columns for data
    df['SMA6'] = df['Close'].rolling(6).mean()
    df['SMA21'] = df['Close'].rolling(21).mean()
    
    #Display summary
    print(df.tail(25))

    # Calculate entries/exits
    Intraday_5min_strategy(df)
    


# In[12]:
clear = lambda: os.system('cls')

while True:
    clear()
    start_intraday_monitor(scrip, eval_date)
    print("*", end=" ", flush=True)
    time.sleep(10)


# In[ ]:




