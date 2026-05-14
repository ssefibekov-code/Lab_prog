#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y_cos, label='cos(x)', color='red', linewidth=2)

plt.title('Графики функций sin(x) и cos(x)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', fontsize=10)

plt.savefig('images/task1_plot.png', dpi=150, bbox_inches='tight')
plt.show()