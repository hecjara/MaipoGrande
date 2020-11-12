function validacion() {
    cantidad = document.getElementById("cantidadtxt").value;
    precio = document.getElementById("preciotxt").value;

    if (cantidad == null || cantidad.length == 0 || /^\s+$/.test(cantidad)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece una cantidad válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }
    else if (isNaN(cantidad)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece una cantidad válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }
    else if (cantidad <= 0) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece una cantidad válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }

    if (precio == null || precio.length == 0 || /^\s+$/.test(precio)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece un precio válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }
    else if (isNaN(precio)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece un precio válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }
    else if (precio <= 0) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece un precio válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }

}