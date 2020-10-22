function validacion_eliminacion(id_detalle){
    Swal.fire({
        title: '¿Desea eliminar el producto de la solicitud?',
        text: "No podras deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // redirigir al usuario a la ruta de actulizar envio
            window.location.href = "/eliminar_detalleproducto/"+id_detalle+"/";
        }
    })
}