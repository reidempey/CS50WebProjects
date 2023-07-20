def check_n(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def main():
    n = input("Number: ")
    if check_n(n):
        n = int(n)
        if n > 0:
            print("N is positive.")
        else:
            print("N is negative.")
    else:
        print("You didn't give me a whole number!")


if __name__ == "__main__":
    main()