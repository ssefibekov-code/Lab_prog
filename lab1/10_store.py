#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

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

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']

table_code = goods['Стол']
table_item1 = store[table_code][0]
table_item2 = store[table_code][1]
table_quantity = table_item1['quantity'] + table_item2['quantity']
table_cost = table_item1['quantity'] * table_item1['price'] + table_item2['quantity'] * table_item2['price']
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')


sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']

sofa_code = goods['Диван']
sofa_item1 = store[sofa_code][0]
sofa_item2 = store[sofa_code][1]
sofa_quantity = sofa_item1['quantity'] + sofa_item2['quantity']
sofa_cost = sofa_item1['quantity'] * sofa_item1['price'] + sofa_item2['quantity'] * sofa_item2['price']
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')


chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']

chair_code = goods['Стул']
chair_item1 = store[chair_code][0]
chair_item2 = store[chair_code][1]
chair_item3 = store[chair_code][2]
chair_quantity = chair_item1['quantity'] + chair_item2['quantity'] + chair_item3['quantity']
chair_cost = chair_item1['quantity'] * chair_item1['price'] + chair_item2['quantity'] * chair_item2['price'] + chair_item3['quantity'] * chair_item3['price']
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
