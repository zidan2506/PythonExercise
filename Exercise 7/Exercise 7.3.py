dict = {}

while True:
    action = input("(new/data/exit)\nEnter your action: ")
    if action == "new":
        name = input("Enter the name of the airport: ")
        code = input("Enter the ICAO code: ")

        dict.update({code:name})
        print(dict)
    if action == "data":
        choose = input("Enter ICAO code: ")
        a = dict.get(choose)
        print(f'Airport name:  {a}')
    if action == "exit":
        break