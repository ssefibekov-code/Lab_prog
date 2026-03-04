#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код

'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
# 'Терминатор'
# 'Назад в будущее'
# 'Пятый элемент'
# 'Чужие'

first_movie = my_favorite_movies[:10]  # первый фильм
print(first_movie)

last_movie = my_favorite_movies[-15:]  # последний
print(last_movie)

second_movie = my_favorite_movies[12:25]  # второй
print(second_movie)

last_second_movie = my_favorite_movies[-22:-17]  # последний
print(last_second_movie)
