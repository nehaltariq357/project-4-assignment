import random

def done():
    random_num = random.randint(0,1)
    if random_num == 0:
        return False
    
    return True


def choatic_counting():
    for i in range(1,11):
        if done():
            return
        print(i)


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    choatic_counting()
    print("I'm done.")
if __name__ == '__main__':
    main()