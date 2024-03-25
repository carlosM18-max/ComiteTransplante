<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>Bar Chart</h4>
          </template>
          <template v-slot:body>
            <BarChart :chartData="BarChartData" />
          </template>
        </iq-card>
      </b-col>
      <b-col lg="6" sm="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>Doughnut Chart</h4>
          </template>
          <template v-slot:body>
            <DoughnutChart :chartData="DoughnutChartData" />
          </template>
        </iq-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'

// Chart
import { BarChart, DoughnutChart } from 'vue-chart-3'
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)
export default {
  name: 'ChartJs',
  components: { iqCard,  BarChart, DoughnutChart },
  mounted() {
    xray.index()
    // Additional chart initialization can go here
  },
  data() {
    const BarChartData = {
      labels: ['August', 'September', 'October', 'November', 'December', 'January', 'February'],
      datasets: [
        {
          label: 'Bar Chart',
          data: [65, 59, 80, 81, 55, 55],
          backgroundColor: 'rgba(8, 155, 171, 1)',
          borderColor: 'rgba(8, 155, 171, 1)',
          tension: 0.1,
          borderSkipped: false
        }
      ],
      options: {
        responsive: true,
        plugins: {
          legends: {
            display: false
          }
        }
      }
    }

    const DoughnutChartData = {
      type: 'doughnut',
      labels: ['January', 'February', 'March', 'April', 'May'],
      datasets: [
        {
          label: 'Donut Chart',
          data: [10, 20, 15, 30, 25],
          backgroundColor: ['rgba(8, 155, 171, 1)', 'rgba(252, 159, 91, 1)', 'rgba(242, 99, 97, 1)', 'rgba(87, 222, 83, 1)', 'rgba(97, 226, 252, 1)'],
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

    // Define other chart data objects here

    return { BarChartData, DoughnutChartData /* Add other chart data objects here */ }
  }
}
</script>

<style scoped></style>
