# Fibonacci logic:
# Fibonacci sequence hoti hai:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# (her number = previous 2 numbers ka sum)

# version 1
a, b = 0, 1

while b < 10:
    #print(b)
    a, b = b, a + b


#version 2
MAX_TERM_VALUE : int = 10000
def main():
    current_term = 0
    next_term = 1

    while current_term <= MAX_TERM_VALUE:
        print(current_term)
        term_after_next = current_term + next_term
        current_term = next_term
        next_term = term_after_next


if __name__ == '__main__':
    main()