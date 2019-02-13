# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

numbers = []
squares = []
x = 100

for i in range(1, x+1):
    numbers.append(i)
    a = i ** 2
    squares.append(a)

print(numbers)
print(squares)

print(sum(squares))

print(sum(numbers)**2)

print(sum(numbers)**2 - sum(squares))
