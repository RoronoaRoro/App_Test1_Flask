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
const validateTipo_pedido = (tipo_pedido) => {
    if (!tipo_pedido) return false;
    return true;
};
const validateCantidad = (cantidad) => {
    if (!cantidad) return false;
    let lengthValid = cantidad.length <= 10;
    return lengthValid;
};
const validateDescripcion = (descripcion) => {
    if (!descripcion) return false;
    let lengthValid = descripcion.length <= 80;
    return lengthValid;
};
const validateNombre_solicitante = (nombre_solicitante) => {
    if (!nombre_solicitante) return false;
    let lengthValid = 3 <= nombre_solicitante.length && nombre_solicitante.length <= 80;
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
    let re = /[+]569 [0-9]{8}/;
    let formatValid = re.test(celular);
    let lengthValid = celular.length <=15;
    return formatValid && lengthValid;
};
  
const validateForm = () => {
    // DOM elements are obtained from the form
    let myForm = document.forms["form-pedido"];
    let region = myForm["region"].value;
    let comuna = myForm["comuna"].value;
    let tipo = myForm["tipo"].value;
    let cantidad = myForm["cantidad"].value;
    let descripcion = myForm["descripcion"].value;
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
    if (!validateTipo_pedido(tipo)) {
        setInvalidInput("Ingrese algún tipo entre las opciones.");
    }
    if (!validateDescripcion(descripcion)) {
        setInvalidInput("Ingrese una descripción con menos de 80 caracteres.");
    }
    if (!validateCantidad(cantidad)) {
        setInvalidInput("Ingrese una cantidad válida.");
    }
    if (!validateNombre_solicitante(nombre)) {
        setInvalidInput("El nombre ingresado no es válido.");
    }
    if (!validateEmail(email)) {
        setInvalidInput("El email ingresado no es válido.");
    }
    if (!validateCelular(phoneNumber)) {
        setInvalidInput("El número de celular ingresado no es válido.");
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
            text: '¿Está seguro de realizar este pedido?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, estoy seguro',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    title: 'Éxito',
                    text: 'Su pedido se ha realizado.',
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
            }
        });
    }
};

let submitBtn = document.getElementById("form-submit");
submitBtn.addEventListener("click", function(event) {
    validateForm();
});