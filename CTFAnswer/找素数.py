import math


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

min = 367
add = 186
ii = 1

while ii<151:
    if isPrime(min):
        ii = ii + 1
    min = min + add

print(min)