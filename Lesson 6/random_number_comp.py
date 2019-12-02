import random
# Вводим константы
LOW = 1
HIGH = 100

def ask_human_number(question, LOW, HIGH):
    # Пользователь загадывает число в диапазоне от 1 до 100
    response = None
    while response not in range(LOW, HIGH):
        response = int(input(question))
    return response

def main():
    tries = 0
    human_number = ask_human_number("Загадайте число", LOW, HIGH)
    cpu_number = random.randint(LOW, HIGH)
    print(cpu_number)
    guess_number = 0
    guess_low = 1
    guess_high = 100

    while cpu_number != human_number:
        human_help = input("Больше или меньше компьютерное число")
        guess_number = cpu_number
        tries += 1
        if tries == 10:
            print("Компьютер не справился")
            break
        if human_help == ">":
            guess_high = cpu_number
            cpu_number = random.randint(guess_low, guess_number)
            print(cpu_number)
        elif human_help == "<":
            guess_low = cpu_number
            cpu_number = random.randint(guess_number, guess_high)
            print(cpu_number)
        else:
            print("Такого нет варианта")
        if cpu_number == human_number:
            print("Компьютер угадал число", human_number, "и уложился в", tries,"попыток")


main()




