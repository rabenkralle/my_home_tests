# Создаем папки
import os

def make_folder():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)

def del_folder():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.removedirs(folder_name)
