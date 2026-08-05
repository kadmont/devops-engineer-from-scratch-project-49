# Точка входа для игры "Простое ли число?"

# Импортирую фукцию run_game из общего движка
# /brain_games/engine.py импортируем функцию run_game
from brain_games.engine import run_game

# /brain_games/games/prime.py импортируем функцию prime
from brain_games.games import prime


# Функция которая вызывает run_game(prime), точка запуска
def main():
    # Основная функция, которая запускает игру
    # передает модуль prime в движок run_game
    run_game(prime)


# Если запускаем этот файл напрямую (не библиотека),
# то запускается main. Как скрипт и модуль 
if __name__ == "__main__":
    main()