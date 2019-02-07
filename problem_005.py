# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 20

for a in range (20, 1000000000):
    while a % i == 0:
        i = i - 1
        if i == 1:
            print (a)
            break
    i = 20
