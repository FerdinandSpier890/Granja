# 1) Instalar: pip install PyMySQL

# 2) Importar MySQL
import pymysql
import time


def conexion():
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='LordPeacock890', database='bdejemplo')
        return conn

    except:
        print("Error en la Conexión")
        return None


def insertarGas(gas):
    segundos = time.time()
    hora = time.ctime(segundos)
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sensorgas (sensor, valor, hora) VALUES ('MQ-6', '" + str(gas) + "', '" + hora + "');")
    conn.commit()
    conn.close()
    return True


def insertarTemperatura(temperatura):
    segundos = time.time()
    hora = time.ctime(segundos)
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sensortemperatura (sensor, valor, hora) VALUES ('DHT11', '" + str(
            temperatura) + "', '" + hora + "');")
    conn.commit()
    conn.close()
    return True


def insertarHumedad(humedad):
    segundos = time.time()
    hora = time.ctime(segundos)
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sensorhumedad (sensor, valor, hora) VALUES ('DHT11', '" + str(humedad) + "', '" + hora + "');")
    conn.commit()
    conn.close()
    return True


def consultarListaSensorGas():
    conn = conexion()
    listaSensores = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensorgas;")
    for fila in cursor.fetchall():
        listaSensores.append([fila[0], fila[1], fila[2], fila[3]])
    return listaSensores


def consultarListaSensorGasConValores(id):
    conn = conexion()
    listaSensores = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensorgas WHERE id = '" + id + "';")
    for fila in cursor.fetchall():
        listaSensores.append([fila[0], fila[1], fila[2], fila[3]])
    return listaSensores


def consultarListaSensorTemperatura():
    conn = conexion()
    listaSensores = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensortemperatura;")
    for fila in cursor.fetchall():
        listaSensores.append([fila[0], fila[1], fila[2], fila[3]])
    return listaSensores


def consultarListaSensorTemperaturaConValores(id):
    conn = conexion()
    listaSensores = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensortemperatura WHERE id = '" + id + "';")
    for fila in cursor.fetchall():
        listaSensores.append([fila[0], fila[1], fila[2], fila[3]])
    return listaSensores


def consultarListaSensorHumedad():
    conn = conexion()
    listaSensores = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensorhumedad;")
    for fila in cursor.fetchall():
        listaSensores.append([fila[0], fila[1], fila[2], fila[3]])
    return listaSensores


def consultarListaSensorHumedadConValores(id):
    conn = conexion()
    listaSensores = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensorhumedad WHERE id = '" + id + "';")
    for fila in cursor.fetchall():
        listaSensores.append([fila[0], fila[1], fila[2], fila[3]])
    return listaSensores


def consultarSensores():
    conn = conexion()
    listaSensores = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM componentes;")
    for fila in cursor.fetchall():
        listaSensores.append([fila[0], fila[1], fila[2], fila[3]])
    return listaSensores


if __name__ == '__main__':
    # 3) Hacer la Conexión
    conbd = conexion()
    # estado = insertar(conbd)
    # consultar(conbd)

    resultadoListaSensorGas = consultarListaSensorGas()
    for fila in resultadoListaSensorGas:
        print("{}. El Sensor {} sensó {} el dia {}".format(fila[0], fila[1], fila[2], fila[3]) + "\n")

    resultadoListaSensorTemperatura = consultarListaSensorTemperatura()
    for fila in resultadoListaSensorTemperatura:
        print("{}. El Sensor {} sensó {} el dia {}".format(fila[0], fila[1], fila[2], fila[3]) + "\n")

    resultadoListaSensorHumedad = consultarListaSensorHumedad()
    for fila in resultadoListaSensorHumedad:
        print("{}. El Sensor {} sensó {} el dia {}".format(fila[0], fila[1], fila[2], fila[3]) + "\n")
# 4)
