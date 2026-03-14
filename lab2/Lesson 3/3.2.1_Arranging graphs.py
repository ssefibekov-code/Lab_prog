import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = [1, 2, 3, 4, 5]
y1 = [9, 4, 2, 4, 9]
y2 = [1, 7, 6, 3, 5]
y3 = [-7, -4, 2, -4, -7]

fg = plt.figure(figsize=(9, 4), constrained_layout=True)
gs = fg.add_gridspec(2, 2)

fig_ax_1 = fg.add_subplot(gs[0, :])
plt.plot(x, y2)

fig_ax_2 = fg.add_subplot(gs[1, 0])
plt.plot(x, y1)

fig_ax_3 = fg.add_subplot(gs[1, 1])
plt.plot(x, y3)

plt.show()
