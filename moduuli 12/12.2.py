import json
import requests
uinput = input("Anna paikkakuntasi nimi:")
api_key = "d4f39d15e382ded1516350b162e173a4"
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={uinput}&appid={api_key}"
vastaus = requests.get(pyyntö).json()

if vastaus.get('cod') == 200:
    sää = vastaus["weather"][0]["description"]
    celsius = vastaus["main"]["temp"]-273.15
    print(f"Kaupungissa {uinput} lämpötila on {celsius:.2f} C")
    print(f"kuvaus säälle: {sää}")
else:
    print('Hakusanaasi vastaavaa paikkakuntaa ei löytynyt. Tarkista kirjoitusasu')

