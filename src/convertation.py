def convert_to_number(token):
    """Преобразует токен, являющийся строкой, в число (int или float)"""
    if '.' in token:
        return float(token)
    else:
        return int(token)