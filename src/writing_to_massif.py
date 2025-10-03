from src.is_numeric import is_numeric
from src.convertation import convert_to_number
from src.is_operation import is_operation
import sys


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
        elif element == '**' or element == '^':
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
