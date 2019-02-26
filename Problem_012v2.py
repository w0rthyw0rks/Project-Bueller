# runs in 10-11 seconds

import math
import time

start_time = time.time()

triangle = 1
a = 1
count = 0

while count <= 500:
    count = 0
    a = a + 1
    triangle = triangle + a
    triSqRt = int(math.sqrt(triangle))
    for i in range(1, triSqRt + 1):
        if triangle % i == 0:
            count = count + 2

print(triangle)

print("--- %s seconds ---" % (time.time() - start_time))
