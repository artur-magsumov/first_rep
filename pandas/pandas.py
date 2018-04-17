##matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

fixed_df = pd.read_csv('csv_table.csv',  # Это то, куда вы скачали файл
                       sep=';', encoding='utf-8',
                       parse_dates=['data'], index_col='data')
fixed_df[:]
