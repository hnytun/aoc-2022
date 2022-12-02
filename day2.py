file1 = open('inputs/day2_sample.txt', 'r').read()
rounds = file1.split("\n")

def evalscore(opponent,you):
    """
    #opponent
    rock A
    paper B
    sciccors C
    #you
    rock X - 1
    paper Y - 2
    sciccors Z - 3
    """
    if(opponent == 'A' and you == 'X'):
        return 3+1
    elif(opponent == 'A' and you == 'Y'):
        return 6+2
    elif(opponent == 'A' and you=='Z'):
        return 0+3

    elif(opponent == 'B' and you == 'X'):
        return 0+1
    elif(opponent == 'B' and you == 'Y'):
        return 3+2
    elif(opponent == 'B' and you == 'Z'):
        return 6+3

    elif(opponent == 'C') and you=='X':
        return 6+1
    elif(opponent == 'C') and you=='Y':
        return 0+2
    elif(opponent == 'C') and you=='Z':
        return 3+3

def findWinnerhand(opponent):
    if(opponent == 'A'):
        return 'Y'
    elif(opponent == 'B'):
        return 'Z'
    elif(opponent == 'C'):
        return 'X'

def findDrawhand(opponent):
    if(opponent == 'A'):
        return 'X'
    elif(opponent == 'B'):
        return 'Y'
    elif(opponent == 'C'):
        return 'Z'

def findLosinghand(opponent):
    if(opponent == 'A'):
        return 'Z'
    elif(opponent == 'B'):
        return 'X'
    elif(opponent == 'C'):
        return 'Y'

def decideOutcome(you):
    if(you == 'X'):
        return -1
    elif(you == 'Y'):
        return 0
    elif(you=='Z'):
        return 1

totalscore=0
totalscore2=0
for round in rounds:
    round = round.split(' ')
    totalscore += (evalscore(round[0],round[1]))

    if(decideOutcome(round[1]) == 0):
        totalscore2 += evalscore(round[0],findDrawhand(round[0]))
    elif(decideOutcome(round[1]) == 1):
        totalscore2 += evalscore(round[0],findWinnerhand(round[0]))
    elif(decideOutcome(round[1]) == -1):
        totalscore2 += evalscore(round[0],findLosinghand(round[0]))


print("part 1: ", totalscore)
print("part 2: ", totalscore2)
