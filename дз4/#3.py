#3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize = (12, 10))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

df = pd.read_csv('iris_data.csv')

species = df['Species'].unique()

x1 = sum(df['PetalLengthCm'] <= 1.2)
x2 = sum((df['PetalLengthCm'] > 1.2) & (df['PetalLengthCm'] <= 1.5))
x3 = sum(df['PetalLengthCm'] > 1.5)


ax1.pie([x1, x2, x3], labels = ['<= 1.2 см', '1.2 - 1.5 см', ' > 1.5 см'])
ax2.pie([list(df['Species']).count(i) for i in species], labels = species)
plt.show()
