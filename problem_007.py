# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?

import time
start_time = time.time()

primes = []

for possiblePrime in range(2, 20000000):

    isPrime = True

    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(possiblePrime)

    if len(primes) == 10001:
        break

print(primes[-1])

print("--- %s seconds ---" % (time.time() - start_time))

