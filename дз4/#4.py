#4
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize = (15, 15))
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)

df = pd.read_csv('iris_data.csv')

x_SepalLength = list(df['SepalLengthCm'])
x_SepalWidth = list(df['SepalWidthCm'])
x_PetalLength = list(df['PetalLengthCm'])
x_PetalWidth = list(df['PetalWidthCm'])

ax1.scatter(x_SepalWidth, x_SepalLength)
ax2.scatter(x_SepalWidth, x_PetalLength)
ax3.scatter(x_SepalWidth, x_PetalWidth)
ax4.scatter(x_SepalLength, x_PetalLength)
ax5.scatter(x_SepalLength, x_PetalWidth)
ax6.scatter(x_PetalLength, x_PetalWidth)

mnk1 = np.polyfit(x_SepalWidth, x_SepalLength, 1) 
mnk2 = np.polyfit(x_SepalWidth, x_PetalLength, 1) 
mnk3 = np.polyfit(x_SepalWidth, x_PetalWidth, 1) 
mnk4 = np.polyfit(x_SepalLength, x_PetalLength, 1) 
mnk5 = np.polyfit(x_SepalLength, x_PetalWidth, 1) 
mnk6 = np.polyfit(x_PetalLength, x_PetalWidth, 1) 

z1 = np.poly1d(mnk1)
z2 = np.poly1d(mnk2)
z3 = np.poly1d(mnk3)
z4 = np.poly1d(mnk4)
z5 = np.poly1d(mnk5)
z6 = np.poly1d(mnk6)

x_uses1 = np.linspace(min(x_SepalWidth), max(x_SepalWidth), 100)
x_uses2 = np.linspace(min(x_SepalWidth), max(x_SepalWidth), 100)
x_uses3 = np.linspace(min(x_SepalWidth), max(x_SepalWidth), 100)
x_uses4 = np.linspace(min(x_SepalLength), max(x_SepalLength), 100)
x_uses5 = np.linspace(min(x_SepalLength), max(x_SepalLength), 100)
x_uses6 = np.linspace(min(x_PetalLength), max(x_PetalLength), 100)

ax1.plot(x_uses1, z1(x_uses1), 'r-', linewidth=2)
ax2.plot(x_uses2, z2(x_uses2), 'r-', linewidth=2)
ax3.plot(x_uses3, z3(x_uses3), 'r-', linewidth=2)
ax4.plot(x_uses4, z4(x_uses4), 'r-', linewidth=2)
ax5.plot(x_uses5, z5(x_uses5), 'r-', linewidth=2)
ax6.plot(x_uses6, z6(x_uses6), 'r-', linewidth=2)

ax1.set_xlabel('SepalWidth')
ax1.set_ylabel('SepalLength')
ax2.set_xlabel('SepalWidth')
ax2.set_ylabel('PetalLength')
ax3.set_xlabel('SepalWidth')
ax3.set_ylabel('PetalWidth')
ax4.set_xlabel('SepalLength')
ax4.set_ylabel('PetalLength')
ax5.set_xlabel('SepalLength')
ax5.set_ylabel('PetalWidth')
ax6.set_xlabel('PetalLength')
ax6.set_ylabel('PetalWidth')

print(mnk1, mnk2, mnk3, mnk4, mnk5, mnk6, sep = '\n')

plt.tight_layout()

plt.show()