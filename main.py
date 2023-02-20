# 1) Instalar flask: pip install flask
# 2) Activar entorno: venv\Scripts\activate
# 3) Instalar requests: pip install requests uwu

import serial
import time
# 4) Importar flask:
from flask import Flask, render_template, request

import bdWeb
# 5) Configuraciones de flask para la app web
import gallinas
import sensor
import sensorDB

app = Flask(__name__)


# 6) Decoradores

@app.route("/")
def index():
    arduino = serial.Serial('COM6', 9600)
    time.sleep(2)
    global r1
    global r2
    global r3

    while True:
        cad1 = arduino.readline().decode('utf-8')
        cad2 = arduino.readline().decode('utf-8')
        cad3 = arduino.readline().decode('utf-8')

        r1 = cad1
        r2 = cad2
        r3 = cad3

        gas = cad1.index(' ')
        labelgas = cad1[:gas]
        valuegas = cad1[gas + 1:]
        bdWeb.insertarGas(r3)

        temperatura = cad2.index(' ')
        labeltemperatura = cad2[:temperatura]
        valuetemperatura = cad2[temperatura + 1:]
        bdWeb.insertarTemperatura(r1)

        humedad = cad3.index(' ')
        labelhumedad = cad3[:humedad]
        valuehumedad = cad3[humedad + 1:]
        bdWeb.insertarHumedad(r2)

        if labeltemperatura == 'T':
            labeltemperatura = '''La temperatura es de: {}'''.format(valuetemperatura)

        if labelhumedad == 'H':
            labelhumedad = '''La humedad es de: {}'''.format(valuehumedad)

        if labelgas == 'G':
            labelgas = '''La presencia de gas es de: {}'''.format(valuegas)

        return render_template("index.html", ga=r1, temp=r2, hum=r3)


@app.route("/listaGas")
def consultarGas():
    listaSensorGas = []
    listaSensorGas = bdWeb.consultarListaSensorGas()
    return render_template("gas.html", listaSensorGas=listaSensorGas)


@app.route("/consultaGas", methods=["POST"])
def consultarGasPorValor():
    id = request.form['id']
    listaSensorGas = bdWeb.consultarListaSensorGasConValores(id)
    return render_template("gas.html", listaSensorGas=listaSensorGas)


@app.route("/listaTemperatura")
def consultarTemperatura():
    listaSensorTemperatura = []
    listaSensorTemperatura = bdWeb.consultarListaSensorTemperatura()
    return render_template("temperatura.html", listaSensorTemperatura=listaSensorTemperatura)


@app.route("/consultaTemperatura", methods=["POST"])
def consultarTemperaturaPorValor():
    id = request.form['id']
    listaSensorTemperatura = bdWeb.consultarListaSensorTemperaturaConValores(id)
    return render_template("temperatura.html", listaSensorTemperatura=listaSensorTemperatura)


@app.route("/listaHumedad")
def consultarHumedad():
    listaSensorHumedad = []
    listaSensorHumedad = bdWeb.consultarListaSensorHumedad()
    return render_template("humedad.html", listaSensorHumedad=listaSensorHumedad)


@app.route("/consultaHumedad", methods=["POST"])
def consultarHumedadPorValor():
    id = request.form['id']
    listaSensorHumedad = bdWeb.consultarListaSensorHumedadConValores(id)
    return render_template("humedad.html", listaSensorHumedad=listaSensorHumedad)


@app.route("/clista")
def sensores():
    sensor.consulta()
    return render_template("listaSensor.html")


@app.route("/glista")
def gallinas():
    gallinas.consulta()
    return render_template("listaGallinas.html")


@app.route("/esp8266", methods=["POST"])
def esp8266():
    gas = request.form['gas']
    temperatura = request.form['temperatura']
    humedad = request.form['humedad']
    registro = sensorDB.insertarIoT(gas, temperatura, humedad)
    return registro


@app.route("/cesp8266")
def consultaESP8266():
    lista = sensorDB.consultarIoT()
    return render_template("lista_esp8266.html", datos=lista)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
