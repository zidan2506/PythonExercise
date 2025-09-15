tuple = 'Winter','Spring','Summer','Fall'
def check(x):
    if x in range(3,6):
        print(f'Your month is in the {tuple[1]} term')
    elif x in range(6,9):
        print(f'Your month is in the {tuple[2]} term')
    elif x in range(9,12):
        print(f'Your month is in the {tuple[3]} term')
    else:
        print(f'Your month is in the {tuple[0]} term')
while True:
    month = (input('Enter the month: '))
    if month == '':
        break
    x = int(month)
    check(x)
