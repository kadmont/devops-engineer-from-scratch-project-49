# Логика игры "НОД"

# Импортируем модуль, набор математических инструментов
import math

# Импортируем модуль для генерации случайных чисел
import random  # NOSONAR

# Описание игры, которое будет показано пользователю
DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    # Случайные числа а и б
    a = random.randint(1, 50)  # NOSONAR
    b = random.randint(1, 50)  # NOSONAR
    # Сформировать вопрос
    question = f"{a} {b}"
    # Вычисляем НОД и преобразуем в строку для сравнения с ответом игрока
    correct_answer = str(math.gcd(a, b))
    # Возврат кортежа: вопрос и правильный ответ
    return question, correct_answer