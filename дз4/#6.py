#6
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('BTC_data.csv')
df['time'] = pd.to_datetime(df['time'])

df['t'] = (df['time'] - min(df['time']))
df['t'] = (df['t']).dt.days


plt.figure(figsize=(14, 8))

mnk = np.polyfit(df['t'], df['close'], 2)
z = np.poly1d(mnk)

plt.title('Значения цены биткоина на бирже с 2018 по 2023 год', fontsize=18)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Цена закрытия', fontsize=12)
plt.plot(df['time'], df['close'])
x_range = np.linspace(min(df['t']), max(df['t']), 100)
plt.plot(min(df['time']) + pd.to_timedelta(x_range, unit='d'), z(x_range), linewidth=2, label = 'Апромаксимация цены биткоина полиномом 2 степени')
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%y'))
plt.legend(fontsize=11)

plt.show()
