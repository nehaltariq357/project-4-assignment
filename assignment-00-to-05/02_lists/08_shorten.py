# Jab tak list ka length MAX_LENGTH se zyada hai:
# pop() se last element hatao
# print() karo usey
#remove element print ho rha ha
max_length:int = 3

def shorten(lst):
    while len(lst) > max_length:
        last_element = lst.pop()
        print(last_element)

def get_lst():
    lst = []
    element = input("Please enter an element of the list or press enter to stop. ")
    while element:
        lst.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return lst


def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()