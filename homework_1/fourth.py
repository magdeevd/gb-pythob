def main():
    n = int(input("Enter n: "))

    max_number = 0

    while n:
        n, mod = divmod(n, 10)
        max_number = max(max_number, mod)

    print(max_number)


if __name__ == '__main__':
    main()
