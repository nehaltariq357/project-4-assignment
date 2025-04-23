
#Accessing Elements:
def access(list,index):
    try:
        if 0<= index<len(list):
            return list[index]
    except IndexError:
        return "Index out of range!"
    
#Modifying Elements:

def modify(list,index,new_value):
    try:
        list[index] = new_value
        return list
    except IndexError:
        return "Index out of range!"
    
#Slicing the List:
def slicing(list,start,end):
    try:
        sliced_list = list[start:end]
        return sliced_list
    except IndexError:
        return "Index out of range!"


def index_game():
    lst:list = [1,2,3,4,5]

    while True:
        print("Current list:", lst)
        print("choose an operation: access, modify, slice or press Enter to exit")
        operation = input("Enter an operation: ")

        if operation == "access":
            index = int(input("Enter index to access: "))
            print(access(lst,index))
        elif operation == "modify":
            index = int(input("Enter index to modify: "))
            new_value = int(input("Enter a new value: "))
            print(modify(lst,index,new_value))
        elif operation == "slice":
            start = int(input("Enter a start index: "))
            end = int(input("Enter a end index: "))
            print(slicing(lst,start,end))

        elif operation == "":
            print("Thanks for playing the Index Game!")
            break
        else:
            print("Invalid input!")

index_game()