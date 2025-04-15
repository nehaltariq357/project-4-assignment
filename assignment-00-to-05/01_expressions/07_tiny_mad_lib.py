SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my" # adjective noun verb
def main():
    adjective:str = input("Please type an adjective and press enter: ")
    noun:str = input("Please type a noun and press enter: ")
    verb:str = input("Please type a verb and press enter: ")
    print(f"{SENTENCE_START} \033[1m\033[3m{adjective} {noun} {verb}\033[0m!")
if __name__ == '__main__':
    main()