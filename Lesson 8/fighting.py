"""Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать
функцию attack(person1, person2).
Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
Функция должна сама работать со словарями и изменять их значения.

Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.
"""


# Запрашиваем имя игрока
def ask_name(question):
    name = ""
    while name == "":
        name = input(question)
    return name

# Определеяем характеристики игрока
def player(health, damage, armor):
    name = ask_name("Введите имя игрока: ")
    player_stat = {"name": name, "health": health, "damage": damage, "armor": armor}
    return player_stat

# Определяем характеристики врага
def enemy(health, damage, armor):
    name = ask_name("Введите имя врага: ")
    enemy_stat = {"name": name, "health": health, "damage": damage, "armor": armor}
    return enemy_stat

def get_damage(damage, armor):
    return damage/armor

# Описываем функцию атаки
def attack(person1, person2):
    damage = get_damage(person1["damage"], person2["armor"])
    while person2["health"] != 0:
        person2["health"] -= damage
        break
    else:
        print("Герой мертв")
    return person1

# Основная часть программы
def main():
    human_player = player(100, 40, 1.2)
    print(human_player)
    human_enemy = enemy(50, 50, 3)
    print(human_enemy)
    attack(human_player, human_enemy)
    print(human_player)
    print(human_enemy)

main()