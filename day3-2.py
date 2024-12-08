import re
line = ""
total = 0
enabled = True
nextline = ""
while nextline is not None:
    try:
        nextline = input()
        line = line + nextline
    except:
         nextline = None
sections = line.split("don't()")
instructions = re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", sections[0])
for instruction in instructions:
    total += int(instruction[4:instruction.find(",")]) * int(instruction[instruction.find(",")+1:instruction.find(")")])
for section in sections:
    startIndex = section.find("do()") + 4
    if startIndex == 3:
        continue
    instructions = re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", section[startIndex:])
    for instruction in instructions:
        total += int(instruction[4:instruction.find(",")]) * int(instruction[instruction.find(",")+1:instruction.find(")")])
print(total)
