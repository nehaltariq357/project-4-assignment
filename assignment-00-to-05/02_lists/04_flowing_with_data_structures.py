def add_three_Copies(my_list,data):
    for _ in range(3):
        my_list.append(data)


def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("list before",my_list)
    add_three_Copies(my_list,message)
    print("list after",my_list)


if __name__ == '__main__':
    main()