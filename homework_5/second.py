def main():
    """
    2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
    количества слов в каждой строке.
    """
    number_of_lines = 0
    number_of_words = {}

    with open('files/second.txt') as file:
        for line in file:
            number_of_lines += 1
            number_of_words[number_of_lines] = len(line.split(' '))

    print("Количество строк:", number_of_lines)
    print("Количество слов в строках:")

    for line, count in number_of_words.items():
        print(f"{line} - {count}")


if __name__ == '__main__':
    main()
