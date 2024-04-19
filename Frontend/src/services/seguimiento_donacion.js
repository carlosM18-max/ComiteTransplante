/* eslint-disable prettier/prettier */
function obtenerSegDonaciones() {
    return new Promise((resolve, reject) => {
        fetch('http://localhost:8000/obtener_seguimiento_donacion/')
            .then(res => {
                if (!res.ok) {
                    throw new Error('Error al obtener los seguimientos');
                }
                return res.json();
            })
            .then(segDonacion => {
                resolve(segDonacion);
            })
            .catch(error => {
                console.error('Error al obtener los seguimientos: ' + error);
                reject(error);
            });
    });
}

function insertarSegDonacion(segDonacion) {
    return new Promise((resolve, reject) => {
      fetch('http://localhost:8000/insertar_seguimiento_donacion/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(segDonacion),
      })
        .then(res => {
          if (!res.ok) {
            throw new Error('Error al insertar los datos del seguimiento de la donación al servidor: ' + res);
          }
  
          resolve(res.json());
        })
        .catch(error => {
          console.error('Error al enviar los datos del seguimiento de la donación al servidor: ' + error);
          reject(error);
        });
    });
  }

export { obtenerSegDonaciones, insertarSegDonacion }