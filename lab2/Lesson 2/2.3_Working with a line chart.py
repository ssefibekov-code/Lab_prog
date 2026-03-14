import matplotlib.pyplot as plt

#Вариант 1:
x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, '--')                                    

#Вариант 2:
line = plt.plot(x, y)
plt.setp(line, linestyle='--')

plt.show()   