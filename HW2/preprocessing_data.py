# preprocessing_data - файл подготовки данных
import pandas as pd

def data_missing(data):  
    cols_with_na = data.columns[data.isnull().any()]

    if len(cols_with_na) == 0:
         print("Пропусков нет")
    else:
         for col in cols_with_na:
           print(f"{col}: {data[col].isnull().sum()} пропусков")

def fill_missing_mean(data):
    df = data.copy()

    for col in df.columns:
        if df[col].isnull().any():
           df[col].fillna(df[col].mean(), inplace=True)

    return df
def count_duplicates(data):
    total_duplicates = data.duplicated().sum()
    print(f"Количество полностью совпадающих строк: {total_duplicates}")
 