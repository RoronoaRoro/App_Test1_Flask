from flask import app
import pymysql

DB_NAME = "App_Test1_Flask"
DB_USERNAME = "test_user"
DB_PASSWORD = "testpassword"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

def add_a_donation(c,comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular):
    sql = "INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor = c.cursor()
    try:
        result = cursor.execute(sql, (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular))
        c.commit()
        donation_id = cursor.lastrowid
        if result == 1:
            return donation_id
        else: return False
    except pymysql.Error as e:
        app.logger.error("Error con base de datos: {}".format(str(e)))
    return False

def add_a_request(c,comuna_id, tipo, descripcion, cantidad, nombre, email, celular):
    sql = "INSERT INTO pedido (comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor = c.cursor()
    try:
        result = cursor.execute(sql, (comuna_id, tipo, descripcion, cantidad, nombre, email, celular))
        c.commit()
        request_id = cursor.lastrowid
        if result == 1:
            return request_id
        else: return False
    except pymysql.Error as e:
        app.logger.error("Error con base de datos: {}".format(str(e)))
    return False

def add_photo(ruta, nombre, idd):
    sql = "INSERT INTO foto (ruta_archivo, nombre_archivo, donacion_id) VALUES (%s, %s, %s);"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (ruta, nombre, idd))
    conn.commit()

def get_donations(inf_limit, sup_limit):
    sql = "SELECT donacion.id, comuna.nombre, donacion.tipo, donacion.cantidad, donacion.fecha_disponibilidad, donacion.nombre FROM donacion JOIN comuna ON donacion.comuna_id = comuna.id ORDER BY donacion.id DESC LIMIT %s,%s;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (inf_limit, sup_limit))
    donations = cursor.fetchall()
    return donations

def get_requests(inf_limit, sup_limit):
    sql = "SELECT pedido.id, comuna.nombre as comuna, pedido.tipo, pedido.descripcion, pedido.cantidad, pedido.nombre_solicitante FROM pedido JOIN comuna ON pedido.comuna_id = comuna.id ORDER BY pedido.id DESC LIMIT %s,%s;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (inf_limit, sup_limit))
    requests = cursor.fetchall()
    return requests

def get_photos(inf_limit, sup_limit):
    sql = "SELECT fotos.ruta_archivo FROM (SELECT MIN(ruta_archivo) AS ruta_archivo, donacion_id, MIN(id) AS id FROM foto GROUP BY donacion_id ORDER BY donacion_id DESC) AS fotos LIMIT %s, %s;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (inf_limit, sup_limit))
    photos = cursor.fetchall()
    return photos

def get_total_donations():
    sql="SELECT COUNT(*) FROM (SELECT donacion.id, comuna.nombre as comuna, donacion.tipo, donacion.cantidad, donacion.fecha_disponibilidad, donacion.nombre FROM donacion JOIN comuna ON donacion.comuna_id = comuna.id) as donaciones;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    total_donations = cursor.fetchone()[0]
    return total_donations

def get_total_requests():
    sql="SELECT COUNT(*) FROM pedido;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    total_requests = cursor.fetchone()[0]
    return total_requests

def get_info_donation(idd):
    sql = "SELECT regiones.nombre AS region, comuna.nombre AS comuna, donacion.calle_numero, donacion.tipo, donacion.cantidad, donacion.fecha_disponibilidad, donacion.descripcion, donacion.condiciones_retirar, donacion.nombre, donacion.email, donacion.celular FROM donacion JOIN comuna on donacion.comuna_id=comuna.id JOIN (SELECT region.nombre, comuna.id FROM region JOIN comuna ON region.id=comuna.region_id) AS regiones ON donacion.comuna_id=regiones.id WHERE donacion.id = %s;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (idd))
    donation = cursor.fetchone()
    return donation

def get_info_request(id):
    sql = "SELECT regiones.nombre AS region, comuna.nombre AS comuna, pedido.tipo, pedido.descripcion, pedido.cantidad, pedido.nombre_solicitante, pedido.email_solicitante, pedido.celular_solicitante FROM pedido JOIN comuna on pedido.comuna_id=comuna.id JOIN (SELECT region.nombre, comuna.id FROM region JOIN comuna ON region.id=comuna.region_id) AS regiones ON pedido.comuna_id=regiones.id WHERE pedido.id = %s;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    request = cursor.fetchone()
    return request

def get_donation_map():
    sql ="SELECT donacion.id, donacion.calle_numero, donacion.tipo, donacion.cantidad, donacion.fecha_disponibilidad, donacion.email, comuna.nombre FROM donacion JOIN comuna ON donacion.comuna_id = comuna.id ORDER BY donacion.id DESC LIMIT 5;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    donation = cursor.fetchall()
    return donation

def get_request_map():
    sql ="SELECT pedido.id, pedido.tipo, pedido.cantidad, pedido.email_solicitante, comuna.nombre FROM pedido JOIN comuna ON pedido.comuna_id = comuna.id ORDER BY pedido.id DESC LIMIT 5;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    request = cursor.fetchall()
    return request

def get_stats_donations():
    sql = "SELECT tipo, COUNT(*) AS total FROM donacion GROUP BY tipo;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    donation = cursor.fetchall()
    return donation

def get_stats_requests():
    sql = "SELECT tipo, COUNT(*) AS total FROM pedido GROUP BY tipo;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    request = cursor.fetchall()
    return request

def get_photo_by_id(id):
    sql ="SELECT ruta_archivo FROM foto WHERE donacion_id = %s;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    photos = [row[0] for row in cursor.fetchall()]
    return photos

def get_amount_photos_by_id(id):
    sql ="SELECT COUNT(*) FROM foto WHERE donacion_id = %s;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    amount = cursor.fetchone()[0]
    return amount