import pandas as pd
import requests

data = requests.get('https://climatereanalyzer.org/clim/t2_daily/json/cfsr_world_t2_day.json').json()

list_ = []
for year in pd.DataFrame(data)['data'].iloc[:-3]:
  list_.extend(year)

temp = [x for x in list_ if x != None]

dates = pd.date_range(start='1979-01-01', periods=len(temp))

df = pd.Series(temp,index=dates).rename('temp').rename_axis('date').reset_index()

df['year'] = df.date.dt.year

df['monthday'] = '2020' + df.date.dt.month.astype(str).str.zfill(2) + df.date.dt.day.astype(str).str.zfill(2)

df.monthday = pd.to_datetime(df.monthday)

df.to_csv('temp.csv',index=False)