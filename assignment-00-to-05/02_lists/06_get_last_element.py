def get_last_element(lst):
    print(lst[-1])

def get_lst():
    lst = []
    element = input("enter an element to the list or press enter to stop. ")
    while element:
        lst.append(element)
        element = input("enter an element to the list or press enter to stop. ")
    return lst



def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()