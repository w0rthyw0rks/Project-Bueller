import math
import time

start_time = time.time()

n = 100

digits = math.factorial(n)

print(sum(int(x) for x in str(digits)))

print(sum(map(int, str(digits))))


print("--- %s seconds ---" % (time.time() - start_time))
