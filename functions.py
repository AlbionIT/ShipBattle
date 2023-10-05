def is_miss(row, col, desk):
    """Проверка на промах или попадание"""
    if desk.my_field[row - 1][col - 1] == "0":
        return 'miss'
    elif desk.my_field[row - 1][col - 1] == "▀":
        return 'hit'
    else:
        return False
