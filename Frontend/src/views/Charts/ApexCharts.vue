<template>
  <b-container fluid>
    <b-row>
      <!-- Column Chart -->
      <b-col lg="6" v-for="(item, index) in filteredCharts('column')" :key="'column' + index">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>{{ item.title }}</h4>
          </template>
          <template v-slot:body>
            <ApexChart :element="item.type" :chartOption="item.bodyData" v-if="item && item.type" />
          </template>
        </iq-card>
      </b-col>
      <!-- Line Chart -->
      <b-col lg="6" v-for="(item, index) in filteredCharts('line')" :key="'line' + index">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>{{ item.title }}</h4>
          </template>
          <template v-slot:body>
            <ApexChart :element="item.type" :chartOption="item.bodyData" v-if="item && item.type" />
          </template>
        </iq-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'
import ApexChart from '../../components/xray/charts/ApexChart'

export default {
  name: 'ApexCharts',
  components: { iqCard, ApexChart },
  mounted() {
    xray.index()
  },
  methods: {
    filteredCharts(chartType) {
      return this.charts.filter(item => item.type === chartType);
    }
  },
  data() {
    return {
      charts: [
        // Column Chart
        {
          title: 'Column Chart',
          type: 'column',
          bodyData: {
            chart: {
              height: 350,
              type: 'bar'
            },
            plotOptions: {
              bar: {
                horizontal: false,
                columnWidth: '55%',
                endingShape: 'rounded'
              }
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              show: true,
              width: 2,
              colors: ['transparent']
            },
            colors: ['#089bab', '#FC9F5B', '#e64141'],
            series: [
              {
                name: 'Net Profit',
                data: [44, 55, 57, 56, 61, 58]
              },
              {
                name: 'Revenue',
                data: [76, 85, 101, 98, 87, 105]
              },
              {
                name: 'Free Cash Flow',
                data: [35, 41, 36, 26, 45, 48]
              }
            ],
            xaxis: {
              categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
            },
            yaxis: {
              title: {
                text: '$ (thousands)'
              }
            },
            fill: {
              opacity: 1
            },
            tooltip: {
              y: {
                formatter: function (val) {
                  return '$ ' + val + ' thousands'
                }
              }
            }
          }
        },
        // Line Chart
        {
          title: 'Line Chart',
          type: 'line',
          bodyData: {
            chart: {
              height: 350,
              type: 'line',
              zoom: {
                enabled: false
              }
            },
            series: [
              {
                name: 'Desktops',
                data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
              }
            ],
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'straight'
            },
            title: {
              text: 'Product Trends by Month',
              align: 'left'
            },
            grid: {
              row: {
                colors: ['#f3f3f3', 'transparent'],
                opacity: 0.5
              }
            },
            xaxis: {
              categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
            }
          }
        },
        // Otros gráficos...
      ]
    }
  }
}
</script>
