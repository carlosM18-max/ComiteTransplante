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
                  <template v-slot:cell(sort)>
                    <td>
                      <a href="#!" class="indigo-text"><i class="fa fa-long-arrow-up" aria-hidden="true"></i> <i class="fa fa-long-arrow-down ms-1" aria-hidden="true"></i></a>
                    </td>
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
        ID: '',
        Nombre: '',
        Aparato_Sistema: '',
        Descripción: '',
        Detalle_Transplante_ID: '',
        Estatus: '',
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
      if (field === 'Estatus') {
        this.rows.sort((a, b) => {
          const statusA = a.Estatus.toLowerCase();
          const statusB = b.Estatus.toLowerCase();
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
        { label: 'Aparato Sistema', key: 'Aparato_Sistema', class: 'text-left' },
        { label: 'Descripción', key: 'Descripción', class: 'text-left' },
        { label: 'Detalle Transplante ID', key: 'Detalle_Transplante_ID', class: 'text-left' },
        { label: 'Estatus', key: 'Estatus', class: 'text-left', sortable: true }, // Columna "estatus" sortable
        { label: 'Sort', key: 'sort', class: 'text-left' },
        { label: 'Remove', key: 'remove', class: 'text-center' }
      ],
      rows: [
        {
          ID: '1',
          Nombre: 'Corazón',
          Aparato_Sistema: 'Cardiovascular',
          Descripción: 'Órgano muscular que bombea sangre a través del sistema circulatorio del cuerpo.',
          Detalle_Transplante_ID: '1',
          Estatus: 'grave',
          editable: false
        },
        {
          ID: '2',
          Nombre: 'Pulmones',
          Aparato_Sistema: 'Respiratorio',
          Descripción: 'Órganos esenciales para la respiración, donde se produce el intercambio gaseoso entre el oxígeno y el dióxido de carbono.',
          Detalle_Transplante_ID: '2',
          Estatus: 'estable',
          editable: false
        },
        {
          ID: '3',
          Nombre: 'Hígado',
          Aparato_Sistema: 'Digestivo',
          Descripción: 'Órgano que desempeña funciones vitales en el metabolismo, la desintoxicación y la producción de diversas sustancias bioquímicas necesarias para la digestión.',
          Detalle_Transplante_ID: '3',
          Estatus: 'crítico',
          editable: false
        }
      ]
    }
  }
}
</script>
