/* eslint-disable prettier/prettier */
function insertarSolicitud(solicitud) {
  return new Promise((resolve, reject) => {
    fetch('http://localhost:8000/hospital/api/v1solicitud_transplantes/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(solicitud),
    })
      .then(res => {
        console.log(res.status); // Imprime el código de estado de la respuesta
        console.log(res.statusText); // Imprime el mensaje de estado de la respuesta
        console.log(res.text()); // Convierte el cuerpo de la respuesta a texto
        if (!res.ok) {
          throw new Error('Error al insertar los datos de la solicitud al servidor: ' + res);
        }
        return res.json();
      })
      .then(datos => {
        resolve(datos);
      })
      .catch(error => {
        console.error('Error al enviar los datos de la solicitud al servidor: ' + error);
        reject(error);
      });
  });
}

export { insertarSolicitud }