def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    i = 1
    while a <= b:
        a = a + 0.1 * a
        i = i + 1

    print(i)


if __name__ == '__main__':
    main()
