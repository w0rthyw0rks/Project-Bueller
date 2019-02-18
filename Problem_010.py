# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import time
start_time = time.time()

primes = [2, 3]
num = primes[-1]

while num < 2000000:
    isPrime = True
    for prime in primes:
        if prime * prime > num:
            break
        if num % prime == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(num)
    num += 2

print(sum(set(primes)))


print("--- %s seconds ---" % (time.time() - start_time))
