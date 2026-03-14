import matplotlib.pyplot as plt
import numpy as np

#Цветовое распределение
np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))
plt.pcolor(vals)

#colorbar
np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))
plt.pcolor(vals)
plt.colorbar()

#Colorbar с дискретным разделением цветов
np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))
plt.pcolor(vals, cmap=plt.get_cmap('viridis', 11) )
plt.colorbar()

plt.show()
