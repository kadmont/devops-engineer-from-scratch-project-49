# Логика игры "Арифметическая прогрессия"

import random  # NOSONAR - safe for game logic

DESCRIPTION = "What number is missing in the progression?"


def generate_round():
    length = random.randint(5, 10)  # NOSONAR
    start = random.randint(1, 50)  # NOSONAR
    step = random.randint(1, 10)  # NOSONAR
    hidden_index = random.randint(0, length - 1)  # NOSONAR

    # Генерация членов прогрессии по формуле start + i * step
    progression = [str(start + i * step) for i in range(length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    question = ' '.join(progression)
    return question, correct_answer