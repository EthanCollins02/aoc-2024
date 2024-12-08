import re
line = ""
total = 0
while line is not None:
    try:
        line = input()
        instructions = re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", line)
        for instruction in instructions:
            total += int(instruction[4:instruction.find(",")]) * int(instruction[instruction.find(",")+1:instruction.find(")")])
    except Exception as e:
        line = None
print(total)
