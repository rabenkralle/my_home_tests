# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def human(name, age, city):
    print(name + ", ", age, "год(а), ", "проживает в городе", city)

human("Дмитрий", 22, "Санкт-Петербург")