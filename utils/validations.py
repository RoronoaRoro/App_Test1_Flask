import datetime
import re 
import filetype

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def validateRegiones(regiones):
    if not regiones:
        return False
    return True

def validateComunas(comunas):
    if not comunas:
        return False
    return True

def validateCalle_numero(calle_numero):
    if not calle_numero:
        return False
    lengthValid = len(calle_numero) <= 80
    return lengthValid

def validateTipo_donacion(tipo_donacion):
    valores_posibles = ['Fruta', 'Verdura', 'Otro']
    return tipo_donacion in valores_posibles

def validateCantidad(cantidad):
    if not cantidad:
        return False
    lengthValid = len(cantidad) <= 10
    return lengthValid

def validateFecha_disponibilidad(fecha_disponibilidad):
    if not fecha_disponibilidad:
        return False
    fechaHoy = datetime.date.today()
    fechaIntroducida = datetime.datetime.strptime(fecha_disponibilidad, "%Y-%m-%d").date()
    esValida = fechaIntroducida >= fechaHoy

    regex = re.compile(r"202[3-9]-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$")
    formatValid = regex.match(fecha_disponibilidad)
    return bool(formatValid) and esValida

def validateDescripcion(descripcion):
    if not descripcion:
        return True
    lengthValid = len(descripcion) <= 80
    return lengthValid

def validateDescripcionPedido(descripcion):
    if not descripcion:
        return False
    lengthValid = len(descripcion) <= 80
    return lengthValid

def validateCondiciones(condiciones):
    if not condiciones:
        return True
    lengthValid = len(condiciones) <= 80
    return lengthValid

def validateNombre_donante(nombre_donante):
    if not nombre_donante:
        return False
    lengthValid = 3 <= len(nombre_donante) <= 80
    return lengthValid

def validateEmail(email):
    if not email:
        return False
    # format validation
    regex = re.compile(r'^[\w\.]+@([\w]+\.)+[\w]{2,3}$')
    formatValid = regex.match(email)
    lengthValid = len(email) <= 80

    # return logic AND of validations.
    return bool(formatValid) and lengthValid

def validateCelular(celular):
    if not celular:
        return True
    # format validation
    regex = re.compile(r'[+]569 [0-9]{8}$')
    formatValid = regex.match(celular)
    lengthValid = len(celular) <= 15

    # return logic AND of validations.
    return bool(formatValid) and lengthValid

def validateFoto1(files):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if files is None:
        return False

    # check if the browser submitted an empty file
    if files.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(files)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    
    if files.content_length > MAX_FILE_SIZE:
        return False
    return True

def validateFoto2(files):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if files is None:
        return True

    # check if the browser submitted an empty file
    if files.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(files)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    
    if files.content_length > MAX_FILE_SIZE:
        return False
    return True
