function obtenerPacientes() {
    let arregloPacientes = [];
    try {
        fetch('http://localhost:8000/hospital/api/v1pacientes/').then(res => {
            res.json().then(pacientes => {
                pacientes = Object.values(pacientes)
                pacientes.forEach(paciente => {
                    arregloPacientes.push(paciente.persona_ID);
                })
            })
        })

        return arregloPacientes;
    } catch (error) {
        console.error('Error al obtener los pacientes: ' + error);
        throw error;
    }
}

export { obtenerPacientes }