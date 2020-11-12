function validacion() {

    nombres = document.getElementById("txtnombres").value;
    apellidos = document.getElementById("txtapellidos").value;
    telefono = document.getElementById("txttelefono").value;
    email = document.getElementById("txtemail").value;
    direccion = document.getElementById("txtdireccion").value;
    pais = document.getElementById("cbopais").value;
    fecha_nacimiento = document.getElementById("txtfecha").value;


    if (nombres == null || nombres.length == 0 || /^\s+$/.test(nombres)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrese un nombre válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }

    if (apellidos == null || apellidos.length == 0 || /^\s+$/.test(apellidos)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrese un apellido válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }

    if (telefono == null || telefono.length == 0 || /^\s+$/.test(telefono)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece un telefono válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }
    else if (isNaN(telefono)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece un telefono válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }
    else if (telefono <= 0) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrece un telefono válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }

    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/.test(email)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrese un email válido!',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }

    if (direccion == null || direccion.length == 0 || /^\s+$/.test(direccion)) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrese una direccion válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }

    if (pais == null || pais == 0) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Seleccione un país',
            // footer: '<a href>Why do I have this issue?</a>'
        })
        return false;
    }


    // var today = new Date();
    // var dd = String(today.getDate()).padStart(2, '0');
    // var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    // var yyyy = today.getFullYear();
    // today = mm + '-' + dd + '-' + yyyy;

    // if (fecha_nacimiento > today){
    //     Swal.fire({
    //         icon: 'error',
    //         title: 'Oops...',
    //         text: 'Ingrese una fecha de nacimiento válida.',
    //         // footer: '<a href>Why do I have this issue?</a>'
    //     })
    //     return false;
    // }

    
    if(fecha_nacimiento == null || fecha_nacimiento.length == 0 || /^\d{2}([./-])\d{2}\1\d{4}$/.test(fecha_nacimiento)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Ingrese una fecha de nacimiento válida!',
            // footer: '<a href>Why do I have this issue?</a>'
        })

        return false;
    }

}