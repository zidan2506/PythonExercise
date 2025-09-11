import random
def roll(sides):
    return random.randint(1,sides)
result = 0
sides = int(input('How many sides? '))

while result != sides:
    result = roll(sides)
    print(result)

