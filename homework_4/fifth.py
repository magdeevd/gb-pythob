from functools import reduce


def main():
    """
    5. Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти четные числа от 100 до 1000 (включая границы).
    Необходимо получить результат вычисления произведения всех элементов списка.
    Подсказка: использовать функцию reduce().
    """
    result = reduce(lambda acc, number: acc * number, [number for number in range(100, 1000 + 1) if number % 2 == 0])
    print(result)


if __name__ == '__main__':
    main()
