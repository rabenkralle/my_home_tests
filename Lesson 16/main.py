import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_folder
import random_number_comp, random_number

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Не указана команда')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не указано имя файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не указано имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не указано имя файла или папки')
        else:
            delete_file(name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не указано имя файла или папки')
        else:
            change_folder(name)
    elif command == 'compgame':
        try:
            random_number_comp.main()
        except ValueError:
            print('Неправильное значение')
    elif command == 'game':
        try:
            random_number.game()
        except ValueError:
            print('Неправильное значение')
    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не указано имя файла или папки')
        else:
            try:
                new_name = sys.argv[3]
            except IndexError:
                print('Не указано новое имя файла или папки')
            else:
                copy_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('ch - смена директории')

save_info('Конец')