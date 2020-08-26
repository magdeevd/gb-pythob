def main():
    seconds = int(input("Enter time in seconds: "))
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))


if __name__ == '__main__':
    main()
