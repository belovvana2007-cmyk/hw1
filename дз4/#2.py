#2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

fig = plt.figure(figsize = (12, 10))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)


size1 = 200
size2 = 1000
size3 = 5000


values1 = np.random.normal(0, 1, size1)
values2 = np.random.normal(0, 1, size2)
values3 = np.random.normal(0, 1, size3)

ax1.hist(values1, bins = 50, density=True)
ax2.hist(values2, bins = 50, density=True)
ax3.hist(values3, bins = 50, density=True)

x = [-4 + i * (8 / 999) for i in range(1000)]
theoretical_pdf = norm.pdf(x, 0, 1)

ax1.plot(x, theoretical_pdf, linewidth=2)
ax2.plot(x, theoretical_pdf, linewidth=2)
ax3.plot(x, theoretical_pdf, linewidth=2)

ax1.set_title('Гистограмма для 200 точек')
ax2.set_title('Гистограмма для 1000 точек')
ax3.set_title('Гистограмма для 5000 точек')

plt.show()
