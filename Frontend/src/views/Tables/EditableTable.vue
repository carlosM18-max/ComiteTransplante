<!-- eslint-disable prettier/prettier -->
<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Detalle Organos: </h4>
          </template>
          <template v-slot:body>
            <b-row>
              <b-col md="12" class="table-responsive w-100">
                <b-table striped bordered hover :items="rows" :fields="columns">
                  <template v-slot:cell(ID_A)="data">
                    <span v-if="!data.item.editable">{{ data.item.ID }}</span>
                    <input type="text" v-model="data.item.ID" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(Especificaciones)="data">
                    <span v-if="!data.item.editable">{{ data.item.Especificaciones }}</span>
                    <input type="text" v-model="data.item.Especificaciones" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(Restricciones)="data">
                    <span v-if="!data.item.editable">{{ data.item.Restricciones }}</span>
                    <input type="text" v-model="data.item.Restricciones" v-else class="form-control text-center" />
                  </template>
                  <template v-slot:cell(sort)>
                    <td>
                      <a href="#!" class="indigo-text"><i class="fa fa-long-arrow-up" aria-hidden="true"></i> <i
                          class="fa fa-long-arrow-down ms-1" aria-hidden="true"></i></a>
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
        { label: 'Acciones', key: 'remove', class: 'text-center' }
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
  },
}
</script>
