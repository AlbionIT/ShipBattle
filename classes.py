class Ship:
    def __init__(self, length, row_col):
        """Создание корабля. length - длинна, row - строка, col - столбец"""
        self.row = row_col[0]
        self.col = row_col[1]
        self.length = length


class Desk:
    def __init__(self):
        """Создание пустого поля и пустого списка кораблей на поле"""
        self.my_field = [["0" for j in range(6)] for i in range(6)]
        self.enemy_field = [["0" for j in range(6)] for i in range(6)]
        self.ships = []

    def clear_desk(self):
        self.my_field = [["0" for j in range(6)] for i in range(6)]
        self.ships = []

    def get_ships(self):
        """Вывести список кораблей"""
        print(len(self.ships))

    def add_ship(self, ship):
        """Добавление корабля на поле"""
        if ship.col - 1 + ship.length <= 6 and ship.col > 0 and ship.row > 0:
            self.ships.append(ship)
            if ship.length == 1:
                self.my_field[ship.row - 1][ship.col - 1] = "▀"
            elif ship.length == 2:
                self.my_field[ship.row - 1][ship.col - 1] = "▀"
                self.my_field[ship.row - 1][ship.col] = "▀"
            else:
                self.my_field[ship.row - 1][ship.col - 1] = "▀"
                self.my_field[ship.row - 1][ship.col] = "▀"
                self.my_field[ship.row - 1][ship.col + 1] = "▀"
            return True
        else:
            return False

    def can_add(self, list_x, len_ship):
        """Проверка на возможность добавления корабля по введённым коардинатам"""
        a = [[" " for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                if list_x[0] - 1 - (-i + 1) < 0 or list_x[1] - 1 - (-j + 1) < 0:
                    a[i][j] = "0"
                elif list_x[0] - 1 - (-i + 1) > 5 or list_x[1] - 1 - (-j + 1) > 5:
                    a[i][j] = "0"
                else:
                    a[i][j] = self.my_field[list_x[0] - 1 - (-i + 1)][list_x[1] - 1 - (-j + 1)]

        for row in a:
            for elem in row:
                if elem != "0":
                    return False

        if len_ship == 2:
            for i in range(3):
                for j in range(3):
                    if list_x[0] - 1 - (-i + 1) < 0 or list_x[1] - (-j + 1) < 0:
                        a[i][j] = "0"
                    elif list_x[0] - 1 - (-i + 1) > 5 or list_x[1] - (-j + 1) > 5:
                        a[i][j] = "0"
                    else:
                        a[i][j] = self.my_field[list_x[0] - 1 - (-i + 1)][list_x[1] - (-j + 1)]

            for row in a:
                for elem in row:
                    if elem != "0":
                        return False
        return True

    def field_output(self):
        """Вывод своего поля на экран"""
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        n_row = 1
        for row in self.my_field:
            print(n_row, "|", end=" ")
            for elem in row:
                print(elem, "|", end=' ')
            print()
            n_row += 1

    def field_output_enemy(self):
        """Вывод поля врага на экран"""
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        n_row = 1
        for row in self.enemy_field:
            print(n_row, "|", end=" ")
            for elem in row:
                print(elem, "|", end=' ')
            print()
            n_row += 1

    def shot(self, row, col, desk):
        """Выстрел в точку на поле"""
        if desk.my_field[row - 1][col - 1] == "0":
            desk.my_field[row - 1][col - 1] = "M"
            self.enemy_field[row - 1][col - 1] = "M"
        elif desk.my_field[row - 1][col - 1] == "▀":
            desk.my_field[row - 1][col - 1] = "X"
            self.enemy_field[row - 1][col - 1] = "X"

    def is_Win(self):
        """Проверка на победу"""
        n = 0
        for row in self.enemy_field:
            for elem in row:
                if elem == "X":
                    n += 1
        if n == 11:
            return True
        else:
            return False
