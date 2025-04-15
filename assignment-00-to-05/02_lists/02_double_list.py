def main():
    numbers:list[int] = [1,2,3,4]
    for i in range(len(numbers)):
        element_at_index = numbers[i] #getting list value from indexing
        numbers[i] = element_at_index * 2 # multiplying value by 2 and updating list value with the help of indexing

    print(numbers)  # This should print the doubled list
if __name__ == '__main__':
    main()