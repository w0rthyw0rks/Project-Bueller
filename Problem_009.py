# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time
start_time = time.time()

triplets = []

# lets start by finding every possible combo of a + b + c = 1000
# then remove all options that don't fit a > b > c
# then scan to see if a^2 + b^2 = c^2

#for a in range(1, 332):
#    for b in range(1, 1000):
#        for c in range(1, 1000):
#            if a + b + c == 1000:
#                triplets.append([a, b, c])

# ---98 seconds---

for a in range(1, 334):
    for b in range(1, 1000):
        if a < b:
            for c in range(1, 1000):
                if b < c:
                    if a + b + c == 1000:
                        triplets.append([a, b, c])
# ---73 seconds---

# array = [[43, 372, 585], [43, 373, 584], [43, 374, 583], [43, 375, 582], [43, 376, 581], [43, 377, 580], [43, 378, 579], [43, 379, 578], [43, 380, 577], [43, 381, 576], [43, 382, 575], [43, 383, 574], [43, 384, 573], [43, 385, 572], [43, 386, 571], [43, 387, 570], [43, 388, 569], [43, 389, 568], [43, 390, 567], [43, 391, 566], [43, 392, 565], [43, 393, 564], [43, 394, 563], [43, 395, 562], [43, 396, 561], [43, 397, 560], [43, 398, 559], [43, 399, 558], [43, 400, 557]]

pyTrip = []

#print(len(array))

for i in range(0, len(triplets)):
    if (triplets[i][0])**2 + (triplets[i][1])**2 == (triplets[i][2])**2:
         pyTrip.append(triplets[i])


#print(triplets)

print(pyTrip)

print(pyTrip[0][0]*pyTrip[0][1]*pyTrip[0][2])

print("--- %s seconds ---" % (time.time() - start_time))

