# Игра угадай число
import random

# Компьютер загадывает число
comp_num = random.randint(1, 100)

# print(comp_num)

#Создаем переменную пользовательского числа
hum_num = None

# Задаем уровни сложности
difficulties = (1, 4, 10, 20)
difficult = -1
while difficult < 0 or difficult > 3:
    difficult = int(input("Выберите уровень сложности от 0 до 3: "))
else:
    pass
max_count = difficulties[difficult]
#Запускаем цикл угадывания числа

for i in range(max_count):
    print("Попытка №: ", i + 1)
    hum_num = int(input("Введите число от 1 до 100: "))
    if hum_num == comp_num:
        print("Вау! Вы угадали")
        print("Уложились в", i + 1, "попыток")
        break
    elif hum_num > comp_num:
        print("Число больше, чем должно быть")
    else:
        print("Число меньше")
    if i == max_count - 1:
        print("Вы проиграли")
"""while hum_num != comp_num and i <= difficult:
    hum_num = int(input("Введите число от 1 до 100: "))
    i += 1
    if hum_num > comp_num:
        print("Должно быть число меньше")
    elif hum_num < comp_num:
        print ("Число должно быть больше")
    else:
        pass

else:
    pass
"""

