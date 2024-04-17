/* eslint-disable prettier/prettier */
export default {
  methods: {
    onSubmit() {
      fetch('http://localhost:8000/hospital/api/v1solicitud_transplantes/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.user),
      })
      .then(response => {
        if (response.ok) {
          // Si la respuesta es exitosa, redirige a la página deseada
          this.$router.replace('/table/tables-basic');
        } else {
          // Manejar errores si la respuesta no es exitosa
          console.error('Error al enviar la solicitud al backend');
        }
      })
      .catch(error => {
        console.error('Error al enviar la solicitud:', error);
      });
    }    
  }
}
