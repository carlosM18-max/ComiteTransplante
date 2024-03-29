/* eslint-disable prettier/prettier */
export default {
    methods: {
      onSubmit() {
        console.log('Enviando solicitud al backend:', this.user);
        fetch('http://localhost:8000/hospital/api/v1/solicitud_transplantes/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.user),
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Error al enviar los datos al backend');
          }
          console.log('Solicitud enviada con éxito al backend.');
          // Redirige a la página de la tabla después de que la solicitud se haya completado con éxito
          this.$router.push('/table/tables-basic');
        })
        .catch(error => {
          console.error('Error al enviar los datos al backend:', error);
          // Maneja el error aquí
        });
      }
    }
  }
  