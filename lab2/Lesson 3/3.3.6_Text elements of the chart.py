import matplotlib.pyplot as plt
import math

fig, axs = plt.subplots(2, 3, figsize=(12, 7))
conn_style=[
    'angle,angleA=90,angleB=0,rad=0.0',
    'angle3,angleA=90,angleB=0',
    'arc,angleA=0,angleB=0,armA=0,armB=40,rad=0.0',
    'arc3,rad=-1.0',
    'bar,armA=0.0,armB=0.0,fraction=0.1,angle=70',
    'bar,fraction=-0.5,angle=180',
]
for i in range(2):
    for j in range(3):
        axs[i, j].text(0.1, 0.5, '\n'.join(conn_style[i*3+j].split(',')))
        axs[i, j].annotate('text', xy=(0.2, 0.2), xycoords='data',
            xytext=(0.7, 0.8), textcoords='data',
            arrowprops=dict(arrowstyle='->',
connectionstyle=conn_style[i*3+j]))

plt.show()
