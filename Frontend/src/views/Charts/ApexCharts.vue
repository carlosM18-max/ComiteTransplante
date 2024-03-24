<template>
  <b-container fluid>
    <b-row>
      <!-- Column Chart -->
      <b-col lg="6" v-for="(item, index) in charts" :key="'column' + index" v-if="item.type === 'column'">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>{{ item.title }}</h4>
          </template>
          <template v-slot:body>
            <ApexChart :element="item.type" :chartOption="item.bodyData" />
          </template>
        </iq-card>
      </b-col>
      <!-- Line Chart -->
      <b-col lg="6" v-for="(item, index) in charts" :key="'line' + index" v-if="item.type === 'line'">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>{{ item.title }}</h4>
          </template>
          <template v-slot:body>
            <ApexChart :element="item.type" :chartOption="item.bodyData" />
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
    generateData(baseval, count, yrange) {
      var i = 0
      var series = []
      while (i < count) {
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min
        var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15

        series.push([baseval, y, z])
        baseval += 86400000
        i++
      }
      return series
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
                colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
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
