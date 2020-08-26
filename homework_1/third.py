def main():
    n = input("Enter n: ")
    result = int(n) + int(f"{n}{n}") + int(f"{n}{n}{n}")
    print(result)


if __name__ == '__main__':
    main()
