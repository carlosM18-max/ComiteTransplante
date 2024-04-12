<!-- eslint-disable prettier/prettier -->
<template>
  <b-row>
    <b-col sm="12">
      <iq-card no-body>
        <template v-slot:headerTitle>
          <b-card-title>{{ $t('Validate Wizard') }}</b-card-title>
        </template>

        <template v-slot:body>
          <div class="stepwizard mt-4">
            <ul class="stepwizard-row setup-panel">
              <div id="donatario" class="wizard-step active"
                :class="`${currentindex == 1 ? 'active' : ''} ${currentindex > 1 ? 'done active' : ''}`">
                <a href="" class="active btn"> <i class="ri-user-fill text-primary"></i><span>Detalles del
                    donatario</span> </a>
              </div>
              <div id="especificaciones" class="wizard-step"
                :class="`${currentindex == 2 ? 'active' : ''} ${currentindex > 2 ? 'done active' : ''}`">
                <a href="" class="btn btn-default disabled active"> <i class="ri-article-fill text-danger"></i><span>Especificaciones de la donación</span> </a>
              </div>
              <div id="resumen" class="wizard-step"
                :class="`${currentindex == 3 ? 'active' : ''} ${currentindex > 3 ? 'done active' : ''}`">
                <a href="" class="btn btn-default disabled active"> <i
                    class="ri-user-fill text-success"></i><span>Resumen</span> </a>
              </div>
              <div id="confirmacion" class="wizard-step"
                :class="`${currentindex == 4 ? 'active' : ''} ${currentindex > 4 ? 'done active' : ''}`">
                <a href="" class="btn btn-default disabled active"> <i
                    class="ri-check-fill text-warning"></i><span>Confirmación</span> </a>
              </div>
            </ul>
          </div>
          <Form @submit="onSubmit" :validation-schema="schema" class="text-center mt-3">
            <!-- <b-form id="form-wizard1" class="text-center mt-3"> -->
            <!-- Parte 1 informacion del donatario -->
            <div :class="`${currentindex == 1 ? 'show' : 'd-none'}`">
              <fieldset>
                <div class="form-card text-start">
                  <b-row>
                    <div class="col-7">
                      <h3 class="mb-4">Informacion del donatario:</h3>
                    </div>
                  </b-row>
                  <b-row>
                    <b-col md="6">
                      <b-form-group label-for="donatario_select" label="CURP: *">
                        <b-form-select plain v-model="solicitud.donatario" :options="llenarDonatarioSelect()"
                          id="donatario_select" :class="{ 'is-invalid': !solicitud.donatario }">
                          <template v-slot:first>
                            <b-form-select-option :value="null" disabled>Selecciona una CURP</b-form-select-option>
                          </template>
                        </b-form-select>
                        <div class="invalid-feedback">¡La CURP del donatario es obligatoria!</div>
                      </b-form-group>
                    </b-col>
                  </b-row>
                </div>
                <a href="#especificaciones" class="btn btn-primary next action-button float-end" @click="changeTab(2)"
                  value="Next">Siguiente</a>
              </fieldset>
            </div>
            <!-- Segunda parte iformacion de la donacion-->
            <div :class="`${currentindex == 2 ? 'show' : 'd-none'}`">
              <fieldset>
                <div class="form-card text-start">
                  <b-row>
                    <div class="col-7">
                      <h3 class="mb-4">Detalles de la donación:</h3>
                    </div>
                  </b-row>
                  <b-row>
                    <b-col md="6">
                      <b-form-group label-for="donador_select" label="CURP del donador: *">
                        <b-form-select plain v-model="solicitud.donador" :options="llenarDonadorSelect()"
                          id="donador_select" :class="{ 'is-invalid': !solicitud.donador }">
                          <template v-slot:first>
                            <b-form-select-option :value="null" disabled>Selecciona una CURP</b-form-select-option>
                          </template>
                        </b-form-select>
                        <div class="invalid-feedback">¡La CURP del donador es obligatoria!</div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label-for="medico_select" label="CURP del médico: *">
                        <b-form-select plain v-model="solicitud.medico" :options="llenarMedicoSelect()"
                          id="medico_select" :class="{ 'is-invalid': !solicitud.medico }">
                          <template v-slot:first>
                            <b-form-select-option :value="null" disabled>Selecciona una CURP</b-form-select-option>
                          </template>
                        </b-form-select>
                        <div class="invalid-feedback">¡La CURP del médico es obligatoria!</div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Tipo de Órgano: *">
                        <b-form-select v-model="solicitud.organo" :options="llenarOrganosSelect()"
                          :class="{ 'is-invalid': !solicitud.organo }" />
                        <div class="invalid-feedback">¡El órgano es obligatorio!</div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Prioridad: *">
                        <b-form-select v-model="solicitud.prioridad" :options="opcionesPrioridad"
                          :class="{ 'is-invalid': !solicitud.prioridad }" />
                        <div class="invalid-feedback">¡La prioridad es obligatoria!</div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Fecha de solicitud: *">
                        <Field v-model="solicitud.fecha_solicitud" type="date" class="form-control"
                          name="fecha_solicitud" :class="{ 'is-invalid': !solicitud.fecha_solicitud }" />
                        <div class="invalid-feedback">¡La fecha de solicitud es obligatoria!</div>
                      </b-form-group>
                    </b-col>
                  </b-row>
                </div>
                <a href="#resumen" @click="changeTab(3)" class="btn btn-primary next action-button float-end"
                  value="Next">Siguiente</a>
                <a href="#donatario" @click="changeTab(1)"
                  class="btn btn-dark previous action-button-previous float-end me-1" value="Previous">Anterior</a>
              </fieldset>
            </div>

            <!-- Parte 3 informacion del medico -->
            <div id="resumen" :class="`${currentindex == 3 ? 'show' : 'd-none'}`">
              <fieldset>
                <div class="form-card text-start">
                  <b-row>
                    <div class="col-7">
                      <h3 class="mb-4">Resumen de la solicitud:</h3>
                    </div>
                  </b-row>
                  <b-row>
                    <b-col md="6">
                      <b-form-group label-for="nombre_donatario" label="Nombre completo del donatario:">
                        <b-form-input type="text" id="nombre_donatario" v-model="resumen.nombre_donatario"
                          disabled></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label-for="nombre_donador" label="Nombre completo del donador:">
                        <b-form-input type="text" id="nombre_donador" v-model="resumen.nombre_donador"
                          disabled></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label-for="nombre_medico" label="Nombre completo del médico:">
                        <b-form-input type="text" id="nombre_medico" v-model="resumen.nombre_medico"
                          disabled></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label-for="organo" label="Órgano a donar:">
                        <b-form-input type="text" id="organo" v-model="resumen.organo"
                          disabled></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label-for="prioridad" label="Prioridad:">
                        <b-form-input type="text" id="prioridad" v-model="solicitud.prioridad"
                          disabled></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label-for="fecha_solicitud" label="Fecha de la solicitud:">
                        <b-form-input type="text" id="fecha_solicitud" v-model="solicitud.fecha_solicitud"
                          disabled></b-form-input>
                      </b-form-group>
                    </b-col>
                  </b-row>
                </div>
                <a href="#payment" @click="changeTab(4)" class="btn btn-primary next action-button float-end"
                  value="Next">Siguiente</a>
                <a href="#account" @click="changeTab(2)"
                  class="btn btn-dark previous action-button-previous float-end me-1" value="Previous">Anterior</a>
              </fieldset>
            </div>
            <div id="confirm" :class="`${currentindex == 4 ? 'show' : 'd-none'}`">
              <fieldset>
                <div class="form-card">
                  <b-row>
                    <div class="col-7">
                      <h3 class="mb-4 text-start">Terminar de agendar la solicitud:</h3>
                    </div>
                  </b-row>
                  <br /><br />
                  <h2 class="text-success text-center">
                    <strong>¡Solicitud realizada!</strong>
                  </h2>
                  <br />
                  <b-row class="justify-content-center">
                    <div class="col-3">
                      <img src="../../assets/images/page-img/img-success.png" class="img-fluid" alt="fit-image" />
                    </div>
                  </b-row>
                  <br /><br />
                  <b-row class="justify-content-center">
                    <div class="col-7 text-center">
                      <h5 class="purple-text text-center">Espera para realizar la donación, gracias por ayudar a los
                        demás</h5>
                    </div>
                  </b-row>
                </div>
              </fieldset>
            </div>
            <!-- </b-form> -->
          </Form>
        </template>
      </iq-card>
    </b-col>
  </b-row>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import iqCard from '../../components/xray/cards/iq-card'
import { Form, Field } from 'vee-validate'
import * as yup from 'yup'
import { obtenerOrganos } from '@/services/organos';
import { obtenerPersonas } from '@/services/personas'
import { obtenerPersonalMedico } from '@/services/personal_medico'
import { insertarSolicitud } from '@/services/solicitudes'

let obtenerOrganosInstancia = []
let obtenerPersonasInstancia = []
let obtenerPersonalMedicoInstancia = []

obtenerOrganos().then(organos => {
  obtenerOrganosInstancia = organos
}).catch(error => {
  console.error(`Error: ${error}`)
})

obtenerPersonas().then(personas => {
  obtenerPersonasInstancia = personas
}).catch(error => {
  console.error(`Error: ${error}`)
})

obtenerPersonalMedico().then(medicos => {
  obtenerPersonalMedicoInstancia = medicos
}).catch(error => {
  console.error(`Error: ${error}`)
})

export default {
  name: 'ValidateWizard',
  components: {
    iqCard,
    Form,
    Field
  },
  data() {
    // Define el esquema de validación
    const schema = yup.object().shape({
      donatario: yup.string().required(),
      donador: yup.string().required(),
      medico: yup.string().required(),
      organo: yup.string().required(),
      prioridad: yup.string().required(),
      fecha_solicitud: yup.date().required(),
    });

    return {
      solicitud: {
        donatario: '',
        donador: '',
        medico: '',
        organo: '',
        prioridad: '',
        fecha_solicitud: '',
      },
      obtenerPersonasInstancia,
      obtenerPersonalMedicoInstancia,
      currentindex: 1,
      schema,
      mostrarAlerta: false,
      obtenerOrganosInstancia,
      opcionesPrioridad: ['Urgente', 'Alta', 'Moderada'],
      resumen: {
        nombre_donatario: '',
        nombre_donador: '',
        nombre_medico: '',
        organo: ''
      }
    }
  },
  methods: {
    llenarOrganosSelect() {
      let organos = []
      obtenerOrganosInstancia.forEach(organo => {
        organos.push({ value: organo.ID, text: organo.nombre })
      })

      return organos
    },
    llenarDonatarioSelect() {
      let personas = []
      obtenerPersonasInstancia.forEach(persona => {
        personas.push({ value: persona.ID, text: persona.curp })
      })

      return personas
    },
    llenarDonadorSelect() {
      let personas = []
      obtenerPersonasInstancia.forEach(persona => {
        if (persona.ID != this.solicitud.donatario && persona.ID != this.solicitud.medico)
          personas.push({ value: persona.ID, text: persona.curp })          
      })

      return personas
    },
    llenarMedicoSelect() {
      let medicos = []

      obtenerPersonasInstancia.forEach(persona => {
        if (obtenerPersonalMedicoInstancia.some(medico => medico.persona_ID === persona.ID)) {
          if (persona.ID != this.solicitud.donatario && persona.ID != this.solicitud.donador)
            medicos.push({ value: persona.ID, text: persona.curp })
        }
      })
      return medicos
    },
    generarResumen() {
      let donatario_encontrado = obtenerPersonasInstancia.find(persona => persona.ID == this.solicitud.donatario)
      let donador_encontrado = obtenerPersonasInstancia.find(persona => persona.ID == this.solicitud.donador)
      let medico_encontrado = obtenerPersonasInstancia.find(persona => persona.ID == this.solicitud.medico)
      let organo_encontrado = obtenerOrganosInstancia.find(organo => organo.ID == this.solicitud.organo)

      this.resumen.nombre_donatario = donatario_encontrado.nombre + ' ' + donatario_encontrado.primer_apellido + ' ' + donatario_encontrado.segundo_apellido

      this.resumen.nombre_donador = donador_encontrado.nombre + ' ' + donador_encontrado.primer_apellido + ' ' + donador_encontrado.segundo_apellido

      this.resumen.nombre_medico = medico_encontrado.nombre + ' ' + medico_encontrado.primer_apellido + ' ' + medico_encontrado.segundo_apellido

      this.resumen.organo = organo_encontrado.nombre
    },
    changeTab(val) {
      this.currentindex = val;
      if (val === 2) {
        if (this.solicitud.donatario == '') {
          this.currentindex = 1
          return
        }
      }
      if (val === 3) {
        if (this.solicitud.donador == '' || this.solicitud.medico == '' || this.solicitud.organo == '' || this.solicitud.prioridad == '' || this.solicitud.fecha_solicitud == '') {
          this.currentindex = 2
          return
        }
        this.generarResumen()
      }
      // Verifica si el último paso del wizard se ha completado
      if (val === 4) {
        // Realiza el envío de los datos al backend
        this.onSubmit();
      }
    },
    onSubmit() {
      insertarSolicitud(this.solicitud)
    },
    showSuccessMessage() {
      // Muestra un mensaje de éxito al usuario
      console.log('¡Solicitud realizada con éxito!');
      // Puedes redirigir a otra página si es necesario
      this.$router.push('/table/tables-basic');
    },
    showErrorMessage() {
      // Muestra un mensaje de error al usuario
      console.log('Ocurrió un error al enviar la solicitud. Por favor, inténtalo de nuevo más tarde.');
    }
  }
}
</script>
