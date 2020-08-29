import sys


def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Zero division")


def main():
    """
    1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
    """
    division(int(sys.argv[1]), int(sys.argv[2]))


if __name__ == '__main__':
    main()
