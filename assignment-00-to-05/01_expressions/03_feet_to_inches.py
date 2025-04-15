inches_in_foot:int = 12
def main():
    number:float = float(input("Enter a number: "))
    label = "foot" if number ==1 else "feet"
    print(f"User Entered {number} {label}")
    feet:float = number
    inches:float = inches_in_foot * feet
    print(f"That is {inches:.2f} inches")   
if __name__ == '__main__':
    main()