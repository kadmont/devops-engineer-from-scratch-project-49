# Точка входа для игры "Проверка на четность"

# Импортирую фукцию run_game из общего движка
# /brain_games/engine.py импортируем функцию run_game
from brain_games.engine import run_game

# /brain_games/games/even.py импортируем функцию even
from brain_games.games import even


# Функция которая вызывает run_game(even), точка запуска
def main():
    # Основная функция, которая запускает игру
    # передает модуль even в движок run_game
    run_game(even)


# Если запускаем этот файл напрямую (не библиотека),
# то запускается main. Как скрипт и модуль 
if __name__ == "__main__":
    main()