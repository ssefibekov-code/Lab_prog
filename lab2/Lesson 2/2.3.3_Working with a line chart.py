import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
plt.plot(x, y1, 'ro')
plt.plot(x, y2, 'bx')
plt.show()