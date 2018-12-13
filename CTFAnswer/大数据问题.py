import math


def factorial(n):
    out = 1
    for i in range(1, n + 1):
        out *= i
    return out


num = 0
for i in range(1, 6790):
    num += factorial(i)

print(num)
