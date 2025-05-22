
def binary_search(arr,target):
    low = 0
    high = len(arr) -1

    while(low<=high):
        #find mid element
        midIndex = low +(high-low)//2 # 

        if (arr[midIndex] == target):
            return midIndex
        
        if (target < arr[midIndex]):
            high = midIndex -1
        
        if(target > arr[midIndex]):
            low = midIndex +1
    #print("Not found")
    return -1
        

my_list = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10

result = binary_search(my_list,target)

if result == -1:
    print("Target not found in the list.")
else:
    print("Target found at index:", result)

