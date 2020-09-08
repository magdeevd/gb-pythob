def main():
    """
    4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
    """
    line = input('Введите набор чисел: ')
    open('numbers.txt', 'w').write(line)
    numbers = open('numbers.txt').read().split()
    result = sum(map(int, numbers))
    print(result)


if __name__ == '__main__':
    main()
