import matplotlib.pyplot as plt
import math

x = list(range(-5, 6))
y = [i**2 for i in x]

plt.annotate('min', xy=(0, 0), xycoords='data', xytext=(0, 10),
textcoords='data', arrowprops=dict(facecolor='g'))
plt.plot(x, y)

plt.show()
