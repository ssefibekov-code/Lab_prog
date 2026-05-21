#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Время трех песен из списка
halo_time = 0
enjoy_time = 0
clean_time = 0

for song in violator_songs_list:
    if song[0] == 'Halo':
        halo_time = song[1]
    elif song[0] == 'Enjoy the Silence':
        enjoy_time = song[1]
    elif song[0] == 'Clean':
        clean_time = song[1]

total_time = halo_time + enjoy_time + clean_time
total_time_rounded = round(total_time, 2)

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# Время трех песен из словаря
sweetest_time = violator_songs_dict['Sweetest Perfection']
policy_time = violator_songs_dict['Policy of Truth']
blue_dress_time = violator_songs_dict['Blue Dress']

other_total = sweetest_time + policy_time + blue_dress_time
other_total_rounded = round(other_total, 2)


def run():
    """Функция для запуска задания из верхнеуровневого модуля"""
    print(f"Три песни (Halo, Enjoy the Silence, Clean) звучат {total_time_rounded} минут")
    print(f"Другие три песни (Sweetest Perfection, Policy of Truth, Blue Dress) звучат {other_total_rounded} минут")


if __name__ == "__main__":
    run()