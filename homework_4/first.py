import argparse


def calculate(hours, payment, prize):
    return (hours * payment) + prize


def main():
    """
    1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для
    конкретных значений необходимо запускать скрипт с параметрами.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--hours', type=int, help='выработка в часах', required=True)
    parser.add_argument('--payment', type=float, help='ставка в час', required=True)
    parser.add_argument('--prize', type=float, help='премия', required=True)

    args = parser.parse_args()

    print(calculate(args.hours, args.payment, args.prize))


if __name__ == '__main__':
    main()
