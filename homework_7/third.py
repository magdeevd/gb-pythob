class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, cell):
        return Cell(self.quantity + cell.quantity)

    def __sub__(self, cell):
        return self.quantity - cell.quantity if (self.quantity - cell.quantity) > 0 else print('error')

    def __mul__(self, cell):
        return Cell(self.quantity * cell.quantity)

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, in_row):
        row = ''

        for i in range(int(self.quantity / in_row)):
            row += f'{"*" * in_row}\n'
        row += f'{"*" * (self.quantity % in_row)}'

        return row


def main():
    """
    3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
    умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
    уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
    """

    cell = Cell(12)

    print(cell.make_order(5))


if __name__ == '__main__':
    main()
