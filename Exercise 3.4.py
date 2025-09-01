year = int(input("Enter year: "))
if year%4==0 or (year%100!=0 and year%400==0):
    print('Your year is a leap year')
else:
    print('Your year is not a leap year')