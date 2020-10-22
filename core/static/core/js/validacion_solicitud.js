function validacion() {
    direccion = document.getElementById("direccion").value;
    min = document.getElementById("min").value;
    max = document.getElementById("max").value;

    if (direccion == null || direccion.length == 0 || /^\s+$/.test(direccion)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrese una dirección válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }

    if (!isNaN(min)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrese una fecha mínima que desea recibir su solicitud.',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }

    if (!isNaN(max)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrese fecha máxima que desee recibir su solicitud.',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }

}