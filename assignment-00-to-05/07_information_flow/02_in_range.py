def in_range(num, low, high):
    if num >= low and num <= high:
        return True
    return False

def main():
    num = int(input("Enter a number: "))
    low = int(input("Enter a low number: "))
    high = int(input("Enter a high number: "))

    if in_range(num, low, high):
        print("The number is in range.")
    else:
        print("The number is not in range.")

if __name__ == '__main__':
    main()
