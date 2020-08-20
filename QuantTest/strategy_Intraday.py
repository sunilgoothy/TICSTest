import pandas as pd
import numpy as np

df_nf5 = pd.read_csv('data/Nifty-Futures.csv', sep='\t')
df_nf5 = df_nf5[df_nf5.columns[:-1]]

def Nifty_Intraday():
    df_nf5['MA6'] = df_nf5['Close'].rolling(6).mean()
    df_nf5['MA21'] = df_nf5['Close'].rolling(21).mean()
    print(df_nf5)

if __name__ == '__main__':
    Nifty_Intraday()
    