# Точка входа для игры "Калькулятор"

# Импортирую фукцию run_game из общего движка
# /brain_games/engine.py импортируем функцию run_game
from brain_games.engine import run_game

# /brain_games/games/calc.py импортируем функцию calc
from brain_games.games import calc


# Функция которая вызывает run_game(calc), точка запуска
def main():
    # Основная функция, которая запускает игру
    # передает модуль calc в движок run_game
    run_game(calc)


# Если запускаем этот файл напрямую (не библиотека),
# то запускается main. Как скрипт и модуль 
if __name__ == "__main__":
    main()