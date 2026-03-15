import matplotlib.pyplot as plt
import numpy as np

fruits = ['aple', 'peach', 'orege', 'bannana', 'melon']
counts = [34, 25, 43, 31, 17]
plt.bar(fruits, counts)
plt.title('Fruits!')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
