def main():
    """
    3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
    (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.
    """
    salaries = {}

    with open('files/third.txt') as file:
        for line in file:
            name, salary = line.split()
            salaries[name] = float(salary)

    less_than_20000 = [name for name, salary in salaries.items() if salary < 20000]
    average_salary = sum(salaries.values()) / len(salaries)

    print(f'Сотрудники с окладом меньше 20000: {", ".join(less_than_20000)}')
    print(f'Средняя зарплата: {average_salary}')


if __name__ == '__main__':
    main()
