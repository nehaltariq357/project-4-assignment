PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
def main():
    user_age: int = int(input(f"How old are you?: "))
    print(f"{BLUE}{user_age}{RESET}")
    # Check if the user can vote in Peturksbouipo

    if user_age >= PETURKSBOUIPO_AGE:
        print(f"{GREEN}You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}{RESET}")

    else :
        print(f"{RED}You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}{RESET}")

    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print(f"{GREEN}You can vote in Stanlau where the voting age is {STANLAU_AGE} {RESET}")
    else:
        print(f"{RED}You cannot vote in Stanlau where the voting age is {STANLAU_AGE} {RESET}")

        # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print(f"{GREEN}You can vote in Mayengua where the voting age is {MAYENGUA_AGE}{RESET}")
    else:
        print(f"{RED}You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}{RESET}")
if __name__ == '__main__':
    main()