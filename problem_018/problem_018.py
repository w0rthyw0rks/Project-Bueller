def maxPathSum(tri, m, n):

    for i in range(m - 2, -1, -1):
        for j in range(i + 1):

            if (tri[i + 1][j] > tri[i + 1][j + 1]):
                tri[i][j] += tri[i + 1][j]
            else:
                tri[i][j] += tri[i + 1][j + 1]

    return tri[0][0]


nums = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".splitlines()

print(nums)

trgArray = []

# this takes the list of lists (strings) and converts it to a list of lists (integers)

for i in range(0, len(nums)):
    row = nums[i].split()
    intRow = [int(x) for x in row]
    trgArray.append(intRow)

print(trgArray)

# this adds in 0's to make each sub list a length of 15

for j in range(0, len(trgArray)):
    c = 0
    for k in trgArray[j]:
        c += 1
    for x in range(c, 15):
        trgArray[j].append(0)

print(trgArray)

# function to find the maximum sum path from the bottom up


a = maxPathSum(trgArray, 15, 15)

print(a)

    # produces 1064 which is not the max
# 1307 is the max if you add the highest number in each row regardless of rules
