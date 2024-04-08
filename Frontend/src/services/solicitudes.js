/* eslint-disable prettier/prettier */
function insertarSolicitud(solicitud) {
  fetch('http://localhost:8000/hospital/api/v1solicitud_transplantes/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(solicitud),
  })
    .then(response => {
      // Manejar la respuesta del backend
      console.log(response.data);
      // Muestra el mensaje de éxito o realiza otras acciones necesarias
      this.showSuccessMessage();
    })
    .catch(error => {
      // Manejar errores de la solicitud
      console.error('Error al enviar los datos:', error);
      // Mostrar mensaje de error al usuario si es necesario
      this.showErrorMessage();
    });
}

export { insertarSolicitud }