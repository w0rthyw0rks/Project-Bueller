# https://en.wikipedia.org/wiki/Lattice_path
# https://en.wikipedia.org/wiki/Binomial_coefficient
# https://en.wikipedia.org/wiki/Factorial

import math
import time
start_time = time.time()

n = 20
k = 20

x = n + k

print(math.factorial(x) / (math.factorial(n)*math.factorial(x - n)))

print("--- %s seconds ---" % (time.time() - start_time))
