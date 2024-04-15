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
                  <template v-for="column in columns" v-bind:key="column.key" v-slot:[`cell(${column.key})`]="data">
                    <span v-if="!data.item.editable">{{ data.item[column.key] }}</span>
                    <input v-else type="text" v-model="data.item[column.key]" class="form-control text-center" />
                  </template>
                  <template v-slot:cell(remove)="data">
                    <b-button variant="iq-bg-danger" size="sm" @click="remove(data.item)">
                      Remover <i class="ri-delete-bin-line"></i>
                    </b-button>
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
<!-- eslint-disable prettier/prettier -->
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
        Especificaciones: '',
        Restricciones: '',
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
    }
  },
  data() {
    return {
      columns: [
        { label: 'ID', key: 'ID', class: 'text-left' },
        { label: 'Especificaciones', key: 'Especificaciones', class: 'text-left' },
        { label: 'Restricciones', key: 'Restricciones', class: 'text-left' },
        { label: 'Remove', key: 'remove', class: 'text-center' }
      ],
      rows: [
        {
          id: 1,
          ID: '1',
          Especificaciones: 'Espec 1',
          Restricciones: 'Restric 1',
          editable: false
        },
        {
          id: 2,
          ID: '2',
          Especificaciones: 'Espec 2',
          Restricciones: 'Restric 2',
          editable: false
        },
        {
          id: 3,
          ID: '3',
          Especificaciones: 'Espec 3',
          Restricciones: 'Restric 3',
          editable: false
        }
      ]
    }
  }
}
</script>
