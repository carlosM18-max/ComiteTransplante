/* eslint-disable prettier/prettier */
async function obtenerOrganos() {
    return new Promise((resolve, reject) => {
        fetch('http://localhost:8000/hospital/api/v1organos/')
            .then(res => {
                if (!res.ok) {
                    throw new Error('Error al obtener los órganos');
                }
                return res.json();
            })
            .then(organos => {
                resolve(organos);
            })
            .catch(error => {
                console.error('Error al obtener los órganos: ' + error);
                reject(error);
            });
    });
}

export { obtenerOrganos }