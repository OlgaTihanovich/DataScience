# Загрузка датасета
import pandas as pd

#Функция для создания DataFrame
def load_data(dataset):

  df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
  df['class_sp'] = pd.Categorical.from_codes(dataset.target,dataset.target_names)
  
  num_rows=df.shape[0]
  num_columns=df.shape[1]

  if num_rows>0:
    print(f"Загружено: {num_rows} строк, {num_columns} столбцов")
    df.info()
    return df
  else:
    print("Датасет не загрузился")