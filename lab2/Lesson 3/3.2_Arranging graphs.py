import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = [1, 2, 3, 4, 5]
y1 = [9, 4, 2, 4, 9]
y2 = [1, 7, 6, 3, 5]
y3 = [-7, -4, 2, -4, -7]

fg = plt.figure(figsize=(7, 3), constrained_layout=True)
gs = gridspec.GridSpec(ncols=2, nrows=1, figure=fg)

fig_ax_1 = fg.add_subplot(gs[0, 0])
plt.plot(x, y1)

fig_ax_2 = fg.add_subplot(gs[0, 1])
plt.plot(x, y2)

plt.show()
