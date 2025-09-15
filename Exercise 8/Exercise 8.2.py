import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_games',
         user='duy',
         password='123',
         autocommit=True
         )
def country(code):
    # sql = f"select airport.name, country.name from airport, country where ident='{code}' and country.iso_country = airport.iso_country "
    sql = f"select name, type from airport where iso_country = '{code}' order by type"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)
while True:
    code = input('Enter country code: ')
    if code == "":
        break
    country(code)



