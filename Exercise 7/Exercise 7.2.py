set = set()
while True:
    set1 = input('Enter the name: ')
    if set1 == '':
        for i in set:
            print(i)
        break
    if set1 in set:
        print('EXISTING NAME')
    else:
        print('NEW NAME')
    set.add(set1)
