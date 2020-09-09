class Date:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def extract(cls, date: str):
        day, month, year = date.split('-')

        return int(day), int(month), int(year)

    @staticmethod
    def validate(date: str):
        day, month, year = Date.extract(date)

        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False

        return True


def main():
    """
    1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
    «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
    извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
    должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
    структуры на реальных данных.
    """
    print(Date.validate('10-12-2012'))
    print(Date.validate('10-24-2012'))


if __name__ == '__main__':
    main()
