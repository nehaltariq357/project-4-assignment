
#Problem #2: Index Game
#Initialize a List:

fruit_list:list = [ 'apple', 'banana', 'orange', 'grape', 'pineapple']
                    # 0        1          2         3         4 

#Accessing Elements
def accessing_element(my_list,index):
    if 0 <= index < len(my_list): #Index 0 se kam na ho aur length se chhota ho
        return my_list[index] # e.g., index = 0, 1, 2, 3, 4 valid hain
    else:
        return "Index out of range!" # agar index bahar ho
result_accessing_element =accessing_element(fruit_list,2)
print(result_accessing_element)

#Modifying Elements:

def modifying_element(my_list,index,new_value): #Accepts a list, an index, and a new value as inputs.
    try:
        my_list[index] = new_value # my_list[2] = "mango"
        return my_list
    except IndexError:
        return "Index out of range!" # agar index bahar ho

result_modifying_element = modifying_element(fruit_list,2,"mango")
print(result_modifying_element)

#Slicing the List:
fruit_list_slicing:list = [ 'apple', 'banana', 'orange', 'grape', 'pineapple']
                            # 0        1          2         3         4       
def slicing_list(my_list,start_indx,end_indx):#Accepts a list, a start index, and an end index as inputs.
    try:
        sliced_element = my_list[start_indx:end_indx]
        return sliced_element
    except IndexError:
        return "Index out of range!" # agar index bahar ho

result_slicing_element = slicing_list(fruit_list_slicing,1,4)
print(result_slicing_element) # banana,orange,grape, index 4 is excluded




