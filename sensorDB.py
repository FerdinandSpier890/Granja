import pymysql


def conexion():
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='LordPeacock890', database='bdejemplo')
        return conn
    except:
        print("Error en la Conexión")
        return None


def consultarSensores():
    conn = conexion()
    listaSensores = []
    cursor = conn.cursor()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM componentes;")
        listaSensores = cursor.fetchall()
    conn.close()
    return listaSensores


def consultarSensorPorId(id):
    conn = conexion()
    sensor = None
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, nombre, descripcion, fabricante FROM componentes WHERE id = %s", (id,))
        sensor = cursor.fetchone()
    conn.close()
    return sensor


def actualizarSensor(nombre, descripcion, fabricante, id):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE componentes SET nombre = %s, descripcion = %s, fabricante = %s WHERE id = %s",
                       (nombre, descripcion, fabricante, id))
        conn.commit()
    conn.close()
    return "Registro actualizado"


def insertarIoT(gas, temperatura, humedad):
    conn = conexion()
    query = "INSERT INTO iot (gas, temperatura, humedad) VALUES ('" + gas + "', '" + temperatura + "', '" + humedad + "'); "
    cursor = conn.cursor()
    cursor.execute(query)
    # print(query)
    conn.commit()
    conn.close()
    return "Registro Guardado"


def consultarIoT():
    conn = conexion()
    liot = []
    cursor = conn.cursor()
    query = "SELECT * FROM iot;"
    with conn.cursor() as cursor:
        cursor.execute(query)
        liot = cursor.fetchall()
    conn.close()
    return liot
