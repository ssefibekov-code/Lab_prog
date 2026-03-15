import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

np.random.seed(123)
vals = np.random.randint(11, size=(7, 7))
fig, ax = plt.subplots()
gr = ax.pcolor(vals)
axins = inset_axes(ax, width="7%", height="50%", loc='lower left',
bbox_to_anchor=(1.05, 0., 0.2, 1), bbox_transform=ax.transAxes,
borderpad=-0.5)
plt.colorbar(gr, cax=axins, ticks=[0, 5, 10], label='Value')

plt.show()
