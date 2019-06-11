import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
data_set = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(data_set, 50, normed=1, facecolor='m', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of ID')
plt.text(60, 0.25, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
