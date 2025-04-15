# Ek year leap year tab hota hai agar:

# 4 se divide ho

# 100 se divide na ho

# Lekin agar 100 se divide hota ho, to phir usko 400 se bhi divide hona chahiy

def main():
    year = int(input("Please enter a year: "))

    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else: # not divisible by 400
                print(f"{year} is not a leap year")
        else: #not divisble by 100
            print(f"{year} is a leap year")
    else:# not divisible by 4
        print(f"{year} is not a leap year")


if __name__ == '__main__':
    main()