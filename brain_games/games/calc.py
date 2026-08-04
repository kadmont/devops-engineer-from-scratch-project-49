# Логика игры "Калькулятор"

import random  # NOSONAR

DESCRIPTION = "What is the result of the expression?"


# формирует строку вопроса и строку с правильным ответом
def generate_round():
    # случайный оператор
    operator = random.choice(['+', '-', '*'])  # NOSONAR
    # случайные числа
    num1 = random.randint(1, 10)  # NOSONAR
    num2 = random.randint(1, 10)  # NOSONAR

    # вычисление правильного ответа
    match operator:
        case '+':
            correct = num1 + num2
        case '-':
            correct = num1 - num2
        case '*':
            correct = num1 * num2

    question = f"{num1} {operator} {num2}"
    # Сравнение со строкой str
    return question, str(correct)