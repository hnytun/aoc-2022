
input=open('inputs/day4.txt', 'r').read().splitlines()

amt=0
amt2=0
for line in input:
    ranges=line.split(",")
    range1 = range(int(ranges[0].split("-")[0]),int(ranges[0].split("-")[1])+1)
    range2 = range(int(ranges[1].split("-")[0]),int(ranges[1].split("-")[1])+1)
    if len(list(set(range1) & set(range2))) != 0:
        amt2+=1
    if set((range2)).issubset(range1):
        amt+=1
        continue
    if set((range1)).issubset(range2):
        amt+=1

print("part1: ", amt)
print("part2: ",amt2)
