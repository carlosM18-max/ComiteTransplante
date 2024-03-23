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
              <div id="user" class="wizard-step active"
                :class="`${currentindex == 1 ? 'active' : ''} ${currentindex > 1 ? 'done active' : ''}`">
                <a href="#user-detail" class="active btn"> <i
                    class="ri-user-fill text-primary"></i><span>Detalles del donatario</span> </a>
              </div>
              <div id="document" class="wizard-step"
                :class="`${currentindex == 2 ? 'active' : ''} ${currentindex > 2 ? 'done active' : ''}`">
                <a href="#user-detail" class="btn btn-default disabled active"> <i
                    class="ri-user-fill text-danger"></i><span>Especificaciones de la donacion</span> </a>
              </div>
              <div id="bank" class="wizard-step"
                :class="`${currentindex == 3 ? 'active' : ''} ${currentindex > 3 ? 'done active' : ''}`">
                <a href="#user-detail" class="btn btn-default disabled active"> <i
                    class="ri-user-fill text-success"></i><span>Datos del medico</span> </a>
              </div>
              <div id="confirm" class="wizard-step"
                :class="`${currentindex == 4 ? 'active' : ''} ${currentindex > 4 ? 'done active' : ''}`">
                <a href="#cpnfirm-data" class="btn btn-default disabled active"> <i
                    class="ri-check-fill text-warning"></i><span>Confirmacion</span> </a>
              </div>
            </ul>
          </div>
          <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors }" class="text-center mt-3">
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
                      <b-form-group label="Nombre: *">
                        <Field v-model="user.fname" type="text" class="form-control" name="FirstName"
                          placeholder="Enter First Name" :rules="isRequire"
                          :class="{ 'is-invalid': errors.FirstName }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.FirstName }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Primer apellido: *">
                        <Field v-model="user.lname" type="text" class="form-control" name="LastName"
                          placeholder="Enter Last Name" :rules="isRequire" :class="{ 'is-invalid': errors.LastName }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.LastName }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Segundo apellido: *">
                        <Field v-model="user.sname" type="text" class="form-control" name="SecondLastName"
                          placeholder="Enter Second Last Name" :rules="isRequire"
                          :class="{ 'is-invalid': errors.SecondLastName }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.SecondLastName }}</span>
                        </div>
                      </b-form-group>
                    </b-col>

                    <b-col md="6">
                      <b-form-group label="Curp: *">
                        <Field class="form-control" v-model="user.curp" type="text" placeholder="CURP" name="CURP"
                          :rules="isRequire" :class="{ 'is-invalid': errors.CURP }"></Field>
                        <div class="invalid-feedback">
                          <span>{{ errors.CURP }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="NSS: *">
                        <Field type="text" class="form-control" name="NSS" :rules="isRequire"
                          :class="{ 'is-invalid': errors.NSS }" placeholder="NSS" />
                        <div class="invalid-feedback">
                          <span>{{ errors.NSS }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Grupo y tipo de sangre: *">
                        <b-form-select v-model="user.bloodGroup" :options="bloodGroupOptions" :rules="isRequire"
                          :class="{ 'is-invalid': errors.bloodGroup }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.bloodGroup }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Estado: *">
                        <b-form-select v-model="user.state" :options="stateOptions" :rules="isRequire"
                          :class="{ 'is-invalid': errors.State }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.State }}</span>
                        </div>
                      </b-form-group>
                    </b-col>

                  </b-row>
                  <b-row>
                  </b-row>
                </div>
                <a href="#personal" class="btn btn-primary next action-button float-end" @click="changeTab(2)"
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
                      <b-form-group label="Nombre del Paciente o Donador: *">
                        <Field type="text" class="form-control" name="Donor_Patient_Name"
                          placeholder="Nombre del Paciente o Donador" :rules="isRequire"
                          :class="{ 'is-invalid': errors.Donor_Patient_Name }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Donor_Patient_Name }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Nombre del Médico: *">
                        <Field type="text" class="form-control" name="Doctor_Name" placeholder="Nombre del Médico"
                          :rules="isRequire" :class="{ 'is-invalid': errors.Doctor_Name }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Doctor_Name }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Tipo de Órgano: *">
                        <Field type="text" class="form-control" name="Organ_Type" placeholder="Tipo de Órgano"
                          :rules="isRequire" :class="{ 'is-invalid': errors.Organ_Type }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Organ_Type }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Prioridad: *">
                        <b-form-select v-model="user.Priority" :options="priorityOptions" :rules="isRequire"
                          :class="{ 'is-invalid': errors.Priority }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Priority }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Fecha de Donación: *">
                        <Field type="date" class="form-control" name="Donation_Date" :rules="isRequire"
                          :class="{ 'is-invalid': errors.Donation_Date }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Donation_Date }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Días de Espera: *">
                        <Field type="number" class="form-control" name="Waiting_Days" placeholder="Días de Espera"
                          :rules="isRequire" :class="{ 'is-invalid': errors.Waiting_Days }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Waiting_Days }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Estado: *">
                        <b-form-select v-model="user.Transplant_Status" :options="transplantStatusOptions"
                          :rules="isRequire" :class="{ 'is-invalid': errors.Transplant_Status }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Transplant_Status }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                  </b-row>
                </div>
                <a href="#payment" @click="changeTab(3)" class="btn btn-primary next action-button float-end"
                  value="Next">Siguiente</a>
                <a href="#account" @click="changeTab(1)"
                  class="btn btn-dark previous action-button-previous float-end me-1" value="Previous">Anterior</a>
              </fieldset>
            </div>

            <!-- Parte 3 informacion del medico -->
            <div id="payment" :class="`${currentindex == 3 ? 'show' : 'd-none'}`">
              <fieldset>
                <div class="form-card text-start">
                  <b-row>
                    <div class="col-7">
                      <h3 class="mb-4">Detalles del medico:</h3>
                    </div>
                  </b-row>
                  <b-row>
                    <b-col md="6">
                      <b-form-group label="Nombre del Médico: *">
                        <Field type="text" class="form-control" name="Doctor_Name" placeholder="Nombre del Médico"
                          :rules="isRequire" :class="{ 'is-invalid': errors.Doctor_Name }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Doctor_Name }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Especialidad del Médico: *">
                        <Field type="text" class="form-control" name="Doctor_Specialization"
                          placeholder="Especialidad del Médico" :rules="isRequire"
                          :class="{ 'is-invalid': errors.Doctor_Specialization }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Doctor_Specialization }}</span>
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col md="6">
                      <b-form-group label="Cédula Profesional del Médico: *">
                        <Field type="number" class="form-control" name="Doctor_Professional_License"
                          placeholder="Cédula Profesional del Médico" :rules="isRequire"
                          :class="{ 'is-invalid': errors.Doctor_Professional_License }" />
                        <div class="invalid-feedback">
                          <span>{{ errors.Doctor_Professional_License }}</span>
                        </div>
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
                    <strong>Solicitud realizada !</strong>
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
                      <h5 class="purple-text text-center">Espera para realizar la donacion, gracias por ayudar a los demas</h5>
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
<script>
import iqCard from '../../components/xray/cards/iq-card'
import { Form, Field } from 'vee-validate'
import * as yup from 'yup'

export default {
  name: 'ValidateWizard',
  components: {
    iqCard,
    Form,
    Field
  },
  data() {
    const schema = yup.object({
      userRole: yup.object().required(),
      FirstName: yup.string().required(),
      LastName: yup.string().required(),
      UserName: yup.string().required(),
      BloodGroup: yup.string().required(), // Agrega la validación para el campo BloodGroup
      State: yup.string().required(), // Agrega la validación para el campo State
      Donor_Patient_Name: yup.string().required(), // Agrega la validación para el campo Donor_Patient_Name
      Doctor_Name: yup.string().required(), // Agrega la validación para el campo Doctor_Name
      Organ_Type: yup.string().required(), // Agrega la validación para el campo Organ_Type
      Priority: yup.string().required(), // Agrega la validación para el campo Priority
      Donation_Date: yup.date().required(), // Agrega la validación para el campo Donation_Date
      Waiting_Days: yup.number().required(), // Agrega la validación para el campo Waiting_Days
      Transplant_Status: yup.string().required() // Agrega la validación para el campo Transplant_Status
    });

    return {
      user: {
        fname: '',
        lname: '',
        name: '',
        username: '',
        email: '',
        new_password: '',
        Address: '',
        address2: '',
        company_name: '',
        profile_image: require('../../assets/images/user/11.png'),
        mobile_no: '',
        alter_contact: '',
        country: null,
        city: '',
        pincode: '',
        role: null,
        BloodGroup: '', // Agrega el campo BloodGroup al objeto user
        State: '', // Agrega el campo State al objeto user
        Donor_Patient_Name: '', // Agrega el campo Donor_Patient_Name al objeto user
        Doctor_Name: '', // Agrega el campo Doctor_Name al objeto user
        Organ_Type: '', // Agrega el campo Organ_Type al objeto user
        Priority: '', // Agrega el campo Priority al objeto user
        Donation_Date: '', // Agrega el campo Donation_Date al objeto user
        Waiting_Days: '', // Agrega el campo Waiting_Days al objeto user
        Transplant_Status: '' // Agrega el campo Transplant_Status al objeto user
      },
      currentindex: 1,
      schema,
      users: [],
      bloodGroupOptions: [
        { value: 'A+', text: 'A+' },
        { value: 'A-', text: 'A-' },
        { value: 'B+', text: 'B+' },
        { value: 'B-', text: 'B-' },
        { value: 'AB+', text: 'AB+' },
        { value: 'AB-', text: 'AB-' },
        { value: 'O+', text: 'O+' },
        { value: 'O-', text: 'O-' },
      ],
      stateOptions: ['Vivo', 'Finado', 'Coma', 'Vegetativo'], // Opciones para el campo State
      priorityOptions: ['urgente', 'alta', 'moderada'], // Opciones para el campo Priority
      transplantStatusOptions: ['Transplante exitoso', 'Recuperacion', 'Pendiente'] // Opciones para el campo Transplant_Status
    }
  },
  methods: {
    changeTab(val) {
      this.currentindex = val
    },
    onSubmit() {
      this.$router.replace('/user/user-list')
    },
    isRequire(value) {
      if (value && value.trim()) {
        return true
      }
      return 'This field is required'
    }
  }
}
</script>