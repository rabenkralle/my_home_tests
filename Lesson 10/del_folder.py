# Удаляем папки
import os

def del_folder():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(),"{}_{}".format("dir", i))
        os.removedirs(new_path)

