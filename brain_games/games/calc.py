# Логика игры "Калькулятор"

# Импортируем модуль для генерации случайных чисел
import random  # NOSONAR

# Описание игры, которое будет показано пользователю
DESCRIPTION = "What is the result of the expression?"


# Функция, которая генерирует один раунд игры
def generate_round():
    # Случайный оператор +, - или *
    operator = random.choice(['+', '-', '*'])  # NOSONAR
    # Случайные два числа
    num1 = random.randint(1, 10)  # NOSONAR
    num2 = random.randint(1, 10)  # NOSONAR

    # Вычисление правильного ответа
    match operator:
        case '+':
            correct = num1 + num2
        case '-':
            correct = num1 - num2
        case '*':
            correct = num1 * num2

    # Строка вопроса
    question = f"{num1} {operator} {num2}"
    # Переводим правильный ответ в строку для корректного сравнения с ответом
    return question, str(correct)