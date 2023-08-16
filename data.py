import pandas as pd
import requests
from path import DATA_DIR

def download_data_from_coinbase(
        product_id,from_day,to_day
):
    data=pd.date_range(start=from_day,end=to_day,freq="1D")
    days=[day.strftime("%Y-%m-%d") for day in data]
    
    if not (DATA_DIR / 'downloads').exists():
        (DATA_DIR / 'downloads').mkdir(parents=True) 
    data=pd.DataFrame()
    for day in days:
        file_name = DATA_DIR / 'downloads' / f'{day}.csv'
        if file_name.exists():
            data_one_day=pd.read_csv(file_name)
        else:
            data_one_day=download_data_for_one_day(product_id,day)
            data_one_day.to_csv(file_name,index=False)
        
        data=pd.concat([data,data_one_day])
    data.to_csv(DATA_DIR/f"final_data.csv",index=False)
    return DATA_DIR/"final_data.csv"

def download_data_for_one_day(product_id: str, day: str) -> pd.DataFrame:
    """
    Downloads one day of data and returns pandas Dataframe
    """
    start = f'{day}T00:00:00'
    from datetime import datetime, timedelta
    end = (datetime.strptime(day, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    end = f'{end}T00:00:00'
    URL = f'https://api.exchange.coinbase.com/products/{product_id}/candles?start={start}&end={end}&granularity=3600'
    r = requests.get(URL)
    data = r.json()
    return pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])


if __name__=="__main__":
    download_data_from_coinbase("BTC-USD","2022-01-01","2022-02-01")