import numpy as np
import matplotlib.pyplot as plt
import os

def f(x):
    if 0 <= x <= 1:
        return np.cos(x + x**3)
    elif 1 < x <= 2:
        return np.exp(-x**2) - x**2 + 2*x
    else:
        return np.nan

f_vec = np.vectorize(f)

x = np.linspace(0, 2, 1000)
y = f_vec(x)

x0 = 0.7
y0 = f(x0)

h = 0.001
df_x0 = (f(x0 + h) - f(x0)) / h

x_tangent = np.linspace(max(0, x0 - 0.3), min(2, x0 + 0.3), 100)
y_tangent = y0 + df_x0 * (x_tangent - x0)

plt.figure(figsize=(12, 8))

plt.plot(x, y, 'b-', linewidth=2, label='f(x)')

plt.plot(x_tangent, y_tangent, 'r--', linewidth=2, label='Касательная')

plt.plot(x0, y0, 'go', markersize=10, label=f'Точка касания')

plt.title('График функции и касательной', fontsize=16, fontweight='bold')
plt.xlabel('x', fontsize=14)
plt.ylabel('f(x)', fontsize=14)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')

plt.annotate(f'x₀ = {x0:.3f}\ny₀ = {y0:.3f}', 
             xy=(x0, y0), 
             xytext=(x0 + 0.2, y0 + 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             fontsize=11,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='black', alpha=0.9))

plt.tight_layout()
plt.savefig('graph_variant.png', dpi=300, bbox_inches='tight')
plt.show()