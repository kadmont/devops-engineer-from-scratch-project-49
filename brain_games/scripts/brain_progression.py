# Точка входа для игры "Арифметическая прогрессия"

# Импортирую фукцию run_game из общего движка
# /brain_games/engine.py импортируем функцию run_game
from brain_games.engine import run_game

# /brain_games/games/progression.py импортируем функцию progression
from brain_games.games import progression


# Функция которая вызывает run_game(progression), точка запуска
def main():
    # Основная функция, которая запускает игру
    # передает модуль progression в движок run_game
    run_game(progression)


# Если запускаем этот файл напрямую (не библиотека),
# то запускается main. Как скрипт и модуль 
if __name__ == "__main__":
    main()