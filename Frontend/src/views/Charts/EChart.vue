<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>Pie Chart</h4>
          </template>
          <template v-slot:body>
            <v-chart class="chart" :option="PieChartOption" />
          </template>
        </iq-card>
      </b-col>
      <!-- Otros gráficos -->
    </b-row>
  </b-container>
</template>

<script>
import iqCard from '../../components/xray/cards/iq-card'
import { xray } from '../../config/pluginInit'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { PieChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import VChart from 'vue-echarts'
import { ref } from 'vue'


export default {
  name: 'PieChartComponent',
  components: { iqCard, VChart },
  mounted() {
    xray.index()
  },
  setup() {
    use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent])

    const PieChartOption = ref({
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
          data: [
            { value: 1048, name: 'January' },
            { value: 735, name: 'February' },
            { value: 580, name: 'March' },
            { value: 484, name: 'April' },
            { value: 300, name: 'May' }
          ],
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

    return {
      PieChartOption
    }
  }
}
</script>

<style scoped>
.chart {
  height: 342px;
  width: 785px;
}
</style>
