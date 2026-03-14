import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [i*2 for i in range(10)]

plt.subplot(231)
plt.title('Пример 1', fontsize=15)
plt.plot(x, y)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

plt.subplot(233)
plt.title('Пример 2', fontsize=15)
plt.plot(x, y)
plt.xlabel('Ось X\nНезависимая величина', fontsize=14, fontweight='bold')
plt.ylabel('Ось Y\nЗависимая величина', fontsize=14, fontweight='bold')

plt.show()
