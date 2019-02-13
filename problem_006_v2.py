
import time
start_time = time.time()

limit = 100

sum = ( limit * ( limit + 1) ) / 2
sumSquares = (2 * limit + 1) * (limit + 1) * (limit / 6)

print(sum**2 - sumSquares)

print("--- %s seconds ---" % (time.time() - start_time))

# --- 0.00011205673217773438 seconds ---
