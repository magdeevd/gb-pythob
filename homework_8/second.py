class OwnZeroDivisionError(Exception):
    pass


def main():
    """
    2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
    вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
    эту ситуацию и не завершиться с ошибкой.
    """
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))

    try:
        if b == 0:
            raise OwnZeroDivisionError
        else:
            print(a / b)
    except OwnZeroDivisionError:
        print('Деление на ноль!')


if __name__ == '__main__':
    main()
