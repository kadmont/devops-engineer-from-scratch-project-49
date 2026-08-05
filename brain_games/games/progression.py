# Логика игры "Арифметическая прогрессия"

# Импортируем модуль для генерации случайных параметров прогрессии
import random  # NOSONAR

# Описание игры, которое будет показано пользователю
DESCRIPTION = "What number is missing in the progression?"


# Функция, которая генерирует один раунд игры
# Арифметическая прогрессия с одним пропущенным числом.
# Возвращает (вопрос, правильный_ответ) как строки.
def generate_round():
    # Длина прогрессии
    length = random.randint(5, 10)  # NOSONAR
    # Первый элемент прогрессии
    start = random.randint(1, 50)  # NOSONAR
    # Шаг прогрессии
    step = random.randint(1, 10)  # NOSONAR
    # Индекс скрытого элемента (от 0 до length-1)
    hidden_index = random.randint(0, length - 1)  # NOSONAR

    # Генерация членов прогрессии как список
    progression = [str(start + i * step) for i in range(length)]
    # Правильный ответ 
    correct_answer = progression[hidden_index]
    # Заменить скрытый элемент на маркер пропуска
    progression[hidden_index] = '..'

    # Строка вопроса, соединяю все элементы через пробел
    question = ' '.join(progression)
    # Вопрос и правильный ответ (str)
    return question, correct_answer