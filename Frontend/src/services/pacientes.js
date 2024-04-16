/* eslint-disable prettier/prettier */
function obtenerPacientes() {
    return new Promise((resolve, reject) => {
        fetch('http://localhost:8000/hospital/api/v1pacientes/')
            .then(res => {
                if (!res.ok) {
                    throw new Error('Error al obtener los pacientes');
                }
                return res.json();
            })
            .then(pacientes => {
                resolve(pacientes);
            })
            .catch(error => {
                console.error('Error al obtener los pacientes: ' + error);
                reject(error);
            });
    });
}

export { obtenerPacientes }