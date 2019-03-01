# runs in 73 seconds
# runs in 53 seconds (start at 500k not at 1)
# runs in 32 seconds
# runs in 28 seconds
# runs in 20 seconds ( 2 + (3*n+1)/2 )

import time
start_time = time.time()

def countChain(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + countChain(n / 2)
    else:
        return 2 + countChain((3 * n + 1) / 2)

longest_chain = 0
answer = 0

for i in range(500000, 10**6):
    if countChain(i) > longest_chain:
        longest_chain = countChain(i)
        answer = i

print(answer)

print("--- %s seconds ---" % (time.time() - start_time))
