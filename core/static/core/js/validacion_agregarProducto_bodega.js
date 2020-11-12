function validacion() {
    producto = document.getElementById("cboproducto").value;
    cantidad = document.getElementById("cantidadtxt").value;
    precio = document.getElementById("preciotxt").value;
    fecelab = document.getElementById("fecelab").value;
    fecven = document.getElementById("fecven").value;


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

    if(fecelab == null || fecelab.length == 0 || /^\d{2}([./-])\d{2}\1\d{4}$/.test(fecelab)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece una fecha de elaboración válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }

    if(fecven == null || fecven.length == 0 || /^\d{2}([./-])\d{2}\1\d{4}$/.test(fecven)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece una fecha de vencimiento válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }

    if(fecelab > fecven){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La fecha de elaboración no puede ser mayor que la fecha de vencimiento!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }
    else if(fecelab == fecven){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La fecha de elaboración igual a la fecha de vencimiento!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }


}


