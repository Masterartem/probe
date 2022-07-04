#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family = ["Father", "Mother", "Sister", "Brother"]

# список списков приблизителного роста членов вашей семьи
Father = 180
Mother_height = Mother = 170
Sister_height = Sister = 160
Brother_height = Brother = 150
my_family_height = [
    # ['имя', рост],
    ["Father", Father], ["Mother",Mother_height], ["Sister", Sister_height], ["Brother", Brother_height]
]

print("Father height - ", my_family_height[0][1], "cm")
print("Family height = ", Father + Mother + Sister + Brother, "cm")
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
