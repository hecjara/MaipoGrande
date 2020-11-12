function validacion() {
    lote = document.getElementById("cboprodbod").value;
    cantidad = document.getElementById("cantidadtxt").value;  //cantidad ofrecida
    oferta = document.getElementById("ofertatxt").value;
    cant_solicitada = document.getElementById("cant_sol").value; //cantidad solicitada
    cant_lote = document.getElementById("cant_lote").value; // cantidad de productos que hay en el lote

    if (lote == null || lote == 0) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Seleccione un lote para realizar la oferta',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }
    
    if (cantidad > cant_lote) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'No puede ofrecer más productos de los que tiene en el lote.',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }


    if (cantidad < cant_solicitada) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La cantidad ofrecida debe ser menor o igual que la cantidad solicitada.',
            // footer: '<a href>Why do I have this issue?</a>'
        })
 
        return false;
    }
    else if (cantidad == null || cantidad.length == 0 || /^\s+$/.test(cantidad)) {
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