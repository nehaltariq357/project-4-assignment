

def get_user_number():
    number = []
    while True:
        user_input =input("Enter a number: ")
        if user_input == "":
            break   
        num = int(user_input)
        number.append(num)
    return number

def count_num(num_list):
    count = {}
    for num in num_list:
        if num in count:
            count[num] +=1 # num is used as a key in the dictionary.If the same number appears again, we increase its count.
        else:
            count[num] = 1

    return count

def main():
    user_number = get_user_number()
    num_dict = count_num(user_number)
    print(num_dict)
if __name__ == '__main__':
    main()




