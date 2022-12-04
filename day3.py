
input=open('inputs/day3.txt', 'r').read().splitlines()

def get_priority(char):
    return ord(char)-38 if char.isupper() else ord(char)-96

def find_duplicate(comp1,comp2,comp3=None):
    if comp3 == None:
        for char in comp1:
            if(char in comp2):
                return char
    else:
        for char in comp1:
            if(char in comp2 and char in comp3):
                return char

sum=0
for line in input:
    first=line[0:(int(len(line)/2))]
    second=line[(int(len(line)/2)):len(line)]
    sum += get_priority(find_duplicate(first,second))

sum2=0
groups = list(zip(*(iter(input),) * 3))
for group in groups:
    sum2+=get_priority(find_duplicate(group[0],group[1],group[2]))

print("part1: ",sum)
print("part2:",sum2)