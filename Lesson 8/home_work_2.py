# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def max_number(number_1, number_2, number_3):
    # Ищем максимальное число из трех
    result = max([number_1, number_2, number_3])
    return result

def ask_number():
    number = int(input("Введите число: "))
    return number

# Запрашиваем три числа
num_1 = ask_number()
num_2 = ask_number()
num_3 = ask_number()

result = max_number(num_1, num_2, num_3)
print(result)

