# Liters=Gallons×3.78541
def gasoline():
   return gas * 3.78541
while True:
    gas = float(input("Enter the negative value to stop: "))
    if gas > 0:
        print(f'{gas} Gallons is equal to {gasoline():.2f} Litres')
    else:
        print(f'STOPPED')
        break