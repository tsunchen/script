import numpy as np
import matplotlib.pyplot as plt


CMBChina_int_001 = [2.8,3,3.1,3.2,3.4,3.5,3.6,3.65,3.7]
CMBChina_day_001 = [7,14,21,31,61,91,181,365,9999]

first_figure = plt.figure("First Figure")

subplot1 = first_figure.add_subplot(2,3,1)
plt.plot(np.random.rand(50).cumsum(), 'k--')
subplot1 = first_figure.add_subplot(2,3,6)
plt.plot(CMBChina_day_001, 'k--')

plt.show()

#plt.xlabel('Smarts')
#plt.ylabel('Probability')
#plt.title('Histogram of ID')
#plt.text(60, 0.25, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)
#plt.show()
