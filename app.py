import json
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, flash
from flask_cors import cross_origin
from utils.db import *
from utils.validations import * 
import os
import hashlib
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@cross_origin(origin="localhost", supports_credentials=True)
def index():
    donations = get_donation_map()
    requests = get_request_map()
    formatted_donations = []

    for donation in donations:
        formatted_donation = list(donation)
        formatted_donation[4] = donation[4].strftime('%Y-%m-%d')  # Convert the datetime object to a date string
        formatted_donations.append(tuple(formatted_donation))
    donations_json = json.dumps(formatted_donations)
    requests_json = json.dumps(requests)

    return render_template("/MainPages/index.html", donations_json=donations_json, requests_json=requests_json)

@app.route('/add-request', methods=['GET', 'POST'])
def add_request():
    if request.method == 'POST':
        # Get data from the form
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        comuna_id = request.form.get("comuna_id")
        tipo = request.form.get("tipo")
        descripcion = request.form.get("descripcion")
        cantidad = request.form.get("cantidad")
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        celular = request.form.get("celular")      
        error = [] 
        if not validateRegiones(region):
            error.append("Error en la región")
        if not validateComunas(comuna):
            error.append("Error en la comuna")
        if not validateTipo_donacion(tipo):
            error.append("Error en el tipo")
        if not validateDescripcionPedido(descripcion):
            error.append("Error en la descripción")
        if not validateCantidad(cantidad):
            error.append("Error en la cantidad")
        if not validateNombre_donante(nombre):
            error.append("Error en el nombre")
        if not validateEmail(email):
            error.append("Error en el email")
        if not validateCelular(celular):
            error.append("Error en el celular")
        print(error)
        if not error:
            # Connect to the bd and add the request
            conn = get_conn()
            add_a_request(conn, comuna_id, tipo, descripcion, cantidad, nombre, email, celular)
            # Close the connection
            conn.close()
            return redirect(url_for('index'))

    # If the HTTP request is GET, then just show the add request form
    else:
        return render_template('/MainPages/add-request.html')

@app.route('/add-donation', methods=['GET', 'POST'])
def add_donation():
    if request.method == 'POST':
        # Get data from the form
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        comuna_id = request.form.get("comuna_id")
        calle_numero = request.form.get("calle-numero")
        tipo = request.form.get("tipo")
        cantidad = request.form.get("cantidad")
        fecha_disponibilidad = request.form.get("fecha-disponibilidad")
        descripcion = request.form.get("descripcion")
        condiciones_retirar = request.form.get("condiciones")
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        celular = request.form.get("celular")
        photo1 = request.files.get("foto_1")
        photo2 = request.files.get("foto_2")
        photo3 = request.files.get("foto_3")       
        error = [] 
        if not validateRegiones(region):
            error.append("Seleccione alguna región.")
        if not validateComunas(comuna):
            error.append("Seleccione alguna comuna.")
        if not validateCalle_numero(calle_numero):
            error.append("Ingrese una dirección con menos de 80 caracteres.")
        if not validateTipo_donacion(tipo):
            error.append("Ingrese algún tipo entre las opciones.")
        if not validateCantidad(cantidad):
            error.append("Ingrese alguna cantidad inferior o igual a 10 dígitos.")
        if not validateFecha_disponibilidad(fecha_disponibilidad):
            error.append("Ingrese alguna fecha posterior o igual al día actual.")
        if not validateDescripcion(descripcion):
            error.append("Ingrese una descripción con menos de 80 caracteres.")
        if not validateCondiciones(condiciones_retirar):
            error.append("Ingrese sus condiciones en menos de 80 caracteres.")
        if not validateNombre_donante(nombre):
            error.append("El nombre ingresado no es válido.")
        if not validateEmail(email):
            error.append("El email ingresado no es válido.")
        if not validateCelular(celular):
            error.append("El número de celular ingresado no es válido.")
        if not validateFoto1(photo1):
            error.append("Seleccione alguna imagen válida en foto1.")
        if photo2:
            if not validateFoto2(photo2):
                error.append("El archivo en foto2 no es válido.")
        if photo3:
            if not validateFoto2(photo3):
                error.append("El archivo en foto3 no es válido.")
        print(error)
        if not error:
            # Connect to the bd and add the donation
            conn = get_conn()
            donation_id = add_a_donation(conn, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular)
            # Close the connection
            conn.close()
            # This is for the first photo
            # Generate a hash for the photo's name
            _filename = hashlib.sha256(
                secure_filename(photo1.filename).encode("utf-8")
                ).hexdigest()
            _extension = filetype.guess(photo1).extension
            img_filename = f"{_filename}.{_extension}"
        
            # Store the img in the folder
            photo1.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
            
            photo1_url = url_for('uploaded_file', filename=img_filename)
            # ruta_archivo, nombre_archivo, donacion_id
            add_photo(photo1_url, img_filename, donation_id)

            # If there are 2nd and 3rd photo, make the same:
            if photo2:
                _filename = hashlib.sha256(
                secure_filename(photo2.filename).encode("utf-8")
                ).hexdigest()
                _extension = filetype.guess(photo2).extension
                img_filename = f"{_filename}.{_extension}"
                # Store the img in the folder
                photo2.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

                photo2_url = url_for('uploaded_file', filename=img_filename)
                # ruta_archivo, nombre_archivo, donacion_id
                add_photo(photo2_url, img_filename, donation_id)

            if photo3:
                _filename = hashlib.sha256(
                secure_filename(photo3.filename).encode("utf-8")
                ).hexdigest()
                _extension = filetype.guess(photo3).extension
                img_filename = f"{_filename}.{_extension}"
                # Store the img in the folder
                photo3.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

                photo3_url = url_for('uploaded_file', filename=img_filename)
                # ruta_archivo, nombre_archivo, donacion_id
                add_photo(photo3_url, img_filename, donation_id)

            return redirect(url_for('index'))
        else:
            return render_template('/MainPages/add-donation.html', error=error)

    # If the HTTP request is GET, then just show the add donation form
    else:
        return render_template('/MainPages/add-donation.html')


@app.route('/list-requests')
def list_requests():
    total_requests=get_total_requests()
    if not total_requests:
        return redirect(url_for('add_request'))
    # Get the actual page number from the URL
    page = request.args.get('page', default=1, type=int)
    per_page = 5  # Number of donations per page
    if(total_requests%5)==0:
        max_page = total_requests/5
    else:
        max_page = (int(total_requests/5))+1
    if page<1:
        return redirect(url_for('list_requests', page=1))
    if page > max_page:
        return redirect(url_for('list_requests', page=max_page))

    # Calculate the beginning & end index of the showed rows
    start_index = (page - 1) * per_page

    requests=get_requests(start_index, per_page)
    return render_template("/MainPages/list-requests.html", requests=requests, total_requests=total_requests, per_page=per_page, page=page)

@app.route('/list-donations')
def list_donations():
    total_donations=get_total_donations()
    if not total_donations:
        return redirect(url_for('add_donation'))
    # Get the actual page number from the URL
    page = request.args.get('page', default=1, type=int)
    per_page = 5  # Number of donations per page
    if(total_donations%5)==0:
        max_page = total_donations/5
    else:
        max_page = (int(total_donations/5))+1
    if page<1:
        return redirect(url_for('list_donations', page=1))
    if page > max_page:
        return redirect(url_for('list_donations', page=max_page))

    # Calculate the beginning & end index of the showed rows
    start_index = (page - 1) * per_page

    donations=get_donations(start_index, per_page)
    photos = get_photos(start_index, per_page)
    return render_template("/MainPages/list-donations.html", donations=donations, photos=photos, total_donations=total_donations, per_page=per_page, page=page)

@app.route('/request-info')
def request_info():
    urlParams = request.args
    id = urlParams.get('id')
    requests = get_info_request(id)
    return render_template('/TablesDetail/request-info.html', requests=requests)

@app.route('/donation-info')
def donation_info():
    urlParams = request.args
    id = urlParams.get('id')
    donation = get_info_donation(id)
    photo = get_photo_by_id(id)
    amount = get_amount_photos_by_id(id)
    return render_template('/TablesDetail/donation-info.html', donation=donation, photo=photo, amount=amount)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/stats", methods=["GET"])
def stats():
    return render_template('/MainPages/stats.html')

@app.route("/stats-donation", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def stats_donacion():
    donation = get_stats_donations()
    donation = json.dumps(donation)
    return donation

@app.route("/stats-request", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def stats_pedido():
    request = get_stats_requests()
    request = json.dumps(request)
    return request