#5
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('BTC_data.csv')
df['time'] = pd.to_datetime(df['time'])

plt.figure(figsize=(14, 8))
plt.title('Значения цены биткоина на бирже с 2018 по 2023 год', fontsize=18)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Цена закрытия', fontsize=12)
plt.plot(df['time'], df['close'])

plt.grid()
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%y'))
plt.show()