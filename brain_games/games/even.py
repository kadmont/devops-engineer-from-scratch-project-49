# Логика игры "Проверка на четность"

# Импортируем модуль для генерации случайных чисел
import random  # NOSONAR - safe for game logic

# Описание игры, которое будет показано пользователю
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    # Проверяет, является ли число чётным (предикат, True или False)
    return number % 2 == 0


# Генерирует вопрос и правильный ответ для одного раунда.
def generate_round():
    # Генерация случайного числа
    number = random.randint(1, 100)  # NOSONAR
    # Вывод конвертирую в строку
    question = str(number)
    # Правильный ответ (строка) для сравнения с ответом пользователя
    correct_answer = 'yes' if is_even(number) else 'no'
    # Вернуть пары
    return question, correct_answer