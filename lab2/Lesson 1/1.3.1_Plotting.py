import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = x

plt.title('Линейная зависимость y = x')          # заголовок
plt.xlabel('x')                                  # ось абсцисс
plt.ylabel('y')                                  # ось ординат
plt.grid()                                       # включение отображение сетки
plt.plot(x, y, 'r--')                            # построение графика
plt.show()