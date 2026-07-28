import random  # NOSONAR - safe for game logic

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    # Проверяет, является ли число чётным (предикат).
    return number % 2 == 0


def generate_round():
    # Генерирует вопрос и правильный ответ для одного раунда.
    number = random.randint(1, 100)  # NOSONAR
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer