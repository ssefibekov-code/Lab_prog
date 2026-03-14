import matplotlib.pyplot as plt


weight=['light', 'regular', 'bold']
plt.figure(figsize=(12, 4))

for i, lc in enumerate(['left', 'center', 'right']):
    plt.subplot(1, 3, i+1)
    plt.title(label=lc, loc=lc, fontsize=12+i*5, fontweight=weight[i],
pad=10+i*15)
 
plt.show()