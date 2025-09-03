createuser = input('Create your Username: ')
createpass = input('Create your Password: ')
limit = 0
while limit != 5:
    user = input('Enter your Username: ')
    password = input('Enter your Password: ')
    limit += 1
    if user == createuser and password == createpass:
        print('welcome')
    elif user != createuser and password != createpass:
        print('wrong pass or user name\nPls try again')
print('Access Denied')
