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
                  <template v-for="column in columns" v-slot:[`cell(${column.key})`]="{ item }">
                    <span v-if="!item.editable" :key="column.key">{{ item[column.key] }}</span>
                    <input v-else type="text" v-model="item[column.key]" class="form-control text-center"
                      :key="'input_' + column.key" />
                  </template>
                  <template v-slot:cell(sort)>
                    <td>
                      <a href="#!" class="indigo-text"><i class="fa fa-long-arrow-up" aria-hidden="true"></i> <i
                          class="fa fa-long-arrow-down ms-1" aria-hidden="true"></i></a>
                    </td>
                  </template>
                  <template v-slot:cell(remove)="data">
                    <b-button variant=" iq-bg-success mr-1 mb-1" size="sm" @click="edit(data.item)"
                      v-if="!data.item.editable"><i class="ri-ball-pen-fill m-0"></i></b-button>
                    <b-button variant=" iq-bg-success mr-1 mb-1" size="sm" @click="submit(data.item)"
                      v-else>Ok</b-button>
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
      rows: []
    }
  }
}
</script>
