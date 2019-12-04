# coding=utf-8
# Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, 
# прочитать из них информацию. И получить объект: словарь из предыдущего задания.
 
import json
import pickle

with open('group.pickle', 'rb') as f:
    my_favourite_group = pickle.load(f)

print(my_favourite_group)
print(type(my_favourite_group))
my_favourite_group = ""

print(my_favourite_group)

with open('group.json', 'r', encoding='utf-8') as f:
    my_favourite_group = json.load(f)

print(my_favourite_group)
print(type(my_favourite_group))
