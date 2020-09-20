import yfinance as yf
import pandas as pd
from openpyxl import load_workbook
import datetime as dt
from stock_config import nifty50_stock_list as stock_list

def get_valid_date(start_date, end_date):
    valid = False
    num_tries = 0
    while not valid and num_tries <=5:
        valid_check_data = yf.download('RELIANCE.NS', start = start_date, end=end_date)
        try:
            open_price = valid_check_data.iloc[0]['Open']
            valid = True
            num_tries = 0
        except:
            start_date = (pd.to_datetime(start_date) + pd.DateOffset(days=1)).strftime('%Y-%m-%d')
            end_date = (pd.to_datetime(end_date) + pd.DateOffset(days=1)).strftime('%Y-%m-%d')
            valid = False
            num_tries += 1
    return start_date, end_date

def main_logic(eval_date):
    start_date=eval_date
    end_date = (pd.to_datetime(start_date) + pd.DateOffset(days=1)).strftime('%Y-%m-%d')
    start_date, end_date = get_valid_date(start_date, end_date)

    data = yf.download(stock_list, start = start_date, end=end_date)
    this_month_close = pd.DataFrame(data.iloc[0]['Adj Close'])

    start_date=(pd.to_datetime(eval_date) - pd.DateOffset(months=1)).strftime('%Y-%m-%d')
    end_date = (pd.to_datetime(start_date) + pd.DateOffset(days=1)).strftime('%Y-%m-%d')

    start_date, end_date = get_valid_date(start_date, end_date)

    data = yf.download(stock_list, start = start_date, end=end_date)
    last_month_close = pd.DataFrame(data.iloc[0]['Adj Close'])

    final_df = last_month_close.join(this_month_close)
    final_df.rename(columns =lambda t: t.strftime('%Y-%m-%d'), inplace=True)

    ## Calculate Momentum
    last_month_date = final_df.columns[0]
    this_month_date = final_df.columns[1]
    final_df['Change'] = final_df[this_month_date] - final_df[last_month_date]
    final_df['% Change'] = (final_df['Change'] / final_df[last_month_date])*100

    ## Final Output
    final_df.sort_values(by=['% Change'], ascending=False, inplace=True)
    final_df.rename_axis('MOMENTUM_ATH', inplace=True)
    final_df.rename_axis('', axis='columns', inplace=True)

    ## Output to File
    ### Create an empty excel file as below filename before running below code
    filename = f'data/output/momentum_monthly_output.xlsx'
    book = load_workbook(filename)
    writer = pd.ExcelWriter(filename, engine = 'openpyxl')
    writer.book = book

    final_df.round(2).to_excel(writer, sheet_name=eval_date)
    writer.save()
    writer.close()


if __name__ == "__main__":

    start_date = "2020-03-20"
    end_date = "2020-09-18"

    dt_start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
    dt_end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

    eval_date = dt_start_date
    while eval_date <= dt_end_date:
        eval_date = eval_date.strftime('%Y-%m-%d')
        print(eval_date)
        main_logic(eval_date)
        eval_date = (pd.to_datetime(eval_date) + pd.DateOffset(days=7))