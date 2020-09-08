def main():
    """
    4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4

    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
    числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
    """
    translations = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

    with open('files/fourth.txt') as file, open('result.txt', 'a') as result_file:
        for line in file:
            word, dash, number = line.split()
            result_file.write(f"{translations[word]} {dash} {number}\n")


if __name__ == '__main__':
    main()
