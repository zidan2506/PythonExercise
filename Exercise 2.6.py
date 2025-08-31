import random
# a = random.randint(0,9)
# b = random.randint(0,9)
# c = random.randint(0,9)
# d = random.randint(1,6)
# e = random.randint(1,6)
# f = random.randint(1,6)
# print(f'3-digit code is {a,b,c}')
# print(f'4 -digit code is {d,e,f}')
a = [random.randint(0,9) for _  in range(3)]
b = [random.randint(1,6) for _  in range(3)]
print(f'3-digit code is {a}')
print(f'4 -digit code is {b}')


