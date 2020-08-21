import pandas as pd
import numpy as np
import csv

def csvToDic2(filename):
    rs_dict = dict()
    try:
        with open(filename, encoding='utf_16_le') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter='\t')
            line_count = 0
            for row in csv_reader:
                _temp = {}
                if line_count == 0:
                    _key = list(row.keys())
                commented_line = row[_key[0]].startswith('#')
                if ( not commented_line ):
                    for record in row:
                        if (record != _key[0]) and (record != ''):
                            _temp[record] = row[record]

                    rs_dict[row[_key[0]]]=_temp
                line_count += 1
            print(f'<INFO> csvToDic Processed {line_count} lines from {filename}.')
    except Exception as e:
        print(f'<ERR> Not able to read data from csv, msg: {e}')

    return rs_dict




data_nf5 = dict()
def load_csv():
    data_nf5 = csvToDic2('data/Nifty-Futures-Aug.csv')
    # print(data_nf5['20-08-2020 14:00:00'])
    df_nf5 = pd.read_csv('data/Nifty-Futures-Aug.csv', sep='\t', encoding='utf_16_le')
    df_nf5 = df_nf5[df_nf5.columns[:-1]]
    
def Nifty_Intraday():
    df_nf5['MA6'] = df_nf5['Close'].rolling(6).mean()
    df_nf5['MA21'] = df_nf5['Close'].rolling(21).mean()
    for i, j in df_nf5.iterrows():
        if(j['Close']<j['MA6']):
            j['Signal'] = 'BUY'
        print(j)
    # print(df_nf5)

def SMA(data as dict):
    print(data['20-08-2020 14:00:00'])


if __name__ == '__main__':
    # data_nf5 = csvToDic2('data/Nifty-Futures-Aug.csv')
    # SMA(data_nf5)
    Nifty_Intraday()
    