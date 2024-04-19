<!-- eslint-disable prettier/prettier -->
<template>
  <b-container fluid>
    <b-row>
      <b-col lg="12">
        <b-row>
          <b-col md="6" lg="3">
            <iq-card body-class="iq-bg-primary rounded-4">
              <template v-slot:body>
                <div class="d-flex align-items-center justify-content-between">
                  <div class="rounded-circle iq-card-icon bg-primary">
                    <i class="ri-user-fill"></i>
                  </div>
                  <div class="text-end">
                    <h2 class="mb-0">
                      <span><count-up :end-val="5600" duration="5"></count-up></span>
                    </h2>
                    <h5 class="">Doctors</h5>
                  </div>
                </div>
              </template>
            </iq-card>
          </b-col>
          <b-col md="6" lg="3">
            <iq-card body-class="iq-bg-warning rounded-4">
              <template v-slot:body>
                <div class="d-flex align-items-center justify-content-between">
                  <div class="rounded-circle iq-card-icon bg-warning">
                    <i class="ri-women-fill"></i>
                  </div>
                  <div class="text-end">
                    <h2 class="mb-0">
                      <span><count-up :end-val="3450" duration="5"></count-up></span>
                    </h2>
                    <h5 class="">Nurses</h5>
                  </div>
                </div>
              </template>
            </iq-card>
          </b-col>
          <b-col md="6" lg="3">
            <iq-card body-class="iq-bg-danger rounded-4">
              <template v-slot:body>
                <div class="d-flex align-items-center justify-content-between">
                  <div class="rounded-circle iq-card-icon bg-danger">
                    <i class="ri-group-fill"></i>
                  </div>
                  <div class="text-end">
                    <h2 class="mb-0">
                      <span><count-up :end-val="3500" duration="5"></count-up></span>
                    </h2>
                    <h5 class="">Patients</h5>
                  </div>
                </div>
              </template>
            </iq-card>
          </b-col>
          <b-col md="6" lg="3">
            <iq-card body-class="iq-bg-info rounded-4">
              <template v-slot:body>
                <div class="d-flex align-items-center justify-content-between">
                  <div class="rounded-circle iq-card-icon bg-info">
                    <i class="ri-hospital-line"></i>
                  </div>
                  <div class="text-end">
                    <h2 class="mb-0">
                      <span><count-up :end-val="4500" duration="5"></count-up></span>
                    </h2>
                    <h5 class="">Pharmacists</h5>
                  </div>
                </div>
              </template>
            </iq-card>
          </b-col>
        </b-row>
      </b-col>

      <!-- Primeras graicas -->
      <b-col lg="6" sm="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>Recuento total de órganos solicitados</h4>
          </template>
          <template v-slot:body>
            <v-chart class="chart" :option="PieChartData" />
          </template>
        </iq-card>
      </b-col>
      <b-col lg="6" sm="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>Solicitudes generadas</h4>
          </template>
          <template v-slot:body>
            <DoughnutChart :chartData="DoughnutChartData" />
          </template>
        </iq-card>
      </b-col>
      <!-- Tercera Grafica -->
      <!-- Cuarta Grafica -->
    </b-row>
  </b-container>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import { xray } from '../../config/pluginInit'
import IqCard from '../../components/xray/cards/iq-card'
// Chart
// import ApexChart from '../../components/xray/charts/ApexChart'
import { DoughnutChart } from 'vue-chart-3'
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { PieChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import VChart from 'vue-echarts'
import { ref } from 'vue'
// import { Navigation, Pagination } from 'swiper/modules'
import CountUp from 'vue-countup-v3'
import 'swiper/css'
import 'swiper/scss'
import 'swiper/css/navigation'
import 'swiper/css/pagination'
import { obtenerSolicitudes } from '@/services/solicitudes'
import { obtenerOrganos } from '@/services/organos'

let obtenerSolicitudesInstancia = []
let obtenerOrganosInstancia = []

export default {
  name: 'DashboardOne',
  components: { IqCard, CountUp, DoughnutChart, VChart },
  async mounted() {
    xray.index()
    await obtenerSolicitudes().then(solicitudes => {
      obtenerSolicitudesInstancia = solicitudes
    }).catch(error => {
      console.error(`Error: ${error}`)
    })

    await obtenerOrganos().then(organos => {
      obtenerOrganosInstancia = organos
    }).catch(error => {
      console.error(`Error: ${error}`)
    })

    this.gr_estatusSolicitudes()
    this.gr_organos()
  },
  methods: {
    gr_organos() {
      obtenerSolicitudesInstancia.forEach(solicitud => {
        let obtenerOrgano = obtenerOrganosInstancia.find(organo => organo.ID == solicitud.organo_ID)
        let indice = this.organos.findIndex(organo => organo.name === obtenerOrgano.nombre);
        if (indice != -1) {
          this.organos[indice].value++
        } else {
          this.organos.push({ value: 1, name: obtenerOrgano.nombre })
        }
      })

      this.PieChartData = ref({
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: this.organos,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      })
    },
    gr_estatusSolicitudes() {
      obtenerSolicitudesInstancia.forEach(solicitud => {
        switch (solicitud.estatus) {
          case 'Pendiente':
            this.solicitudes.pendiente++
            break;
          case 'Recuperacion':
            this.solicitudes.recuperacion++
            break;
          case 'Transplante exitoso':
            this.solicitudes.transplante_exitoso++
            break;
          default:
            console.error("¡No existe el estatus!")
            break;
        }
      })

      this.DoughnutChartData = {
        type: 'doughnut',
        labels: ['Pendientes', 'En recuperación', 'Transplante exitoso'],
        datasets: [
          {
            label: 'Donut Chart',
            data: [this.solicitudes.pendiente, this.solicitudes.recuperacion, this.solicitudes.transplante_exitoso],
            backgroundColor: ['rgba(242, 99, 97, 1)', 'rgba(252, 159, 91, 1)', 'rgba(87, 222, 83, 1)'],
            hoverOffset: 4,
            borderSkipped: false
          }
        ],
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top'
            },
            title: {
              display: true,
              text: 'Chart.js Doughnut Chart'
            }
          }
        }
      }
    }
  },
  setup() {
    use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent])
  },
  data() {
    return {
      solicitudes: {
        pendiente: 0,
        recuperacion: 0,
        transplante_exitoso: 0
      },
      organos: [],
      DoughnutChartData: {},
      PieChartData: {},
      obtenerSolicitudesInstancia,
      obtenerOrganosInstancia,
    }
  }
}
</script>
<!-- eslint-disable prettier/prettier -->
<style>
.iq-card-body {
  flex: unset;
}
</style>
<!-- eslint-disable prettier/prettier -->
<style scoped></style>
<!-- eslint-disable prettier/prettier -->
<style scoped>
.chart {
  height: 400px;
  width: 785px;
}
</style>