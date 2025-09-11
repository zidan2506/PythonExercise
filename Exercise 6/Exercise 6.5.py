def num(lst):
    for i in lst:
        if i % 2 ==0:
            lst2.append(i)

    return f'Original list is {lst}\nCut-down list is {lst2}'
lst = []
lst2 = []
while True:
    a =(input('Enter an integer:  '))
    if a == '':
        print(num(lst))
        break
    lst.append(int(a))
