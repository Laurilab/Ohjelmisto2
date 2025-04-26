import mysql.connector
from flask import Flask, Response
import json

connection = mysql.connector.connect(
    host='127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'lauri1',
    password = 'salis1',
    charset = 'utf8mb4',
    collation= 'utf8mb4_general_ci',
    autocommit = True
)

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def get_airport(icao):
    try:
        code = icao
        sql=(f'SELECT airport.name, municipality '
             f" FROM airport "
             f" where airport.ident = '{code}' ")
        cursor = connection.cursor()
        cursor.execute(sql)
        sql_result = cursor.fetchall()

        status_code = 200
        result = {
            "status_code": status_code,
            "ICAO": code,
            "Name": sql_result[0][0],
            "Municipality": sql_result[0][1]
        }

    except ValueError:
        status_code = 400
        result = {
            "status_code": status_code,
            "teksti": "Virheellinen ICAO"
        }






    jsonvast = json.dumps(result)
    return Response(response=jsonvast, status=status_code, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)



