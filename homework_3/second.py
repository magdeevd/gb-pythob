def stringify_user(name, surname, birthyear, city, email, phone):
    return f"{name} {surname} {birthyear} {city} {email} {phone}"


def main():
    """
    2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
    год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.
    """
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    birthyear = input("Введите год рождения: ")
    city = input("Введите город проживания: ")
    email = input("Введите email: ")
    phone = input("Введите телефон: ")

    print(stringify_user(name=name, surname=surname, birthyear=birthyear, city=city, email=email, phone=phone))


if __name__ == '__main__':
    main()
