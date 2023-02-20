from flask import request, render_template, Flask

import sensorDB

app = Flask(__name__)


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
