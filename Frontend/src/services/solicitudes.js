/* eslint-disable prettier/prettier */
async function obtenerSolicitudes() {
  return new Promise((resolve, reject) => {
      fetch('http://localhost:8000/hospital/api/v1solicitud_transplantes/')
          .then(res => {
              if (!res.ok) {
                  throw new Error('Error al obtener los registros');
              }
              return res.json();
          })
          .then(solicitudes => {
              resolve(solicitudes);
          })
          .catch(error => {
              console.error('Error al obtener los registros: ' + error);
              reject(error);
          });
  });
}

async function insertarSolicitud(solicitud) {
  return new Promise((resolve, reject) => {
    fetch('http://localhost:8000/hospital/api/v1solicitud_transplantes/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(solicitud),
    })
      .then(res => {
        if (!res.ok) {
          throw new Error('Error al insertar los datos de la solicitud al servidor: ' + res);
        }

        resolve(res.json());
      })
      .catch(error => {
        console.error('Error al enviar los datos de la solicitud al servidor: ' + error);
        reject(error);
      });
  });
}

export { obtenerSolicitudes, insertarSolicitud }