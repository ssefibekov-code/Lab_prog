import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

bbox_properties=dict(
    boxstyle='rarrow, pad=0.3',
    ec='g',
    fc='r',
    ls='-',
    lw=3
)
plt.title('Title', fontsize=17, bbox=bbox_properties, position=(0.5,
0.85))
plt.plot(range(0,10), range(0,10))

plt.show()
