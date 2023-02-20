from flask import Flask, render_template, request, redirect

import main
import sensorDB

app = Flask(__name__)


@app.route("/")
@app.route("/clista")
def consulta():
    lista = sensorDB.consultarSensores()
    return render_template("listaSensor.html", datos=lista)


@app.route("/formulario_actualizar_dato/<int:id>")
def editar_dato(id):
    lista = sensorDB.consultarSensorPorId(id)
    return render_template("actualizarSensor.html", dato=lista)


@app.route("/actualizar_dato", methods=["POST"])
def actualizar_dato():
    id = request.form['id']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    fabricante = request.form['fabricante']
    estado = sensorDB.actualizarSensor(nombre, descripcion, fabricante, id)

    return redirect("/clista")


@app.route("/monitoreo")
def monitoreo():
    main.index()
    return render_template("index.html")


@app.route("/glista")
def gallinas():
    gallinas.consulta()
    return render_template("listaGallinas.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
