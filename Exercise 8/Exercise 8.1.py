import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_games',
         user='duy',
         password='123',
         autocommit=True
         )
def apicao(code):
    # sql = f"select airport.name, country.name from airport, country where ident='{code}' and country.iso_country = airport.iso_country "
    sql = f"select name, municipality from airport where ident = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return print(result)
while True:
    code = input('Enter ICAO code: ')
    if code == "":
        break
    apicao(code)



