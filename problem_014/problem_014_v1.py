# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
start_time = time.time()
chains = []
maxCount = 0

for i in range(2, 1000000):
    a = i
    count = 0
    while a > 1:
        if a % 2 == 0:
            a = a / 2
            count += 1
        else:
            a = a * 3 + 1
            count += 1
    if count > maxCount:
        maxCount = count
    chains.append(count)

# print(chains)
# print(maxCount)
print(chains.index(maxCount)+2)

print("--- %s seconds ---" % (time.time() - start_time))

# runs in 73 seconds 

