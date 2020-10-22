function validacion(){
    producto = document.getElementById("cboproducto").value;
    cantidad = document.getElementById("cant").value;


    if (producto == null || producto == 0) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Seleccione un producto de la lista!',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }

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





}


