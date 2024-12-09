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
            if not bad:
                count += int(instructions[int(len(instructions)/2)])
            print()
    except Exception as e:
        # print(e)
        break
print(count)