import matplotlib.pyplot as plt

plt.figure(figsize=(7,5))

arrows = ['-', '->', '-[', '|-|', '-|>', '<-', '<->', '<|-', '<|-|>',
'fancy', 'simple', 'wedge']

bbox_properties=dict(
    boxstyle='round,pad=0.2',
    ec='k',
    fc='w',
    ls='-',
    lw=1
)
ofs_x = 0
ofs_y = 0

for i, ar in enumerate(arrows):
    if i == 6: ofs_x = 0.5
    plt.annotate(ar, xy=(0.4+ofs_x, 0.92-ofs_y), xycoords='data',
        xytext=(0.05+ofs_x, 0.9-ofs_y), textcoords='data', fontsize=17,
        bbox=bbox_properties,
        arrowprops=dict(arrowstyle=ar)
        )
    if ofs_y == 0.75: ofs_y = 0
    else: ofs_y += 0.15

plt.show()
