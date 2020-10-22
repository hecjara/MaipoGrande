function confirmarModificarProducto() {
    Swal.fire({
        title: '¿Desea modificar el producto??',
        text: "Actualizara los datos de su producto",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, actualizar!'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire(
                'Producto actualizado!',
                'El producto de la solicitud ha sido actualizado',
                'success'
            )
        }
    })
}


