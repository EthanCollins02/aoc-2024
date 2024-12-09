grid = []
count = 0
while True:
    try:
        line = input()
        grid.append(line)
    except:
        break
for x in range(len(grid)-2):
    for y in range(len(grid[x])-2):
        if ''.join((grid[x][y] + grid[x][y+2] + grid[x+1][y+1] + grid[x+2][y] + grid[x+2][y+2])) in ["MMASS", "MSAMS", "SSAMM", "SMASM"]:
            count+= 1
print(count)