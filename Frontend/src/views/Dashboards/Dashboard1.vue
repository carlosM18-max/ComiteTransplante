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
      <b-col sm="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Hospital Survey</h4>
          </template>
          <template v-slot:body>
            <div class="iq-card-body pb-0">
              <div class="row text-center">
                <div class="col-sm-3 col-6">
                  <h4 class="margin-0">$ 305</h4>
                  <p class="text-muted">Today's Income</p>
                </div>
                <div class="col-sm-3 col-6">
                  <h4 class="margin-0">$ 999</h4>
                  <p class="text-muted">This Week's Income</p>
                </div>
                <div class="col-sm-3 col-6">
                  <h4 class="margin-0">$ 4999</h4>
                  <p class="text-muted">This Month's Income</p>
                </div>
                <div class="col-sm-3 col-6">
                  <h4 class="margin-0">$ 90,000</h4>
                  <p class="text-muted">This Year's Income</p>
                </div>
              </div>
            </div>
            <div id="home-servey-chart"></div>
            <ApexChart element="home-chart-09" :chartOption="homesurvey" v-if="$route.meta.dark" />
            <ApexChart element="home-chart-09" :chartOption="chart9" v-else />
          </template>
        </iq-card>
      </b-col>
      <!-- Primeras graicas -->
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
      <!-- Tercera Grafica -->
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
      <!-- Cuarta Grafica -->
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
    </b-row>
  </b-container>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import { xray } from '../../config/pluginInit'
import IqCard from '../../components/xray/cards/iq-card'
// Chart
import ApexChart from '../../components/xray/charts/ApexChart'
import { BarChart, DoughnutChart } from 'vue-chart-3'
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { PieChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import VChart from 'vue-echarts'
import { ref } from 'vue'
import { Navigation, Pagination } from 'swiper/modules'
import CountUp from 'vue-countup-v3'
import 'swiper/css'
import 'swiper/scss'
import 'swiper/css/navigation'
import 'swiper/css/pagination'

export default {
  name: 'DashboardOne',
  components: { IqCard, ApexChart, CountUp, BarChart, DoughnutChart, VChart },
  mounted() {
    xray.index()
  },
  methods: {
    filteredCharts(chartType) {
      return this.charts.filter(item => item.type === chartType);
    }
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
          name2: 'Access From',
          type: 'pie',
          radius: '50%',
          data: [
            { value: 1048, name: 'January' }, // Nombre y valor del primer dato
            { value: 735, name: 'February' }, // Nombre y valor del segundo dato
            { value: 580, name: 'March' }, // Nombre y valor del tercer dato
            { value: 484, name: 'April' }, // Nombre y valor del cuarto dato
            { value: 300, name: 'May' } // Nombre y valor del quinto dato
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
      PieChartOption,
      modules: [Navigation, Pagination]
    }
  },
  data() {
    return {
      charts:[
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
      ],
      BarChartData: {
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
      },

      DoughnutChartData: {
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
      },
      slickOptions: {
        centerMode: false,
        centerPadding: '60px',
        slidesToShow: 5,
        slidesToScroll: 1,
        focusOnSelect: true,
        responsive: [
          {
            breakpoint: 992,
            settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '30',
              slidesToShow: 3
            }
          },
          {
            breakpoint: 480,
            settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '15',
              slidesToShow: 1
            }
          }
        ],
        nextArrow: '<a href="#" class="ri-arrow-left-s-line left"></a>',
        prevArrow: '<a href="#" class="ri-arrow-right-s-line right"></a>'
      },
      radialbar: {
        chart: {
          height: 350,
          type: 'radialBar'
        },
        plotOptions: {
          radialBar: {
            dataLabels: {
              name: {
                fontSize: '22px'
              },
              value: {
                fontSize: '16px'
              },
              total: {
                show: true,
                label: 'Total',
                formatter: function () {
                  // By default this function returns the average of all series. The below is just an example to show the use of custom formatter function
                  return 249
                }
              }
            }
          }
        },
        series: [44, 55, 67, 83],
        labels: ['Apples', 'Oranges', 'Bananas', 'Berries'],
        colors: ['#089bab', '#FC9F5B', '#75DDDD', '#ffb57e']
      },
      chart10: {
        chart: {
          height: 300,
          type: 'radialBar'
        },
        plotOptions: {
          radialBar: {
            dataLabels: {
              name: {
                fontSize: '22px'
              },
              value: {
                fontSize: '16px'
              },
              total: {
                show: true,
                label: 'Total',
                formatter: function () {
                  // By default this function returns the average of all series. The below is just an example to show the use of custom formatter function
                  return 249
                }
              }
            }
          }
        },
        series: [44, 55, 67, 83],
        labels: ['Apples', 'Oranges', 'Bananas', 'Berries'],
        colors: ['#089bab', '#FC9F5B', '#75DDDD', '#ffb57e']
      },
      chart9: {
        series: [
          {
            name: 'Cash Flow',
            data: [1.45, 5.42, 5.9, -0.42, -12.6, -18.1, -18.2, -14.16, -11.1, -6.09, 0.34, 3.88, 13.07, 5.8, 2, 7.37, 8.1, 13.57, 15.75, 17.1, 19.8, -27.03, -54.4, -47.2, -43.3, -18.6, -48.6, -41.1, -39.6, -37.6, -29.4, -21.4, -2.4]
          }
        ],
        chart: {
          type: 'bar',
          height: 350
        },
        plotOptions: {
          bar: {
            colors: {
              ranges: [
                {
                  from: -100,
                  to: -46,
                  color: '#e64141'
                },
                {
                  from: -45,
                  to: 0,
                  color: '#089bab'
                },
                {
                  from: 0,
                  to: 20,
                  color: '#FC9F5B'
                }
              ]
            },
            columnWidth: '80%'
          }
        },
        dataLabels: {
          enabled: false
        },
        yaxis: {
          title: {
            text: 'Growth'
          },
          labels: {
            formatter: function (y) {
              return y.toFixed(0) + '%'
            }
          }
        },
        xaxis: {
          type: 'datetime',
          categories: ['2011-01-01', '2011-02-01', '2011-03-01', '2011-04-01', '2011-05-01', '2011-06-01', '2011-07-01', '2011-08-01', '2011-09-01', '2011-10-01', '2011-11-01', '2011-12-01', '2012-01-01', '2012-02-01', '2012-03-01', '2012-04-01', '2012-05-01', '2012-06-01', '2012-07-01', '2012-08-01', '2012-09-01', '2012-10-01', '2012-11-01', '2012-12-01', '2013-01-01', '2013-02-01', '2013-03-01', '2013-04-01', '2013-05-01', '2013-06-01', '2013-07-01', '2013-08-01', '2013-09-01'],
          labels: {
            rotate: -90
          }
        }
      },
      chart1: {
        series: [
          {
            name: 'Net Profit',
            data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
          },
          {
            name: 'Revenue',
            data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
          }
        ],
        chart: {
          type: 'bar',
          height: 350
        },
        colors: ['#827af3', '#6ce6f4'],
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
        xaxis: {
          categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
        },
        yaxis: {},
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
      },
      darkChart1: {
        series: [
          {
            name: 'Net Profit',
            data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
          },
          {
            name: 'Revenue',
            data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
          }
        ],
        chart: {
          type: 'bar',
          foreColor: '#8c91b6',
          height: 350
        },
        colors: ['#827af3', '#6ce6f4'],
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
        xaxis: {
          categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
        },
        yaxis: {},
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
      },
      chart2: {
        series: [
          {
            name: 'Desktops',
            data: [5, 10, 8, 15]
          }
        ],
        chart: {
          height: 150,
          type: 'line',
          zoom: {
            enabled: false
          }
        },
        colors: ['#827af3'],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight'
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5
          }
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr']
        }
      },
      darkChart2: {
        series: [
          {
            name: 'Desktops',
            data: [5, 10, 8, 15]
          }
        ],
        chart: {
          height: 150,
          type: 'line',
          foreColor: '#8c91b6',
          zoom: {
            enabled: false
          }
        },
        colors: ['#827af3'],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight'
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5
          }
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr']
        }
      },
      chart3: {
        series: [44, 55, 13, 33],
        chart: {
          width: 380,
          height: 180,
          type: 'donut'
        },
        dataLabels: {
          enabled: false
        },
        colors: ['#827af3', '#6ce6f4', '#a09e9e', '#fbc647'],
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                show: false
              }
            }
          }
        ],
        legend: {
          position: 'right',
          offsetY: 0,
          height: 150
        }
      },
      darkChart3: {
        series: [44, 55, 13, 33],
        chart: {
          width: 380,
          height: 180,
          foreColor: '#8c91b6',
          type: 'donut'
        },
        dataLabels: {
          enabled: false
        },
        colors: ['#827af3', '#6ce6f4', '#a09e9e', '#fbc647'],
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                show: false
              }
            }
          }
        ],
        legend: {
          position: 'right',
          offsetY: 0,
          height: 150
        }
      },
      chart7: {
        chart: {
          height: 150,
          type: 'area',
          animations: {
            enabled: true,
            easing: 'linear',
            dynamicAnimation: {
              speed: 1000
            }
          },
          toolbar: {
            show: false
          },
          sparkline: {
            enabled: true
          },
          group: 'sparklines'
        },
        colors: ['#099fb0'],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight',
          width: 3
        },
        series: [
          {
            data: [80, 90, 60, 90, 44, 50, 98, 80, 90]
          }
        ],
        markers: {
          size: 4
        },
        yaxis: {
          max: 100
        },
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100]
          }
        },
        legend: {
          show: false
        }
      },
      chart8: {
        chart: {
          height: 150,
          type: 'area',
          animations: {
            enabled: true,
            easing: 'linear',
            dynamicAnimation: {
              speed: 1000
            }
          },
          toolbar: {
            show: false
          },
          sparkline: {
            enabled: true
          },
          group: 'sparklines'
        },
        colors: ['#fc9f5b'],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight',
          width: 3
        },
        series: [
          {
            data: [50, 60, 45, 90, 44, 50, 98, 75, 50]
          }
        ],
        markers: {
          size: 4
        },
        yaxis: {
          max: 100
        },
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100]
          }
        },
        legend: {
          show: false
        }
      }
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
  height: 342px;
  width: 785px;
}
</style>