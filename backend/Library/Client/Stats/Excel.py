import pandas as pd
from datetime import timedelta, datetime

def convert_to_timedelta(time_val):
    num = int(time_val[:-1])
    if time_val.endswith('s'):
        return timedelta(seconds=num)
    elif time_val.endswith('m'):
        return timedelta(minutes=num)
    elif time_val.endswith('h'):
        return timedelta(hours=num)
    elif time_val.endswith('d'):
        return timedelta(days=num)

def duration_column_convert(t):
    deltas = [ convert_to_timedelta(v).total_seconds() for v in t.split()]
    return sum(deltas)

def created_column_convert(t):
    return t.isoformat()
    # return datetime.strptime(t, '%d/%b/%Y %I:%M %p')

def ReadExcel(path):
    customize = {'Created': created_column_convert, 'Time to resolution': duration_column_convert }
    df = pd.read_excel(path, sheet_name=0, index_col=None, header=0, converters=customize, keep_default_na=False)
    df.rename(columns={'Time to resolution': 'Duration', 'Fix Version/s': 'FixVersion'}, inplace=True)
    return df.to_dict('records')
