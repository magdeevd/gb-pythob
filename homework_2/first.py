def main():
    """
    1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
    каждого элемента. Использовать функцию type() для проверки типа.
    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
    """
    l = [1, 'string', 2.0, (1, 2), [3, 3], None]
    types = [type(i) for i in l]
    
    print(types)


if __name__ == '__main__':
    main()



