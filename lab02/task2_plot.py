#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y1 = x ** 2
y2 = x ** 3
y3 = np.exp(x)
y4 = np.log(np.abs(x) + 0.1)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y1, 'g-', linewidth=2)
axes[0, 0].set_title('y = x²')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(x, y2, 'r-', linewidth=2)
axes[0, 1].set_title('y = x³')
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].plot(x, y3, 'b-', linewidth=2)
axes[1, 0].set_title('y = e^x')
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].plot(x, y4, 'm-', linewidth=2)
axes[1, 1].set_title('y = ln(|x| + 0.1)')
axes[1, 1].grid(True, alpha=0.3)

fig.suptitle('Графики элементарных функций', fontsize=16)
plt.tight_layout()

plt.savefig('images/task2_plot.png', dpi=150, bbox_inches='tight')
plt.show()