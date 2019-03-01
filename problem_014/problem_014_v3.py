# runs in 73 seconds
# runs in 53 seconds
# runs in 32 seconds
# runs in 28 seconds
# runs in 20 seconds

import time
start_time = time.time()

def countChain(n):
#   if chains[n]:
#        return chains[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + countChain(n / 2)
    else:
        return 2 + countChain((3 * n + 1) / 2)

chains = []
longest_chain = 0
answer = 0

for i in range(1, 100):
    a = countChain(i)
    if a > longest_chain:
        longest_chain = a
        answer = i
    chains.append([i: a])

print(answer)
print(chains)

print("--- %s seconds ---" % (time.time() - start_time))

