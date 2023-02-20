import pymysql


def conexion():
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='LordPeacock890', database='bdejemplo')
        return conn
    except:
        print("Error en la Conexión")


def insertarGallinas(altura, peso, raza):
    conn = conexion()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO gallinas(altura, peso, raza) values('" + altura + "', '" + peso + "', '" + raza + "');")

    conn.commit()
    conn.close()
    return "Gallina Registrada"


def consultarGallinas():
    conn = conexion()
    lgallinas = []
    cursor = conn.cursor()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM gallinas;")
        lgallinas = cursor.fetchall()
    conn.close()
    return lgallinas


def consultarGallinaPorId(id):
    conn = conexion()
    gallina = None
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, altura, peso, raza FROM gallinas WHERE id = %s", (id,))
        gallina = cursor.fetchone()
    conn.close()
    return gallina


def actualizarGallina(altura, peso, raza, id):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE gallinas SET altura = %s, peso = %s, raza = %s WHERE id = %s ", (altura, peso, raza, id))
    conn.commit()
    conn.close()
    return "Gallina Actualizada"


def eliminarGallina(id):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM gallinas WHERE id = %s", (id))
    conn.commit()
    conn.close()
