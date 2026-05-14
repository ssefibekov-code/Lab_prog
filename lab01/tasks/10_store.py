#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Лампа
lamp_code = goods['Лампа']
lamp_quantity = store[lamp_code][0]['quantity']
lamp_price = store[lamp_code][0]['price']
lamp_cost = lamp_quantity * lamp_price

# Стол
table_code = goods['Стол']
table_quantity = store[table_code][0]['quantity'] + store[table_code][1]['quantity']
table_cost = (store[table_code][0]['quantity'] * store[table_code][0]['price'] + 
              store[table_code][1]['quantity'] * store[table_code][1]['price'])

# Диван
sofa_code = goods['Диван']
sofa_quantity = store[sofa_code][0]['quantity'] + store[sofa_code][1]['quantity']
sofa_cost = (store[sofa_code][0]['quantity'] * store[sofa_code][0]['price'] + 
             store[sofa_code][1]['quantity'] * store[sofa_code][1]['price'])

# Стул
chair_code = goods['Стул']
chair_quantity = (store[chair_code][0]['quantity'] + 
                  store[chair_code][1]['quantity'] + 
                  store[chair_code][2]['quantity'])
chair_cost = (store[chair_code][0]['quantity'] * store[chair_code][0]['price'] + 
              store[chair_code][1]['quantity'] * store[chair_code][1]['price'] +
              store[chair_code][2]['quantity'] * store[chair_code][2]['price'])


def run():
    """Функция для запуска задания из верхнеуровневого модуля"""
    print(f"Лампа - {lamp_quantity} шт, стоимость {lamp_cost} руб")
    print(f"Стол - {table_quantity} шт, стоимость {table_cost} руб")
    print(f"Диван - {sofa_quantity} шт, стоимость {sofa_cost} руб")
    print(f"Стул - {chair_quantity} шт, стоимость {chair_cost} руб")


if __name__ == "__main__":
    run()