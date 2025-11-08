from flask import Flask, Response
import requests, mysql.connector,json
app = Flask(__name__)
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flightgame',
         user='mon',
         password='1234',
         autocommit=True
)

@app.route('/airport/<icao>')
def get_data(icao):
    ICAO = icao.strip().upper()

    try:
        sql = f"select name, municipality from airport where ident = '{ICAO}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        response = {
            "ICAO":ICAO,
            "Name":result[0][0],
            "Location":result[0][1]
        }
        return response
    except IndexError:
        response = {
            'message': "Invalid ICAO code provided",
            'status': 404,
        }
        res_json = json.dumps(response)
        res_html = Response(response=res_json,status=404,mimetype="application/json")
        return res_html

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message":"Invalid endpoint",
        "status":404
    }
    res_json = json.dumps(response)
    res_html = Response(response=res_json,status=404,mimetype="application/json")
    return res_html
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

