# Логика игры "НОД"
import math
import random  # NOSONAR

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    a = random.randint(1, 50)  # NOSONAR
    b = random.randint(1, 50)  # NOSONAR
    question = f"{a} {b}"
    correct_answer = str(math.gcd(a, b))
    return question, correct_answer