# Логика игры "Простое ли число?"

# Импортируем модуль random для генерации случайных чисел
import random  # NOSONAR

# Описание игры, которое будет показано пользователю
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Проверка, является ли число простым.
# Простое число – это число больше 1, которое делится только на 1 и на себя.
# Возвращает True, если число простое, иначе False.
def is_prime(number):
    # Числа меньше 2 не являются простыми (0 и 1)
    if number < 2:
        return False
    # Проверить делители от 2 до квадратного корня из number
    # int(number ** 0.5) + 1 – округлённый вверх квадратный корень
    for i in range(2, int(number ** 0.5) + 1):
        # Если есть делитель, число не простое
        if number % i == 0:
            return False
    # Если нету делителя, то число простое
    return True


# Один раунд, вопрос и правильный ответ
def generate_round():
    # Случайное число
    number = random.randint(1, 100)  # NOSONAR
    # Вопрос в виде строки
    question = str(number)
    # Правильный ответ: 'yes', если число простое, иначе 'no'
    correct_answer = 'yes' if is_prime(number) else 'no'
    # Возвращаем вопрос и ответ
    return question, correct_answer