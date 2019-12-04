# Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.
#
# Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

import random

rnd_list = [random.randint(-100, 100) for i in range(1,20)]
print(rnd_list)

dev_3 = [number for number in rnd_list if number%3 == 0]
print(dev_3)

plus_list = [number for number in rnd_list if number > 0]
print(plus_list)

not_dev_4 = [number for number in rnd_list if number%4 != 0]
print(not_dev_4)