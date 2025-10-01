import sys


def is_numeric(token):
    """Проверяет, является ли токен числом (целым или вещественным)"""
    try:
        float(token) # Пробуем преобразовать в float - если получится, это число
        return True
    except (ValueError, TypeError): # Если не получилось - это не число
        return False


def convert_to_number(token):
    """Преобразует токен, являющийся строкой, в число (int или float)"""
    if '.' in token:
        return float(token)
    else:
        return int(token)


def is_operation(token):
    """Проверяет, является ли токен поддерживаемой операцией"""
    return token in ['+', '-', '*', '/', '//', '**', '%']


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
                Answer: stack.pop() # Извлекаем результат из подвыражения
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


def writing_to_massif(stack, element):
    """Обрабатывает один токен: число или операцию"""

    if is_numeric(element): # Если токен число - преобразуем и добавляем в стек
        stack.append(convert_to_number(element))
        return stack

    elif is_operation(element):

        if len(stack) < 2: # Проверяем, что в стеке есть достаточно операндов
            sys.exit('Not enough operands for operator')

        # Для операций извлекаем два операнда из стека
        element_2 = stack.pop()  # правый операнд
        element_1 = stack.pop() # левый операнд

        # Проводим вычисления
        if element == '+':
            stack.append(element_1 + element_2)
        elif element == '-':
            stack.append(element_1 - element_2)
        elif element == '*':
            stack.append(element_1 * element_2)
        elif element == '/' and element_2 != 0:
            stack.append(element_1 / element_2)
        elif element == '//' and element_2 != 0 and element_2 == int(element_2) and element_1 == int(element_1):
            stack.append(element_1 // element_2)
        elif element == '**':
            stack.append(element_1 ** element_2)
        elif element == '%' and element_2 != 0 and element_2 == int(element_2) and element_1 == int(element_1):
            stack.append(element_1 % element_2)
        elif element_2 == 0:
            sys.exit("You can't divide by zero")
        elif element_2 != int(element_2) or element_1 != int(element_1):
            sys.exit("You can't divide non-integers")
        return stack

    # Если токен не число и не операция - ошибка
    else:
        sys.exit(f"I don`t know what to do with the '{element}'")


def print_welcome_message():
    """Выводит приветственное сообщение и инструкции"""
    print("=" * 70)
    print("          КАЛЬКУЛЯТОР ОБРАТНОЙ ПОЛЬСКОЙ НОТАЦИИ (RPN)")
    print("=" * 70)
    print("ВОЗМОЖНОСТИ:")
    print("  1) Поддержка целых и вещественных чисел")
    print("  2) Арифметические операции: +, -, *, /, //, **, %")
    print("  3) Работа с отрицательными и вещественными числами (например: -5, -3.14)")
    print("  4) Вложенные скобки для группировки выражений")
    print("  5) Проверка ошибок: деление на ноль, неверный синтаксис")

    print("КАК ПОЛЬЗОВАТЬСЯ:")
    print("  Записывайте выражение в формате Обратной Польской Нотации (RPN)")
    print("  Разделяйте все элементы ПРОБЕЛАМИ")

    print("ПРИМЕРЫ:")
    print("  Сложение:        '5 3 +'           →  Answer: 8")
    print("  Умножение:       '2 4 *'           →  Answer: 8")
    print("  Со скобками:     '( 5 3 + ) 2 *'   →  Answer: 16")
    print("  Отрицательные:   '-5 3 +'          →  Answer: -2")
    print("  Степень:         '2 3 **'          →  Answer: 8")

    print("\n" + "=" * 70)
    print("Введите выражение ниже (все элементы через пробел):")


def run_calculator():
    """Основная функция запуска калькулятора"""
    print_welcome_message() # Выводит приветственное сообщение
    for line in sys.stdin:
        if line.split() != [] and line != '\n': # Проверяем, что пользователь ввёл не пустую строку
            calculating_the_expression(line.rstrip().split())
        else:
            sys.exit('No input')


if __name__ == '__main__':
    run_calculator()

