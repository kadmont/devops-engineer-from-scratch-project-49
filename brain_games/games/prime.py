# Логика игры "Простое ли число?"

import random  # NOSONAR - safe for game logic

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    # Check divisibility up to sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 100)  # NOSONAR
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer