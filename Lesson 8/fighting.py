"""Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать
функцию attack(person1, person2).
Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
Функция должна сама работать со словарями и изменять их значения."""


# Запрашиваем имя игрока
def ask_name(question):
    name = ""
    while name == "":
        name = input(question)
    return name

# Определеяем характеристики игрока
def player(health, damage):
    name = ask_name("Введите имя игрока: ")
    player_stat = {"name": name, "health": health, "damage": damage}
    return player_stat

# Определяем характеристики врага
def enemy(health, damage):
    name = ask_name("Введите имя врага: ")
    enemy_stat = {"name": name, "health": health, "damage": damage}
    return enemy_stat

# Описываем функцию атаки
def attack(person1, person2):
    health = person2["health"]
    damage = person1["damage"]
    while health != 0:
        health -= damage
        break
    else:
        print("Герой мертв")
    person2["health"] = health
    return person1

# Основная часть программы
def main():
    human_player = player(100, 30)
    print(human_player)
    human_enemy = enemy(50, 50)
    print(human_enemy)
    attack(human_player, human_enemy)
    print(human_player)
    print(human_enemy)

main()