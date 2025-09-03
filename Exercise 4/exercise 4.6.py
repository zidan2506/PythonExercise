import random
a = int(input(f'\033[031mIt would be more than 9999 for exact answer!\033[0m\nhow many random points to generate?  '))
N = []
n = []
for i in range(a):
    x = random.random()
    y = random.random()
    list1 = (x,y)
    N.append(list1)
    if x**2 + y**2 < 1:
        n.append(list)
print(f'Pi = {(4*len(n))/len(N)}')

