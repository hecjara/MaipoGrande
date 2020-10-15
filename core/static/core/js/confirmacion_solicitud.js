function confirmarActualizarSolicitud(id_solicitud) {
    Swal.fire({
        title: '¿Recibiste lo solicitado?',
        text: "No podras deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, recibí mi pedido!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // redirigir al usuario a la ruta de actulizar envio
            window.location.href = "/actualizar_pedidorecibido/"+id_solicitud+"/";
        }
    })
}

function confirmarAnularSolicitud(id_solicitud) {
    Swal.fire({
        title: '¿Deseas anular la solicitud?',
        text: "No podras deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, anula!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // redirigir al usuario a la ruta de actulizar envio
            window.location.href = "/actualizar_pedidoanulado/"+id_solicitud+"/";
        }
    })
}