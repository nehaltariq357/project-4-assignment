def main():
    num:float = float(input("Type a number to see its square: "))
    square:float = num ** 2 # num * num is equivalent to num**2.The ** operator raises something to a power!
    print(f"{num} squared is \033[1m\033[3m{square}\033[0m")
if __name__ == '__main__':
    main()