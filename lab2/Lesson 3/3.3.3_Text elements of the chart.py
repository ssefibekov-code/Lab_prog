import matplotlib.pyplot as plt

plt.subplot(121)
plt.title('Пример 1', fontsize=15)
plt.text(0, 7, 'HELLO!', fontsize=15)
plt.plot(range(0,10), range(0,10))

plt.subplot(122)
plt.title('Пример 1', fontsize=15)
bbox_properties=dict(boxstyle='darrow, pad=0.3', ec='k', fc='y', ls='-',
lw=3)
plt.text(2, 7, 'HELLO!', fontsize=15, bbox=bbox_properties)
plt.plot(range(0,10), range(0,10))

plt.show()
