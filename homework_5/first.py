def main():
    """
    1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка.
    """
    with open('file.txt', 'a',) as file:

        while True:
            string = input()
            if string == '':
                break
            file.write(string + '\n')


if __name__ == '__main__':
    main()
