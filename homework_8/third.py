class NotNumberError(Exception):
    pass


def main():
    """
    3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
    Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
    список только числами. Класс-исключение должен контролировать типы данных элементов списка.
    """
    result = []
    q = 'q'

    while True:
        number = input('Введите число:')

        try:
            if number.isnumeric():
                result.append(int(number))
            elif number.strip() == q:
                print(result)
                return
            else:
                raise NotNumberError
        except NotNumberError:
            print('Не является числом')

        print(result)


if __name__ == '__main__':
    main()
