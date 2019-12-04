# Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13,
# функция поднимает исключительную ситуации ValueError иначе возвращает введенное число,
# возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число. Введенное число передаем
# параметром в написанную функцию и печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации,
# которая поднимается внутри функции.


def excep(question):

    number = int(input(question))
    if number > 1 or number < 100:
        if number == 13:
            raise ValueError("Число 13!!!")
        else:
            number = number ** 2
            return number



try:
    number = excep("Введите число: ")
    print(number)
except Exception:\
    print('Что-то пошло не так')