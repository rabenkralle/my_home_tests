# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

from mk_folder import make_folder
from del_folder import del_folder
import rand_list
mk_or_del = None

# del_folder()
while mk_or_del != "n":
    mk_or_del = input("Хотите создать папки или удалить (dir_1 to 9)? (y/n/del): ")
    if mk_or_del.lower() == "y":
        make_folder()
    elif mk_or_del.lower() == "del":
        del_folder()
    elif mk_or_del == "n":
        break
    else:
        print("Нет такого варианта")

mk_or_del = None

list = [10, 20, 1, 90, 80, 100, 67, 55]

while mk_or_del != "n":
    mk_or_del = input("Хотите выбрать случайным элемент из списка? (y/n): ")
    if mk_or_del.lower() == "y":
        print(rand_list.list_choice(list))
    elif mk_or_del.lower() == "n":
        pass
    else:
        print("Нет такого варианта")

