#!/usr/bin/env python
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

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

#СТОЛ
table_code = goods["Стол"]
table_item_1 = store[table_code][0]
table_quantity_1 = table_item_1["quantity"]
table_price_1 = table_item_1["price"]
table_full_price_1 = table_quantity_1 * table_price_1

table_item_2 = store[table_code][1]
table_quantity_2 = table_item_2["quantity"]
table_price_2 = table_item_2["price"]
table_full_price_2 = table_quantity_2 * table_price_2

table_full_quantity = (table_quantity_1 + table_quantity_2)
table_full_cost = (table_full_price_1 + table_full_price_2)

print('Стол -', table_full_quantity, 'шт, стоимость', table_full_cost, 'руб')

#ДИВАН
sofa = goods["Диван"]
sofa_store_1 = store[sofa][0]
sofa_quantity_1 = sofa_store_1["quantity"]
sofa_price_1 = sofa_store_1["price"]
sofa_full_price_1 = (sofa_quantity_1 * sofa_price_1)

sofa_store_2 = store[sofa][1]
sofa_quantity_2 = sofa_store_2["quantity"]
sofa_price_2 = sofa_store_2["price"]
sofa_full_price_2 = (sofa_quantity_2 * sofa_price_2)

full_quantity = (sofa_quantity_1 + sofa_quantity_2)
super_full_price = (sofa_full_price_1 + sofa_full_price_2)

print("Диван - ",full_quantity,"шт,", "стоимость ", super_full_price, "руб")

#СТУЛ
Chair_price_1 = store[goods["Стул"]][0]["quantity"] * store[goods["Стул"]][0]["price"]
Chair_price_2 = store[goods["Стул"]][1]["quantity"] * store[goods["Стул"]][1]["price"]
Chair_price_3 = store[goods["Стул"]][2]["quantity"] * store[goods["Стул"]][2]["price"]
Chair_quantity_1 = store[goods["Стул"]][0]["quantity"]
Chair_quantity_2 = store[goods["Стул"]][1]["quantity"]
Chair_quantity_3 = store[goods["Стул"]][2]["quantity"]

Chair_full_quantity = (Chair_quantity_1 + Chair_quantity_2 + Chair_quantity_3)
Chair_full_price = (Chair_price_1 + Chair_price_2 + Chair_price_3)

print("Стул - ", Chair_full_quantity, "шт,", "стоимость", Chair_full_price, "руб")


##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






