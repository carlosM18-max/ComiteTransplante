function obtenerOrganos() {
    let arregloOrganos = [];
    try {
        fetch('http://localhost:8000/hospital/api/v1organos/').then(res => {
            res.json().then(organos => {
                organos = Object.values(organos)
                organos.forEach(organo => {
                    arregloOrganos.push({value: organo.ID, text: organo.nombre});
                })
            })
        })

        return arregloOrganos;
    } catch (error) {
        console.error('Error al obtener los órganos: ' + error);
        throw error;
    }
}

export { obtenerOrganos }