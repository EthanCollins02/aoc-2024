from functools import cmp_to_key

def compare(num1, num2):
    if num1 in preceedRules:
        if num2 in preceedRules[num1]:
            return 1
    if num2 in preceedRules:
        if num1 in preceedRules[num2]:
            return -1
    if num1 in followRules:
        if num2 in followRules[num1]:
            return -1
    if num2 in followRules:
        if num1 in followRules[num2]:
            return 1

followRules = {}
preceedRules = {}
inRules = True
count = 0
while True:
    try:
        line = input()
        if len(line) < 3:
            inRules = False
        if inRules:
                if line[:line.find("|")] not in followRules:
                    followRules[line[:line.find("|")]] = []     
                followRules[line[:line.find("|")]].append(line[line.find("|")+1:])

                if line[line.find("|")+1:] not in preceedRules:
                     preceedRules[line.find("|")+1:] = []
                preceedRules[line.find("|")+1:].append(line[:line.find("|")])
        else:
            instructions = line.split(",")
            if len(instructions) == 1:
                 continue
            # print(instructions)
            bad = False
            for x, instruction in enumerate(instructions):
                if instruction in followRules:
                    if not all(item in followRules[instruction] for item in instructions[x+1:]) or not all(item not in followRules[instruction] for item in instructions[:x]):
                    #   print("bad")
                      bad = True
                      break
                    # else:
                        # print("follow",instruction,followRules[instruction], instructions[x+1:])
                
                if instruction in preceedRules:
                    if not all(item in preceedRules[instruction] for item in instructions[:x]) or not all(item not in preceedRules[instruction] for item in instructions[x+1:]):
                    #   print("bad")
                      bad = True
                      break
                    # else:
                        #  print("preceed",instruction, preceedRules[instruction], instructions[:x])
            if bad:
                sortedInstructions = sorted(instructions, key=cmp_to_key(compare))
                print(sortedInstructions)
                count += int(sortedInstructions[int(len(sortedInstructions)/2)])
    except Exception as e:
        # print(e)
        break
print(count)