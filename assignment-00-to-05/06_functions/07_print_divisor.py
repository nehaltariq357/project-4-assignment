
    # Loop 1 se num tak chalega (i = 1 to num)
    # Har step mein check hoga:
    # Kya num i se poori tarah divide hota hai? (i.e.remainder == 0)
    # Agar evenly divide ho jaaye to iska matlab i ek divisor hai
    # Toh us i ko print kar do

def print_divisor(num):
    for i in range(1,num+1):
        if num % i ==0:
            print(i)


def main():
    user_input = int(input("Enter a number: "))
    print_divisor(user_input)

if __name__ == '__main__':
    main()