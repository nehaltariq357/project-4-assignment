def main():
    anton:int = 21 # anton's age is given as 21 year old
    beth:int = 6 + anton # beth is 6 year older than anton
    chen:int = 20 + beth # chen is 20 year older than beth
    drew:int = chen + anton # drew is old as chen's age plus anton's age, so add them together
    ethan:int = chen # ethan is the same age as chen

    # Print out all of the ages!
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))


if __name__ == '__main__':
    main()