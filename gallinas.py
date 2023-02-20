from flask import Flask, render_template, request, redirect
import gallinasDB, main
import sensor

app = Flask(__name__)


@app.route("/")
@app.route("/glista")
def consulta():
    lista = gallinasDB.consultarGallinas()

    return render_template("listaGallinas.html", datos=lista)


@app.route("/formulario_editarGallinas/<int:id>")
def editarGallinas(id):
    lista = gallinasDB.consultarGallinaPorId(id)
    return render_template("actualizarGallinas.html", dato=lista)


@app.route("/actualizarGallinas", methods=["POST"])
def actualizarGallinas():
    id = request.form["id"]
    altura = request.form["altura"]
    peso = request.form["peso"]
    raza = request.form["raza"]
    estado = gallinasDB.actualizarGallina(altura, peso, raza, id)
    return redirect("/glista")


@app.route("/eliminarGallinas/<int:id>", methods=["GET"])
def eliminarGallinas(id):
    gallinasDB.eliminarGallina(id)
    return redirect("/glista")


@app.route("/insertarGallinas")
def insertarGallinas():
    return render_template("insertarGallinas.html")


@app.route("/insertarGallinasBD", methods=["POST"])
def insertarGallinasBD():
    altura = request.form["altura"]
    peso = request.form["peso"]
    raza = request.form["raza"]
    gallinasDB.insertarGallinas(altura, peso, raza)
    return redirect("/glista")


@app.route("/monitoreo")
def monitoreo():
    main.index()
    return render_template("index.html")


@app.route("/clista")
def sensores():
    sensor.consulta();
    return render_template("listaSensor.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
