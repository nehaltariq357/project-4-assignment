def main():
    #print statement
    print("This program adds two numbers")
    #user input
    num1:str = input("Enter the first number: ")
    num1 = int(num1)
    
    num2:str = input("Enter the second number: ")
    num2 = int(num2)
    #calculation
    total = num1 + num2
    #output
    print(f"The sum of {num1} and {num2} is {total}")


if __name__ == '__main__':
    main()