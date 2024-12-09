import re
grid = []
count = 0
while True:
    try:
        line = input()
        count += len(re.findall(r"XMAS", line)) + len(re.findall(r"SAMX", line))
        grid.append(line)
    except:
        break
for x in range(len(grid)-3):
    for y in range(len(grid[x])):
        column = grid[x][y] + grid[x+1][y] + grid[x+2][y] + grid[x+3][y]
        if column == "XMAS" or column == "SAMX":
            count += 1
        if y < len(grid[x])-3:
            rightDiag = grid[x+3][y] + grid[x+2][y+1] + grid[x+1][y+2] + grid[x][y+3]
            leftDiag = grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2] + grid[x+3][y+3]
            if rightDiag in ["XMAS","SAMX"]:
                count +=1
            if leftDiag in ["XMAS","SAMX"]:
                count += 1
print(count)
