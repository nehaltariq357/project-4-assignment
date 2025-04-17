
def is_odd(num):
    remainder = num % 2 ==1
    return remainder 
    


def main():
    for num in range(10,20):
        if is_odd(num):
            print(num, "odd", end=" ")
        else:
            print(num, "even", end=" ")
if __name__ == '__main__':

    main()