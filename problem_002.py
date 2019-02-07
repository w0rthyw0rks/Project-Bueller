my_fib = list ()
my_fib.append(1)
my_fib.append(2)

for n in range(1,100):
    a = my_fib[n] + my_fib[n-1]
    if a < 4000000:
        my_fib.append(a)
    else:
        break

my_evens = list()

l = len(my_fib)

for n in range(0,l):
    if my_fib[n] % 2 == 0:
        my_evens.append(my_fib[n])


print (my_fib)
print ()
print (my_evens)
print ()
print (sum(my_evens))
