import mysql.connector
from geopy.distance import geodesic  # cần cài geopy trước

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_games',
    user='duy',
    password='123',
    autocommit=True
)

def coordinates(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cur = connection.cursor()
    cur.execute(sql, (icao,))
    row = cur.fetchone()
    cur.close()
    return row

def distance(code1, code2):
    coords1 = coordinates(code1)
    coords2 = coordinates(code2)

    if not coords1 or not coords2:
        return None


    return geodesic(coords1, coords2).kilometers

while True:
    code1 = input("Enter first ICAO code: ").strip().upper() #strip() -> remove the space at the begin and end
    if code1 =="":
        break
    code2 = input("Enter second ICAO code: ").strip().upper()
    if code2 == "":
        break

    dist = distance(code1, code2)
    if dist is None:
        print("One or both ICAO codes not found.")
    else:
        print(f"Distance between {code1} and {code2}: {dist:.2f} km")
