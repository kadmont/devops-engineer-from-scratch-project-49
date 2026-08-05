# Точка входа для игры "НОД"

# Импортирую фукцию run_game из общего движка
# /brain_games/engine.py импортируем функцию run_game
from brain_games.engine import run_game

# /brain_games/games/gcd.py импортируем функцию gcd
from brain_games.games import gcd


# Функция которая вызывает run_game(gcd), точка запуска
def main():
    # Основная функция, которая запускает игру
    # передает модуль gcd в движок run_game
    run_game(gcd)


# Если запускаем этот файл напрямую (не библиотека),
# то запускается main. Как скрипт и модуль 
if __name__ == "__main__":
    main()