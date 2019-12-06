# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо 
# числа вводится специальный символ, выполнение программы завершается. 
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к 
# полученной ранее сумме и после этого завершить программу.

# def s_filter(numbers):


def sum_str(numbers):
    numbers = list(numbers.split(' '))
    list_number = list(filter(lambda x: x != ' ' and x != 's', numbers))
    result = sum(list(map(lambda x: int(x), list_number)))
    return result



    
    
numbers = input('numbers: ')
sum_num = sum_str(numbers)
print(sum_num)
sum_res = sum_num
while numbers != 's':
    numbers = input('numbers: ')
    sum_num = sum_str(numbers)
    sum_res += sum_num
    print(sum_num)
    print(sum_res)
else:
    print('конец программы')