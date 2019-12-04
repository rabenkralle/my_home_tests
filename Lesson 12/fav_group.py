# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
#
#  С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
#  вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно.
#  В файле group.json указать кодировку utf-8.

import json
import pickle

my_favourite_group = {
    'name': 'Marillion',
    'tracks': ['Grendel', 'Cinderella Search', 'Childhoods End'],
    'albums': [{'name': 'Fugazi', 'year': '1984 год'},
               {'name': 'Misplaced Childhood', 'year': '1985 год'}]
}

print(my_favourite_group)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

print('Объект pickle записан')

with open('group.json', 'w', encoding = 'utf-8') as f:
    json.dump(my_favourite_group, f)
    
print('Объект json записан')