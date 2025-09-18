#визуализация данных
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def heatmap_visual(df):
 
    corr_matrix = df.corr()

    plt.figure(figsize=(10, 10)) 
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm', 
        fmt='.2f' 
    )
    plt.title("Features Correlations", fontsize=16)
    plt.show()

def boxplot_visual(dataset):
  #Построение ящиков с усами
  sns.set(style="whitegrid")
  plt.figure(figsize=(12, 10))

  for index, column in enumerate(dataset.select_dtypes(include=[np.number]).columns):
    plt.subplot((len(dataset.columns) // 3) + 1, 3, index + 1)
    sns.boxplot(y=dataset[column])

  plt.tight_layout()
  plt.show()

def hist_visual(dataset):
  sns.set(style="whitegrid")

  # Создание гистограмм 
  dataset.hist(bins=20, figsize=(18, 12), color='green', edgecolor='black')

  # Добавление названий 
  for ax in plt.gcf().get_axes():
    ax.set_xlabel('Значение')
    ax.set_ylabel('Частота')
 
  # Регулировка макета
  plt.tight_layout()
  plt.show()