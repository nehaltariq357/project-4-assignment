AFFIRMATION = "I am capable of doing anything I put my mind to."
def main():
    print("write the following affrimation:" ,AFFIRMATION)
    user_feedback = input()
    while user_feedback !=AFFIRMATION:
        print("Thats was not right.")

        print("Please write the following affrimation correctly:" ,AFFIRMATION)
        user_feedback = input()
    print("That's right! :)")

if __name__ == '__main__':
    main()