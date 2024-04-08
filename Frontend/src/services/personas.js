function obtenerPersonas() {
    let arregloPersonas = [];
    try {
        fetch('http://localhost:8000/hospital/api/v1personas/').then(res => {
            res.json().then(personas => {
                personas = Object.values(personas)
                personas.forEach(persona => {
                    arregloPersonas.push({value: persona.ID, text: persona.curp});
                })
            })
        })

        return arregloPersonas;
    } catch (error) {
        console.error('Error al obtener las personas: ' + error);
        throw error;
    }
}

export { obtenerPersonas }