# 

import time
import math

start_time = time.time()

def isPrime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    else:
        r = math.sqrt(n)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f = f + 6
        return True


primes = []
count = 1

for i in range (1, 65500):
    i = i + 2
    if isPrime(i):
        count = count + 1
        primes.append(i)

print(primes)
print(len(primes))
print(primes[-1])

print("--- %s seconds ---" % (time.time() - start_time))
