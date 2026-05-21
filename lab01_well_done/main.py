#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Верхнеуровневый модуль для лабораторной работы №1
Инкапсулирует логику всех заданий и предоставляет единый интерфейс
"""

import sys
import os
import importlib.util

# Добавляем текущую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def import_task(file_name):
    """
    Динамически импортирует модуль из папки tasks
    """
    tasks_dir = os.path.join(os.path.dirname(__file__), 'tasks')
    file_path = os.path.join(tasks_dir, file_name)
    
    # Создаем имя модуля без расширения
    module_name = file_name.replace('.py', '')
    
    # Динамический импорт
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return module


# Импортируем все модули заданий
task00 = import_task('00_distance.py')
task01 = import_task('01_circle.py')
task02 = import_task('02_operations.py')
task03 = import_task('03_favorite_movies.py')
task04 = import_task('04_my_family.py')
task05 = import_task('05_zoo.py')
task06 = import_task('06_songs_list.py')
task07 = import_task('07_secret.py')
task08 = import_task('08_garden.py')
task09 = import_task('09_shopping.py')
task10 = import_task('10_store.py')


def print_header(title):
    """Выводит красивый заголовок"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def run_all_tasks():
    """Запускает все задания последовательно"""
    tasks = [
        ("00_distance.py - Расстояния между городами", task00.run),
        ("01_circle.py - Площадь круга и точки", task01.run),
        ("02_operations.py - Арифметическая головоломка", task02.run),
        ("03_favorite_movies.py - Фильмы (срезы строк)", task03.run),
        ("04_my_family.py - Семья и рост", task04.run),
        ("05_zoo.py - Зоопарк", task05.run),
        ("06_songs_list.py - Песни Depeche Mode", task06.run),
        ("07_secret.py - Расшифровка сообщения", task07.run),
        ("08_garden.py - Цветы (множества)", task08.run),
        ("09_shopping.py - Магазины и сладости", task09.run),
        ("10_store.py - Склад товаров", task10.run),
    ]
    
    for title, task_func in tasks:
        print_header(title)
        task_func()
    
    print_header("ВСЕ ЗАДАНИЯ УСПЕШНО ВЫПОЛНЕНЫ!")


def show_menu():
    """Показывает интерактивное меню"""
    while True:
        print("\n" + "=" * 70)
        print(" ЛАБОРАТОРНАЯ РАБОТА №1 - ВЕРХНЕУРОВНЕВЫЙ МОДУЛЬ")
        print("=" * 70)
        print("\nВыберите задание для выполнения:\n")
        print("   00 - 00_distance.py - Расстояния между городами")
        print("   01 - 01_circle.py - Площадь круга и точки")
        print("   02 - 02_operations.py - Арифметическая головоломка")
        print("   03 - 03_favorite_movies.py - Фильмы (срезы строк)")
        print("   04 - 04_my_family.py - Семья и рост")
        print("   05 - 05_zoo.py - Зоопарк")
        print("   06 - 06_songs_list.py - Песни Depeche Mode")
        print("   07 - 07_secret.py - Расшифровка сообщения")
        print("   08 - 08_garden.py - Цветы (множества)")
        print("   09 - 09_shopping.py - Магазины и сладости")
        print("   10 - 10_store.py - Склад товаров")
        print("   ----")
        print("   a  - Выполнить ВСЕ задания")
        print("   q  - Выход")
        print("-" * 70)
        
        choice = input("Ваш выбор: ").strip().lower()
        
        if choice == 'q':
            print("\nДо свидания!")
            break
        elif choice == 'a':
            run_all_tasks()
        elif choice == '00':
            print_header("00_distance.py - Расстояния между городами")
            task00.run()
        elif choice == '01':
            print_header("01_circle.py - Площадь круга и точки")
            task01.run()
        elif choice == '02':
            print_header("02_operations.py - Арифметическая головоломка")
            task02.run()
        elif choice == '03':
            print_header("03_favorite_movies.py - Фильмы (срезы строк)")
            task03.run()
        elif choice == '04':
            print_header("04_my_family.py - Семья и рост")
            task04.run()
        elif choice == '05':
            print_header("05_zoo.py - Зоопарк")
            task05.run()
        elif choice == '06':
            print_header("06_songs_list.py - Песни Depeche Mode")
            task06.run()
        elif choice == '07':
            print_header("07_secret.py - Расшифровка сообщения")
            task07.run()
        elif choice == '08':
            print_header("08_garden.py - Цветы (множества)")
            task08.run()
        elif choice == '09':
            print_header("09_shopping.py - Магазины и сладости")
            task09.run()
        elif choice == '10':
            print_header("10_store.py - Склад товаров")
            task10.run()
        else:
            print("\n❌ Неверный выбор! Пожалуйста, введите 00-10, 'a' или 'q'.")
        
        if choice != 'q':
            input("\nНажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    show_menu()