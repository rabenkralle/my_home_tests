# Создайте модуль. В нем создайте функцию, которая принимает список и
# возвращает из него случайный элемент. Если список пустой функция должна вернуть None.
# Проверьте работу функций в этом же модуле.

import random


def list_choice(list):
    response = None
    if list == []:
        pass
    else:
        response = random.choice(list)
    return response






