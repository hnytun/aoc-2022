
input=open('inputs/day5.txt', 'r').read().split("\n\n")

instructions = input[1].split('\n')
stacks = input[0]
length = int(stacks[-1][-1])
stacks =  stacks[:stacks.rfind('\n')]
stacks = stacks.replace("["," ").replace("]"," ")
lines = stacks.split('\n')
stackDict = {}

for line in lines:
    for i in range(0, len(line)):
        if not line[i].isspace():
            if i not in stackDict:
                stackDict[i] = list()
                stackDict[i].append(line[i])
            else:
                stackDict[i].append(line[i])

id=1
for key in sorted(stackDict):
    tmp=stackDict[key]

    stackDict.pop(key)
    stackDict[id] = tmp
    id+=1

for instr in instructions:
    split = instr.split(" ")
    amt = int(split[1])
    init = int(split[3])
    to = int(split[5])

    print("move: ", amt, " from ", init, " to", to)
    #remove
    removed = stackDict[init][0:amt]
    stackDict[init] = stackDict[init][amt:]

    #add (part 1)
    #for i in removed:
    #    stackDict[to] = list(i) + stackDict[to]

    #add (part 2)
    stackDict[to] = removed + stackDict[to]

result1 = ""

for key in sorted(stackDict):
    result1 += stackDict[key][0]

print(result1)








