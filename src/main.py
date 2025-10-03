import sys
from src.calculating import calculating_the_expression


def run_calculator():
    """Основная функция запуска калькулятора"""
    for line in sys.stdin:
        if line.split() != [] and line != '\n': # Проверяем, что пользователь ввёл не пустую строку
            calculating_the_expression(line.rstrip().split())
        else:
            sys.exit('No input')


if __name__ == '__main__':
    run_calculator()