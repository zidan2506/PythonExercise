import random
a = random.randint(1,10)
b = -10
while a != b:
    b = int(input("Enter the number: "))
    if b > a:
        print('Too high')
    elif b < a:
        print('Too low')
print('Correct')
