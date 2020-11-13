function validacion_eliminacion(id_prod_bod){
    Swal.fire({
        title: '¿Desea eliminar el producto de la bodega?',
        text: "No podras deshacer esta acción!",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // redirigir al usuario a la ruta de actulizar envio
            window.location.href = "/eliminar_producto_bodega/"+id_prod_bod+"/";
        }
    })
}