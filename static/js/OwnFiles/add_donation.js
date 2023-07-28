let regionSelector = document.getElementById("region");
let comunaSelector = document.getElementById("comuna");
let comunaIdInput = document.getElementById("comuna_id");
fetch("/static/json/region_comuna.json")
  .then(response => response.json())
  .then(data => {
    data.regiones.forEach(region => {
      let option = document.createElement("option");
      option.value = region.id;
      option.text = region.nombre;
      regionSelector.appendChild(option);
    });
    regionSelector.addEventListener("change", () => {
      comunaSelector.innerHTML = '<option value="">Seleccione una comuna</option>';
      comunaIdInput.value = ''; // clean values of hidden input
      let regionId = regionSelector.value;
      let region = data.regiones.find(region => region.id == regionId);
      let comunas = region ? region.comunas : [];
      comunas.forEach(comuna => {
        let option = document.createElement("option");
        option.value = comuna.id;
        option.text = comuna.nombre;
        comunaSelector.appendChild(option);
      });
    });
    comunaSelector.addEventListener("change", () => {
      comunaIdInput.value = comunaSelector.value;
    });
});

// FORM VALIDATIONS

const validateRegiones = (regiones) => {
    if (!regiones) return false;
    return true;
};
const validateComunas = (comunas) => {
    if (!comunas) return false;
    return true;
};
const validateCalle_numero = (calle_numero) => {
    if (!calle_numero) return false;
    let lengthValid = calle_numero.length <= 80;
    return lengthValid;
};
const validateTipo_donacion = (tipo_donacion) => {
    if (!tipo_donacion) return false;
    return true;
};
const validateCantidad = (cantidad) => {
    if (!cantidad) return false;
    let lengthValid = cantidad.length <= 10;
    return lengthValid;
};
const validateFecha_disponibilidad = (fecha_disponibilidad) => {
    if (!fecha_disponibilidad) return false;
    let fechaHoy = new Date();
    let fechaIntroducida = new Date(fecha_disponibilidad);
    let esValida = fechaIntroducida >= fechaHoy;

    let re = /202[3-9]-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/;
    let formatValid = re.test(fecha_disponibilidad);
    return formatValid && esValida;
};
const validateDescripcion = (descripcion) => {
    if(!descripcion) return true;
    let lengthValid = descripcion.length <=80;
    return lengthValid;
};
const validateCondiciones = (condiciones) => {
    if(!condiciones) return true;
    let lengthValid = condiciones.length <=80;
    return lengthValid;
};
const validateFoto_donacion = (foto_donacion) => {
    if (!foto_donacion) return false;
    return true;
};
const validateNombre_donante = (nombre_donante) => {
    if (!nombre_donante) return false;
    let lengthValid = 3 <= nombre_donante.length && nombre_donante.length <= 80;
    return lengthValid;
};
const validateEmail = (email) => {
    if (!email) return false;
    // Validation of format
    let re = /^[\w\.]+@([\w]+\.)+[\w]{2,3}$/;
    let formatValid = re.test(email);
    let lengthValid = email.length <=80;
    return formatValid && lengthValid;
};
const validateCelular = (celular) => {
    if (!celular) return true;
    // Validation of format
    let re = /[+]569 [0-9]{8}$/;
    let formatValid = re.test(celular);
    let lengthValid = celular.length <=15;
    return formatValid && lengthValid;
};
const validateFoto1 = (files) => {
    if (files.length === 0) return false;
    // Number of files (1)
    let lengthValid = 1 == files.length;
    // Type validation
    let typeValid = true;
    for (const file of files) {
        // file.type should be "image/<foo>" or "application/pdf"
        let fileFamily = file.type.split("/")[0];
        typeValid &&= fileFamily == "image";
    }
    return lengthValid && typeValid;
};
const validateFoto2 = (files) => {
    if (files.length === 0) return true;
    // Number of files (1)
    let lengthValid = 1 == files.length;
    // Type validation
    let typeValid = true;
    for (const file of files) {
        // file.type should be "image/<foo>" or "application/pdf"
        let fileFamily = file.type.split("/")[0];
        typeValid &&= fileFamily == "image";
    }
    return lengthValid && typeValid;
};
  
const validateForm = () => {
    // DOM elements are obtained from the form
    let myForm = document.forms["form_donacion"];
    let region = myForm["region"].value;
    let comuna = myForm["comuna"].value;
    let calle_numero = myForm["calle-numero"].value;
    let tipo = myForm["tipo"].value;
    let cantidad = myForm["cantidad"].value;
    let fecha_disponibilidad = myForm["fecha-disponibilidad"].value;
    let descripcion = myForm["descripcion"].value;
    let condiciones = myForm["condiciones"].value;
    let foto1 = myForm["foto_1"].files;
    let foto2 = myForm["foto_2"].files;
    let foto3 = myForm["foto_3"].files;
    let nombre = myForm["nombre"].value;
    let email = myForm["email"].value;
    let phoneNumber = myForm["celular"].value;

    // Aux functions on validation
    let invalidInputs = [];
    let isValid = true;
    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid &&= false;
    };

    // Validation logic
    if (!validateRegiones(region)) {
        setInvalidInput("Seleccione alguna región.");
    }
    if (!validateComunas(comuna)) {
        setInvalidInput("Seleccione alguna comuna.");
    }
    if (!validateCalle_numero(calle_numero)) {
        setInvalidInput("Ingrese una dirección válida.");
    }
    if (!validateTipo_donacion(tipo)) {
        setInvalidInput("Ingrese algún tipo entre las opciones.");
    }
    if (!validateCantidad(cantidad)) {
        setInvalidInput("Ingrese una cantidad válida.");
    }
    if (!validateFecha_disponibilidad(fecha_disponibilidad)) {
        setInvalidInput("Ingrese alguna fecha actual o futura.");
    }
    if (!validateDescripcion(descripcion)) {
        setInvalidInput("Ingrese una descripción con menos de 80 caracteres.");
    }
    if (!validateCondiciones(condiciones)) {
        setInvalidInput("Ingrese sus condiciones en menos de 80 caracteres.");
    }
    if (!validateNombre_donante(nombre)) {
        setInvalidInput("El nombre ingresado no es válido.");
    }
    if (!validateEmail(email)) {
        setInvalidInput("El email ingresado no es válido.");
    }
    if (!validateCelular(phoneNumber)) {
        setInvalidInput("El número de celular ingresado no es válido.");
    }
    if (!validateFoto1(foto1)) {
        setInvalidInput("Ingrese una imagen válida en foto 1.");
    }
    if (!validateFoto2(foto2)) {
        setInvalidInput("Ingrese una imagen válida en foto 2.");
    }
    if (!validateFoto2(foto3)) {
        setInvalidInput("Ingrese una imagen válida en foto 3.");
    }

    let validationBox = document.getElementById("val-box");
    let validationMessageElem = document.getElementById("val-msg");
    let validationListElem = document.getElementById("val-list");
    if (!isValid) {
        validationListElem.textContent = "";
        // Errors are added
        for (input of invalidInputs) {
            let listElement = document.createElement("li");
            listElement.innerText = input;
            listElement.style.fontSize = "14px";
            validationListElem.append(listElement);
        }
        validationMessageElem.innerText = "Error:";
        // Box of errors is shown
        validationBox.hidden = false;
    } else {
        Swal.fire({
            title: '¿Confirma?',
            text: '¿Está seguro de realizar esta donación?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, estoy seguro',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            Swal.fire({
                title: 'Éxito',
                text: 'Su donación se ha realizado.',
                icon: 'success',
                showCloseButton: true,
                confirmButtonColor: '#3085d6',
                confirmButtonText: '<a href="/" style="color: white;">Volver al inicio</a>'
            })
            // Data of the form is obtained
            const formData = new FormData(myForm);

            // POST request is done using Fetch API (AJAX)
            fetch(myForm.action, {
                method: 'POST',
                body: formData
            })
        });
    }
};

let submitBtn = document.getElementById("form-submit");
submitBtn.addEventListener("click", function(event) {
    validateForm();
});