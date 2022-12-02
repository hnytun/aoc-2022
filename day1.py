file1 = open('inputs/day1.txt', 'r')
meals = file1.read().split('\n')

elfCalories=list()
cals=0
for meal in meals:
    if(meal != ''):
        cals += int(meal)
    else:
        elfCalories.append(cals)
        cals=0

print("part one:")
print(max(elfCalories))

print("part two:")
print(sum(sorted(elfCalories, reverse=True)[:3]))
