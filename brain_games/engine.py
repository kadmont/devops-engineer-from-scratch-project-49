# Общий движок для управления циклом вопрос-ответ

# библиотека, которую добавляем в начале проекта для ввода данных пользователя.
import prompt

# Кол-во успешных попыток
ROUNDS_COUNT = 3


def run_game(game_module):
    # Запуск игры с общим циклом вопросов и ответов.
    print("Welcome to the Brain Games!")
    # Запрашиваем имя игрока, всегда возвращаем строку
    # Позволяет сравнивать ответ пользователя
    # с правильным ответом напрямую без преобразования
    name = prompt.string("May I have your name? ")
    # Приветствуем по имени
    print(f"Hello, {name}!")
    # Выводим описание игры, берем из модуля DESCRIPTION
    print(game_module.DESCRIPTION)

    # Основной игровой цикл, кол-во успешных ответов
    for _ in range(ROUNDS_COUNT): 
        # Сравниваем вопрос и правильный ответ
        question, correct_answer = game_module.generate_round()
        # Показываем вопрос пользователю
        print(f"Question: {question}")
        # Читаем ответ пользователя с клавиатуры
        user_answer = prompt.string("Your answer: ")

        # Сравниваем ответ пользователя с клавиатурой
        if user_answer != correct_answer:
            # Сообщаем об ошибке и завершаем игру
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            # Завершаем и выходим
            return
        # Если ответ правильный выводим "Correct!" и идем дальше
        print("Correct!")
    # Если все раунды пройдены успешно, то поздравляем
    print(f"Congratulations, {name}!")