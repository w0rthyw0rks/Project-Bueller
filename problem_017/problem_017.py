nums = []
words = []
k = 0

for i in range(1, 1001):
    nums.append(str(i))

print(nums)

for j in range(0, len(nums)):

    k = len(nums[j])

    if k == 1:
        if int(nums[j][k - 1]) == 1:
            words.append("one")
        if int(nums[j][k - 1]) == 2:
            words.append("two")
        if int(nums[j][k - 1]) == 3:
            words.append("three")
        if int(nums[j][k - 1]) == 4:
            words.append("four")
        if int(nums[j][k - 1]) == 5:
            words.append("five")
        if int(nums[j][k - 1]) == 6:
            words.append("six")
        if int(nums[j][k - 1]) == 7:
            words.append("seven")
        if int(nums[j][k - 1]) == 8:
            words.append("eight")
        if int(nums[j][k - 1]) == 9:
            words.append("nine")

    if k == 2:

        if int(nums[j]) == 11:
            words.append("eleven")
        if int(nums[j]) == 12:
            words.append("twelve")
        if int(nums[j]) == 13:
            words.append("thirteen")
        if int(nums[j]) == 14:
            words.append("fourteen")
        if int(nums[j]) == 15:
            words.append("fifteen")
        if int(nums[j]) == 16:
            words.append("sixteen")
        if int(nums[j]) == 17:
            words.append("seventeen")
        if int(nums[j]) == 18:
            words.append("eighteen")
        if int(nums[j]) == 19:
            words.append("nineteen")

        if int(nums[j]) % 10 == 0:
            if int(nums[j]) == 10:
                words.append("ten")
            if int(nums[j]) == 20:
                words.append("twenty")
            if int(nums[j]) == 30:
                words.append("thirty")
            if int(nums[j]) == 40:
                words.append("forty")
            if int(nums[j]) == 50:
                words.append("fifty")
            if int(nums[j]) == 60:
                words.append("sixty")
            if int(nums[j]) == 70:
                words.append("seventy")
            if int(nums[j]) == 80:
                words.append("eighty")
            if int(nums[j]) == 90:
                words.append("ninety")

        if int(nums[j]) > 20 and int(nums[j]) % 10 != 0:
            # j will be 20 for a nums[j] value of 21
            # words.append("twenty" + " " + words[int(nums[j][k - 1]) - 1])
            words.append(words[(int(nums[j][k - 2]) * 10) - 1] + " " + words[int(nums[j][k - 1]) - 1])

    if k == 3:
        if int(nums[j]) % 100 == 0:
            words.append(words[int(nums[j][k - 3]) - 1] + " hundred")
        else:
            words.append(words[(int(nums[j][k - 3]) * 100) - 1] + " and " + words[int("".join([nums[j][k - 2], nums[j][k - 1]])) - 1])

    if k == 4:
            words.append("one thousand")

# print(words)

words2 = []

for q in range(0, len(words)):
    words2.append("".join(words[q].split()))

# print(words2)

print(len("".join(words2)))

