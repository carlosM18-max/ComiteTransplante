/* eslint-disable prettier/prettier */
function obtenerPersonas() {
    return new Promise((resolve, reject) => {
        fetch('http://localhost:8000/hospital/api/v1personas/')
            .then(res => {
                if (!res.ok) {
                    throw new Error('Error al obtener las personas');
                }
                return res.json();
            })
            .then(personas => {
                resolve(personas);
            })
            .catch(error => {
                console.error('Error al obtener las personas: ' + error);
                reject(error);
            });
    });
}

export { obtenerPersonas }