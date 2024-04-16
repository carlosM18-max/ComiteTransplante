/* eslint-disable prettier/prettier */
function obtenerPersonalMedico() {
    return new Promise((resolve, reject) => {
        fetch('http://localhost:8000/hospital/api/v1personal_medico/')
            .then(res => {
                if (!res.ok) {
                    throw new Error('Error al obtener los médicos');
                }
                return res.json();
            })
            .then(medicos => {
                resolve(medicos);
            })
            .catch(error => {
                console.error('Error al obtener los médicos: ' + error);
                reject(error);
            });
    });
}

export { obtenerPersonalMedico }