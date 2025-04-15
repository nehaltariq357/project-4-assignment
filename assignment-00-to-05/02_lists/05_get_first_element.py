def get_first_element(lst):
    '''
    print the first element of a provided list
    '''
    print(lst[0])

def get_lst():
    '''
    prompt the user to enter one element of the list at a time and returns the resulting list.
    '''
    lst = []
    element:str = input("please enter an element of the list or press enter to stop. ")
    while element != "":
        lst.append(element)
        element:str = input("please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()