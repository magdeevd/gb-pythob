from itertools import count, cycle


def generate(start, end):
    for el in count(start):
        if el > end:
            break
        else:
            yield el


def repeat(l, end):
    c = 0
    for el in cycle(l):
        if c >= end * len(l):
            break
        yield el
        c += 1


def main():
    """
    6. Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.

    Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
    должен быть бесконечным. Необходимо предусмотреть условие его завершения.
    """
    print([el for el in generate(0, 10)])
    print([el for el in repeat([1, 2, 3, 4], 5)])


if __name__ == '__main__':
    main()
