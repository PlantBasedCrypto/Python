import time
import datetime
import pandas as pd
#, '^GSPC', 'SPG', 'VNQ', 'VTR', 'WELL', 'FRT', 'DLR', 'DOC', 'EQR', 'PEAK', 'HR', 'ESRT', 'BXP', 'SLG'

tickers = ['EXR', 'PLD','^GSPC', 'SPG', 'VNQ', 'VTR', 'WELL', 'FRT', 'DLR', 'DOC', 'EQR', 'PEAK', 'HR','HTA', 'ESRT', 'BXP', 'SLG']
interval = '1d'
period1 = int(time.mktime(datetime.datetime(2022, 2, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2023, 2, 13, 23, 59).timetuple()))

xlwriter = pd.ExcelWriter('historical prices.xlsx', engine='openpyxl')
for ticker in tickers:
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    df = pd.read_csv(query_string)
    df.to_excel(xlwriter, sheet_name=ticker,  index=False)
    
xlwriter.save()