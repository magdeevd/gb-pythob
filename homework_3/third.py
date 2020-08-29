from sys import argv


def my_func(a, b, c):
    return a + b + c - min(a, b, c)


def main():
    """
    3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов.
    """
    print(my_func(int(argv[1]), int(argv[2]), int(argv[3])))


if __name__ == '__main__':
    main()

