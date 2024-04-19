<!-- eslint-disable prettier/prettier -->
<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Solicitudes</h4>
          </template>
          <template v-slot:body>
            <b-row>
              <div class="table-ad mb-3 me-2">
                  <router-link :to="{ name: 'formWizard.simpleWizard' }">
                  <b-button variant="btn btn-sm iq-bg-success float-end">+ Agregar Nueva</b-button>
                </router-link>
              </div>
              <b-col md="12" class="table-responsive w-100">
                <b-table striped bordered hover :items="rows" :fields="columns">
                  <template v-slot:cell(ID_A)="data">
                    <span v-if="!data.item.editable">{{ data.item.ID }}</span>
                    <input type="text" v-model="data.item.ID" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(paciente_ID)="data">
                    <span v-if="!data.item.editable">{{ data.item.paciente_ID }}</span>
                    <input type="text" v-model="data.item.paciente_ID" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(medico_ID)="data">
                    <span v-if="!data.item.editable">{{ data.item.medico_ID }}</span>
                    <input type="text" v-model="data.item.medico_ID" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(organo_ID)="data">
                    <span v-if="!data.item.editable">{{ data.item.organo_ID }}</span>
                    <input type="text" v-model="data.item.organo_ID" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(prioridad)="data">
                    <span v-if="!data.item.editable">{{ data.item.prioridad }}</span>
                    <input type="text" v-model="data.item.prioridad" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(fecha_solicitud)="data">
                    <span v-if="!data.item.editable">{{ data.item.fecha_solicitud }}</span>
                    <input type="text" v-model="data.item.fecha_solicitud" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(dias_espera_A)="data">
                    <span v-if="!data.item.editable">{{ data.item.dias_espera }}</span>
                    <input type="text" v-model="data.item.dias_espera" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(estatus_A)="data">
                    <span v-if="!data.item.editable">{{ data.item.estatus }}</span>
                    <input type="text" v-model="data.item.estatus" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(sort)>
                    <td>
                      <a href="#!" class="indigo-text"><i class="fa fa-long-arrow-up" aria-hidden="true"></i> <i class="fa fa-long-arrow-down ms-1" aria-hidden="true"></i></a>
                    </td>
                  </template>
                  <template v-slot:cell(remove)="data">
                    <b-button
                      variant=" iq-bg-success mr-1 mb-1"
                      size="sm"
                      @click="edit(data.item)"
                      v-if="!data.item.editable"
                      ><i class="ri-ball-pen-fill m-0"></i
                    ></b-button>
                    <b-button
                      variant=" iq-bg-success mr-1 mb-1"
                      size="sm"
                      @click="submit(data.item)"
                      v-else
                      >Ok</b-button
                    >
                    <b-button variant=" iq-bg-danger" size="sm" @click="remove(data.item)">Remover </b-button>
                  </template>
                </b-table>
                <b-pagination v-model="currentPage" :total-rows="totalRows" :per-page="perPage"
                  class="mt-3 justify-content-center" />
              </b-col>
            </b-row>
          </template>
        </iq-card>
      </b-col>
    </b-row>
  </b-container>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import iqCard from '../../components/xray/cards/iq-card'
import { obtenerOrganos } from '@/services/organos';
import { obtenerPersonas } from '@/services/personas'
import { obtenerPersonalMedico } from '@/services/personal_medico'
import { obtenerSolicitudes } from '@/services/solicitudes'

let obtenerOrganosInstancia = []
let obtenerPersonasInstancia = []
let obtenerPersonalMedicoInstancia = []
let obtenerSolicitudesInstancia = []

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

obtenerSolicitudes().then(solicitudes => {
  obtenerSolicitudesInstancia = solicitudes
}).catch(error => {
  console.error(`Error: ${error}`)
})

export default {
  name: 'UiDataTable',
  components: { iqCard },
  mounted() {
    this.llenarTabla()
  },
  methods: {
    llenarTabla() {
      let donatario_encontrado
      let medico_encontrado
      let organo_encontrado

      let solicitudes = []
      obtenerSolicitudesInstancia.forEach(solicitud => {
        donatario_encontrado = obtenerPersonasInstancia.find(persona => persona.ID == solicitud.paciente_ID)
        medico_encontrado = obtenerPersonasInstancia.find(persona => persona.ID == solicitud.medico_ID)
        organo_encontrado = obtenerOrganosInstancia.find(organo => organo.ID == solicitud.organo_ID)

        let objSolicitud = {
          ID: solicitud.ID,
          prioridad: solicitud.prioridad,
          fecha_solicitud: solicitud.fecha_solicitud,
          dias_espera: solicitud.dias_espera,
          estatus: solicitud.estatus,
          estatus_aprobacion: solicitud.estatus_aprobacion,
          paciente_ID: donatario_encontrado.nombre + ' ' + donatario_encontrado.primer_apellido + ' ' + donatario_encontrado.segundo_apellido,
          medico_ID: medico_encontrado.nombre + ' ' + medico_encontrado.primer_apellido + ' ' + medico_encontrado.segundo_apellido,
          organo_ID: organo_encontrado.nombre
        }

        solicitudes.push(objSolicitud)
      })

      this.rows = solicitudes

    },
    default() {
      return {
        id: this.rows.length,
        ID: '',
        donatario_ID: '',
        donador_ID: '',
        medico_ID: '',
        organo_ID: '',
        prioridad: '',
        fecha_solicitud: '',
        dias_espera: '',
        estatus: '',
        editable: false,
      }
    },
    edit(item) {
      item.editable = true
    },
    submit(item) {
      item.editable = false
    },
    remove(item) {
      let index = this.rows.indexOf(item)
      this.rows.splice(index, 1)
    },
    sort(field) {
      if (field === 'estatus') {
        this.rows.sort((a, b) => {
          const statusA = a.estatus.toLowerCase();
          const statusB = b.estatus.toLowerCase();
          if (statusA < statusB) return -1;
          if (statusA > statusB) return 1;
          return 0;
        });
      } else {
        this.rows.sort((a, b) => (a[field] > b[field]) ? 1 : ((b[field] > a[field]) ? -1 : 0));
      }
    }
  },
  data() {
    return {
      columns: [
        { label: 'ID', key: 'ID', class: 'text-left' },
        { label: 'Nombre del Donatario', key: 'paciente_ID', class: 'text-left' },
        { label: 'Nombre del Donador', key: 'donador_ID', class: 'text-left' },
        { label: 'Medico', key: 'medico_ID', class: 'text-left' },
        { label: 'Organo a Donar', key: 'organo_ID', class: 'text-left' },
        { label: 'Prioridad', key: 'prioridad', class: 'text-left' },
        { label: 'Fecha de Solicitud', key: 'fecha_solicitud', class: 'text-left' },
        { label: 'Dias de Espera', key: 'dias_espera', class: 'text-left' },
        { label: 'Estatus', key: 'estatus', class: 'text-left', sortable: true },
        { label: 'Sort', key: 'sort', class: 'text-left' },
        { label: 'Acciones', key: 'remove', class: 'text-center' }
      ],
      rows: [],
      obtenerPersonasInstancia,
      obtenerPersonalMedicoInstancia,
      obtenerOrganosInstancia,
      obtenerSolicitudesInstancia,
      perPage: 10, // Número de registros por página
      currentPage: 1, // Página actual
    }
  },
  computed: {
    totalRows() {
      return this.rows.length;
    },
    paginatedRows() {
      const startIndex = (this.currentPage - 1) * this.perPage;
      const endIndex = startIndex + this.perPage;
      return this.rows.slice(startIndex, endIndex);
    }
  }
}
</script>
