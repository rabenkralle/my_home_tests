# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# Примечание: Списки фруктов создайте вручную в начале файла

fruits_1 = ['apple', 'orange', 'pineapple', 'cherry']
fruits_2 = ['orange', 'melon', 'grape', 'apple']

print([fruit for fruit in fruits_1 if fruit in fruits_2])