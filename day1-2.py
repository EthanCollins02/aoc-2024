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

similarityScore = 0
for num in leftList:
    occurances = 0
    for num2 in rightList:
        if num == num2:
            occurances += 1
    similarityScore += occurances * num

print(similarityScore)
