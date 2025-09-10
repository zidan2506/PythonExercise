import random
a = int(input('How many dice to row ? '))
total = 0

for i in range(a):
    b = random.randint(1, 6)
    total = total +b
print(total)



