num = int(input('Enter the number: '))
if num < 3:
    print(f'The number {num} is not prime')
else:
    for i in range(2, num):
        if num % i ==0:
            print(f'The number {num} is not prime')
            break
    else:
        print(f'The number {num} is prime')



