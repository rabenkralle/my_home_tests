# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dev(num1, num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print('Деление на ноль невозможно')
        
def ask_number(question):
    number = int(input(question))
    return number

num1 = ask_number('Введите число 1: ')
num2 = ask_number('Введите число 2: ')

dev(num1, num2)