import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))
plt.pcolor(vals, cmap=plt.get_cmap('viridis', 11))
plt.colorbar(orientation='horizontal',
    shrink=0.9, extend='max', extendfrac=0.2,
    extendrect=False, drawedges=False)

plt.show()
