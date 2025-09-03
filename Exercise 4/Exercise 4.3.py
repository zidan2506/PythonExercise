a = input("Enter number: ")
b = []
b.append(a)
while a != '':
    a= input("Enter number: ")
    b.append(a)
num = [x for x in b if x != ""]
print(f'The largest number is: {max(num)}')
print(f'The smallest number is: {min(num)}')