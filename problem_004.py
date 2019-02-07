# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

palindroms = list ()

for a in range(100, 1000):
    for b in range (100,1000):

        pal = str(a * b)

        if pal[0] == pal[-1]:
            if pal[1] == pal[-2]:
                if pal[2] == pal[-3]:
                    palindroms.append(int(pal))


print (palindroms)
print ()
print (max(palindroms))
