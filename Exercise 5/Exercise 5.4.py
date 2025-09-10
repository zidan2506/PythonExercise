limit = 5
lst = []
for i in range(limit):
    a = (input('Enter the country: '))
    lst.append(a)
    if limit == 0:

        break
print(f'The cities are:')
for x in lst:
    print(x)
