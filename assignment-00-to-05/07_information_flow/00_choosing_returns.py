ADULT_AGE : int = 18
def is_adult(age:int):

    if age >= ADULT_AGE:
        return True
    
    return False


def main():

    age = int(input("How old is this person?: "))
    person_age = is_adult(age)
    print(person_age)

if __name__ == '__main__':
    main()