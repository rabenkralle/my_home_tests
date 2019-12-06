# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    sum1 = num1 + num2
    sum2 = num2 + num3
    sum3 = num1 + num3
    
    result = max(sum1, sum2, sum3)
    print(result)

my_func(19,14,29)