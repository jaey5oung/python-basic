myNums = {}
for i in range(4):
    num = input((i+1))
    myNums[num] = num[-1]
for i in sorted(myNums.values()):
    print(i)
