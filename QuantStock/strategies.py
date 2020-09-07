# Strategies for stock market

# 5 Min Intraday strategy. Dataframe with timestamp as index
def backtest_Intraday_5min_strategy(df):
    SELL = False
    BUY = False
    for row in df.itertuples():
        if row.Close < row.SMA6 and SELL is False:
            print(row.Index, row.Close, row.SMA6, "SELL")
            SELL = True
            BUY = False
        if row.Close > row.SMA6 and BUY is False:
            print(row.Index, row.Close, row.SMA6, "BUY")
            BUY = True
            SELL = False