# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def max_number(number_1, number_2, number_3):
    # Ищем максимальное число из трех
    numbers = [number_1, number_2, number_3]
    big = max(numbers)
    return big

def ask_number():
    number = int(input("Введите число: "))
    return number

# Запрашиваем три числа
num_1 = ask_number()
num_2 = ask_number()
num_3 = ask_number()

big = max_number(num_1, num_2, num_3)
print(big)

