from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:

        luku = int(luku)
        if luku <= 1:
            value = False
        else:
            for i in range(2, luku):
                if luku % i == 0:
                    value = False
                    break
            else:
                value = True


        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "Number": luku,
            "isprime": value
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen syöte"
        }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

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
