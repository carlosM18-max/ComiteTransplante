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
                  <template v-for="column in columns" v-slot:[`cell(${column.key})`]="{ item }">
                    <span v-if="!item.editable" :key="column.key">{{ item[column.key] }}</span>
                    <input v-else type="text" v-model="item[column.key]" class="form-control text-center"
                      :key="'input_' + column.key" />
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
                <b-pagination v-model="currentPage" :total-rows="totalRows" :per-page="perPage" class="mt-3" />
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
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'
import axios from 'axios'
export default {
  name: 'UiDataTable',
  components: { iqCard },
  mounted() {
    xray.index(),
      this.fetchData()
  },
  methods: {
    fetchData() {
      // Utiliza Axios para obtener los datos del backend
      axios.get('http://localhost:8000/hospital/api/v1solicitud_transplantes/')
        .then(response => {
          this.rows = response.data;
        })
        .catch(error => {
          console.error('Error al obtener los datos del backend:', error);
        });
    },
    add() {
      let obj = this.default()
      this.rows.push(obj)
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
        { label: 'Nombre del Donatario', key: 'donatario_ID', class: 'text-left' }, 
        { label: 'Nombre del Donador', key: 'donador_ID', class: 'text-left' }, 
        { label: 'Medico', key: 'medico_ID', class: 'text-left' }, 
        { label: 'Organo a Donar', key: 'organo_ID', class: 'text-left' }, 
        { label: 'Prioridad', key: 'prioridad', class: 'text-left' }, 
        { label: 'Fecha de Solicitud', key: 'fecha_solicitud', class: 'text-left' }, 
        { label: 'Dias de Espera', key: 'dias_espera', class: 'text-left' }, 
        { label: 'Estatus', key: 'estatus', class: 'text-left', sortable: true }, 
        { label: 'Sort', key: 'sort', class: 'text-left' },
        { label: 'Remove', key: 'remove', class: 'text-center' }
      ],
      rows: [],
    }
  }
}
</script>
