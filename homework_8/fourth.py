class NotEnoughEquipment(Exception):
    pass


class OfficeEquipment:

    def __init__(self, title):
        self.title = title


class Printer(OfficeEquipment):

    def print(self):
        pass


class Scanner(OfficeEquipment):

    def scan(self):
        pass


class Xerox(OfficeEquipment):

    def copy(self):
        pass


class Storage:

    def __init__(self):
        self.items = {}

    @staticmethod
    def __key(equipment):
        return equipment.title + equipment.__class__.__name__

    def put(self, equipment):
        key = self.__key(equipment)
        if key in self.items:
            self.items[key] += 1
        else:
            self.items[key] = 1

    def get(self, equipment):
        key = self.__key(equipment)
        if key not in self.items or self.items[key] == 0:
            raise NotEnoughEquipment
        self.items[key] -= 1


def main():
    """
    4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
    который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
    уникальные для каждого типа оргтехники.

    5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
    в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
    других данных, можно использовать любую подходящую структуру, например словарь.

    6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
    для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    """
    storage = Storage()
    storage.put(Printer('Samsung'))
    storage.put(Scanner('Samsung'))
    storage.put(Xerox('Samsung'))
    storage.get(Printer('Samsung'))

    try:
        storage.get(Printer('Samsung'))
    except NotEnoughEquipment:
        print('Not enough equipment')


if __name__ == '__main__':
    main()
