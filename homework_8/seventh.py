class ComplexNumber:
    def __init__(self, a, b):
        self.number = complex(a, b)

    def __add__(self, other):
        add = self.number + other.number
        return ComplexNumber(add.real, add.imag)

    def __mul__(self, other):
        mul = self.number * other.number
        return ComplexNumber(mul.real, mul.imag)

    def __str__(self):
        return str(self.number)


def main():
    """
    7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
    методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
    (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
    результата.
    """
    z1 = ComplexNumber(3, -4)
    z2 = ComplexNumber(1, 3)
    print(z1 + z2)
    print(z1 * z2)


if __name__ == '__main__':
    main()
