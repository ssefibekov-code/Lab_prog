import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = [1, 2, 3, 4, 5]
y1 = [9, 4, 2, 4, 9]
y2 = [1, 7, 6, 3, 5]
y3 = [-7, -4, 2, -4, -7]

fg = plt.figure(figsize=(5, 5),constrained_layout=True)

widths = [1, 3]
heights = [2, 0.7]

gs = fg.add_gridspec(ncols=2, nrows=2, width_ratios=widths,
height_ratios=heights)

fig_ax_1 = fg.add_subplot(gs[0, 0])
fig_ax_1.set_title('w:1, h:2')

fig_ax_2 = fg.add_subplot(gs[0, 1])
fig_ax_2.set_title('w:3, h:2')

fig_ax_3 = fg.add_subplot(gs[1, 0])
fig_ax_3.set_title('w:1, h:0.7')

fig_ax_4 = fg.add_subplot(gs[1, 1])
fig_ax_4.set_title('w:3, h:0.7')

plt.show()
