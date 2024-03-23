<!-- eslint-disable prettier/prettier -->
<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Solicitudes: </h4>
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
                  <template v-slot:cell(ID)="data">
                    <span v-if="!data.item.editable">{{ data.item.ID }}</span>
                    <input type="text" v-model="data.item.ID" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(Nombre)="data">
                    <span v-if="!data.item.editable">{{ data.item.Nombre }}</span>
                    <input type="text" v-model="data.item.Nombre" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(Medico)="data">
                    <span v-if="!data.item.editable">{{ data.item.Medico }}</span>
                    <input type="text" v-model="data.item.Medico" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(Tipo_organo)="data">
                    <span v-if="!data.item.editable">{{ data.item.Tipo_organo }}</span>
                    <input type="text" v-model="data.item.Tipo_organo" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(prioridad)="data">
                    <span v-if="!data.item.editable">{{ data.item.prioridad }}</span>
                    <input type="text" v-model="data.item.prioridad" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(fecha_de_la_solicitud)="data">
                    <span v-if="!data.item.editable">{{ data.item.fecha_de_la_solicitud }}</span>
                    <input type="text" v-model="data.item.fecha_de_la_solicitud" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(dias_espera)="data">
                    <span v-if="!data.item.editable">{{ data.item.dias_espera }}</span>
                    <input type="text" v-model="data.item.dias_espera" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(estatus)="data">
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
              </b-col>
            </b-row>
          </template>
        </iq-card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'
export default {
  name: 'UiDataTable',
  components: { iqCard },
  mounted() {
    xray.index()
  },
  methods: {
    add() {
      let obj = this.default()
      this.rows.push(obj)
    },
    default() {
      return {
        id: this.rows.length,
        ID: '',
        Nombre: '',
        Medico: '',
        Tipo_organo: '',
        prioridad: '',
        fecha_de_la_solicitud: '',
        dias_espera: '',
        estatus: '',
        editable: false
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
        { label: 'Nombre', key: 'Nombre', class: 'text-left' },
        { label: 'Medico', key: 'Medico', class: 'text-left' },
        { label: 'Tipo_organo', key: 'Tipo_organo', class: 'text-left' },
        { label: 'prioridad', key: 'prioridad', class: 'text-left' },
        { label: 'fecha_de_la_solicitud', key: 'fecha_de_la_solicitud', class: 'text-left' },
        { label: 'dias_espera', key: 'dias_espera', class: 'text-left' },
        { label: 'estatus', key: 'estatus', class: 'text-left', sortable: true }, // Hacer la columna "estatus" sortable
        { label: 'Sort', key: 'sort', class: 'text-left' },
        { label: 'Remove', key: 'remove', class: 'text-center' }
      ],
      rows: [
        {
          id: 1,
          ID: '1',
          Nombre: 'Gio Metric',
          Medico: 'Dr. Mendoza',
          Tipo_organo: 'Corazon',
          prioridad: 'Urgente',
          fecha_de_la_solicitud: '12/05/2020',
          dias_espera: '10',
          estatus: 'grave',
          editable: false
        },
        {
          id: 2,
          ID: '2',
          Nombre: 'Manny Petty',
          Medico: 'Dra. Carmen',
          Tipo_organo: 'Higado',
          prioridad: 'Alta',
          fecha_de_la_solicitud: '01/02/2015',
          dias_espera: '5',
          estatus: 'estable',
          editable: false
        },
        {
          id: 2,
          ID: '2',
          Nombre: 'Manny Petty',
          Medico: 'Dr.Hugo',
          Tipo_organo: 'Cerebro',
          prioridad: 'Moredada',
          fecha_de_la_solicitud: '04/12/2021',
          dias_espera: '10',
          estatus: 'critico', 
          editable: false
        },
        // Puedes añadir más objetos de fila si es necesario
      ]
    }
  }
}
</script>