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
    tries = 10
    human_number = ask_human_number("Загадайте число", LOW, HIGH)
    cpu_number = random.randint(LOW, HIGH)
    print(cpu_number)
    guess_number = 0
    for i in range(tries):
        if cpu_number > human_number:
            cpu_number = random.randint(human_number, guess_number)
        elif cpu_number < human_number:
            cpu_number = random.randint(guess_number, human_number)



