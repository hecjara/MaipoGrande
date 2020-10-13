function validacion() {
    cantidad = document.getElementById("cantidadtxt").value;
    oferta = document.getElementById("ofertatxt").value;

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

    if (oferta == null || oferta.length == 0 || /^\s+$/.test(oferta)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece una oferta válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }
    else if (isNaN(oferta)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece una oferta válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }
    else if (oferta <= 0) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece una oferta válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }

    // Swal.fire({
    //     position: 'center',
    //     icon: 'success',
    //     title: 'Oferta realizada',
    //     showConfirmButton: false,
    //     timer: 2000
    // })
    // return true;

}