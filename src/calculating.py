from src.writing_to_massif import writing_to_massif
import sys


def calculating_the_expression(expression):
    """Вычисляет выражение в обратной польской нотации (RPN)"""

    stack = [] # Основной стек для вычислений
    massif_of_massifs = [] # Стек для хранения состояний при вложенных скобках
    counting_parentheses = 0 # Счётчик скобок

    # Обрабатываем каждый токен в выражении
    for element in expression:
        if element != '(' and element != ')':
            # Если токен не скобка - обрабатываем как число или операцию
            stack = writing_to_massif(stack, element)
        elif element == '(':
            # Открывающая скобка - сохраняем текущее состояние стека и начинаем новое подвыражение
            counting_parentheses += 1
            massif_of_massifs.append(stack) # Сохраняем текущий стек
            stack = []  # Начинаем новый стек для подвыражения в скобках
        elif element == ')':
            # Закрывающая скобка - завершаем подвыражение и возвращаем результат в основной стек
            counting_parentheses -= 1
            if counting_parentheses < 0:
                sys.exit('Incorrect parenthesis syntax') # Проверка на лишние закрывающие скобки
            if len(stack) == 1:
                result = stack.pop() # Извлекаем результат из подвыражения
                stack = massif_of_massifs.pop()  # Восстанавливаем предыдущий стек
                stack.append(result)  # Добавляем результат в основной стек
            else:
                sys.exit('Incorrect entry in parentheses')

    # Проверяем корректность результата после обработки всех токенов
    if counting_parentheses == 0 and len(stack) == 1:
        print(f"Answer: {stack[0]}")
        exit(0)
    elif counting_parentheses > 0:
        sys.exit('Incorrect parenthesis syntax')
    else:
        sys.exit('Not enough operators')