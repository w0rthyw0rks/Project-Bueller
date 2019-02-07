my_list = list()

for n in range(1,1000):
    if n % 3 == 0:
    	my_list.append(n)
    elif n % 5 == 0:
    	my_list.append(n)

print my_list
print sum(my_list)
