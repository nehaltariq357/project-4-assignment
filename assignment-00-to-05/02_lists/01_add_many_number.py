
def add_many_number(numbers)->int:
    '''
    Takes a list of numbers and return the sum of those numbers.
    '''
    total_so_far = 0
    for num in numbers:
        total_so_far +=num

    return total_so_far
def main():
    numbers:list[int] = [1,2,3,4,5] # make a list of numbers
    sun_of_numbers:int = add_many_number(numbers)
    print(sun_of_numbers) # print out the sum above

if __name__ == '__main__':
    main()