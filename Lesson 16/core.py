# coding=utf-8
# Функция для создания файла

import os
import shutil
import datetime

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')


def get_list(folders_only = False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        try:
            os.rmdir(name)
        except FileNotFoundError:
            print('Такой папки не существует')
    else:
        try:
            os.remove(name)
        except FileNotFoundError:
            print('Такого файла не существует')


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка с таким именем уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_folder(name):
    os.chdir(name)
    print(os.getcwd())

if __name__ == '__main__':
    create_file('test.dat', 'text')
    create_folder('new_f')
    get_list(True)
    # delete_file('new_f')
    # delete_file('test.dat')
    copy_file('new_f', 'new_f2')
    copy_file('test.dat', 'test2.dat')
    save_info('abc')