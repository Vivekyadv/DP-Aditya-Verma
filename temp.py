from math import sqrt
def countPrimes(n):
    if n < 2:
        return 0
    count = 1
    for i in range(3, n, 2):
        if is_prime(i):
            count += 1
    return count

def is_prime(k):
    for i in range(2, int(sqrt(k)+1)):
        if k % i == 0:
            return 0
    return 1

print(countPrimes(1500000))
# 2, 3, 5, 7