import math
pi = math.pi
def pizza(diameter, price):
    area = pi*(diameter/200)**2
    return  price/area
# lm = 2
# while lm !=0:
    # lm -=1
piz1 = pizza(float(input('Enter the diameter of the pizza: ')), float(input('Enter the price of the pizza: ')))
piz2 = pizza(float(input('Enter the diameter of the pizza: ')), float(input('Enter the price of the pizza: ')))
print(f'The unit prize per square metre of the first pizza is {piz1:.2f} EURO/m^2')
print(f'The unit prize per square metre of the second pizza is {piz2:.2f} EURO/m^2')
if piz1 < piz2:
        print(f'The first pizza provides better value for money than the second one.')
else:
        print(f'The second pizza provides better value for money than the first one.')
