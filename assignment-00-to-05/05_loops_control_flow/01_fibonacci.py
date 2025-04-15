# Fibonacci logic:
# Fibonacci sequence hoti hai:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# (her number = previous 2 numbers ka sum)

a, b = 0, 1

while b < 10:
    print(b)
    a, b = b, a + b

