a = input('Enter the number: ')
b = []
c = []
while a != "":
    b.append(a)
    a = input('Enter the number: ')
for i in b:
    c.append(int(i))
c.sort(reverse=True)
print(c[0:5])










# b = []
# while True:
#     a = input('Enter the number: ')
#     if a == '':
#         break
#     b.append(int(a))
# b.sort(reverse=True)
# print(b[:5])