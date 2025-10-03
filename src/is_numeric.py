def is_numeric(token):
    """Проверяет, является ли токен числом (целым или вещественным)"""
    try:
        float(token) # Пробуем преобразовать в float - если получится, это число
        return True
    except (ValueError, TypeError): # Если не получилось - это не число
        return False