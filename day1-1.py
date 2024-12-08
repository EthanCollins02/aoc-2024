leftList = []
rightList = []
line = ""
while line is not None:
    try:
        line = input().split()
        leftList.append(int(line[0]))
        rightList.append(int(line[1]))
    except:
        line = None
leftList.sort()
rightList.sort()

totalDist = 0
for x, num in enumerate(leftList):
    totalDist += abs(num - rightList[x])

print(totalDist)
