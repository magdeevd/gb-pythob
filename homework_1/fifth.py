def main():
    proceeds = float(input("Введите значение выручки: "))
    costs = float(input("Введите значение издержек: "))

    profit = proceeds - costs

    if profit >= 0:
        print(f"Рентабельность: {round((profit / proceeds) * 100)}%")
        number_of_employees = int(input("Введите количество сотрудников: "))
        print(f"Прибыль фирмы в расчете на одного сотрудника равна {(profit / number_of_employees):.2f}")
    else:
        print("Фирма не получает прибыли")


if __name__ == '__main__':
    main()
