/* eslint-disable prettier/prettier */
import { createRouter, createWebHistory } from 'vue-router'
/* Layouts */
import Layout1 from '../layouts/Layout1.vue'

/* Dashboards View */
import Dashboard2 from '../views/Dashboards/Dashboard2.vue'
import Dashboard1 from '../views/Dashboards/Dashboard1.vue'
import Dashboard4 from '../views/Dashboards/Dashboard4'

/* Tables Views */
import TablesBasic from '../views/Tables/TablesBasic'
import DataTable from '../views/Tables/DataTable'
import EditableTable from '../views/Tables/EditableTable'
// Charts
import ApexCharts from '../views/Charts/ApexCharts'
import AmCharts from '../views/Charts/AmCharts'
import ChartJS from '../views/Charts/ChartJS.vue'
import Echart from '../views/Charts/EChart.vue'

// Form Wizard
import SimpleWizard from '../views/FormWizard/SimpleWizard.vue'
import ValidateWizard from '../views/FormWizard/ValidateWizard.vue'
import VerticalWizard from '../views/FormWizard/VerticalWizard.vue'
// Vue.use(VueRouter)

const childRoutes = (prop, mode) => [
  {
    path: 'home-1',
    name: prop + '.home-1',
    meta: { dark: mode, auth: true, name: 'Home 1' },
    component: Dashboard1
  },
  {
    path: 'home-2',
    name: prop + '.home-2',
    meta: { dark: mode, auth: true, name: 'Home 2' },
    component: Dashboard2
  },
  {
    path: '/',
    name: prop + '.home-4',
    meta: { dark: mode, auth: true, name: 'Home 4' },
    component: Dashboard4
  }
]

const formWizardRoute = (prop, mode = false) => [
  {
    path: 'simple-wizard',
    name: prop + '.simpleWizard',
    meta: { dark: mode, auth: true, name: 'Simple Wizard' },
    component: SimpleWizard
  },
  {
    path: 'validate-wizard',
    name: prop + '.validateWizard',
    meta: { dark: mode, auth: true, name: 'Validate Wizard' },
    component: ValidateWizard
  },
  {
    path: 'vertical-wizard',
    name: prop + '.verticalWizard',
    meta: { dark: mode, auth: true, name: 'Vertical Wizard' },
    component: VerticalWizard
  }
]
const tableChildRoute = (prop, mode = false) => [
  {
    path: 'tables-basic',
    name: prop + '.basic',
    meta: { dark: mode, auth: true, name: 'Basic' },
    component: TablesBasic
  },
  {
    path: 'data-table',
    name: prop + '.dataTable',
    meta: { dark: mode, auth: true, name: 'Datatable' },
    component: DataTable
  },
  {
    path: 'editable',
    name: prop + '.editable',
    meta: { dark: mode, auth: true, name: 'Editable' },
    component: EditableTable
  }
]


const chartChildRoutes = (prop, mode = false) => [
  {
    path: 'apex-charts',
    name: prop + '.apex',
    meta: { dark: mode, auth: true, name: 'Apex Chat' },
    component: ApexCharts
  },
  {
    path: 'am-charts',
    name: prop + '.am',
    meta: { dark: mode, auth: true, name: 'Am Chart' },
    component: AmCharts
  },
  // {
  //   path: "high-charts",
  //   name: prop + ".high",
  //   meta: { dark: mode, auth: true, name: "High Chart" },
  //   component: HighCharts,
  // },
  {
    path: 'echart',
    name: prop + '.echart',
    meta: { dark: mode, auth: true, name: 'Echart' },
    component: Echart
  },
  // {
  //   path: "morris-charts",
  //   name: prop + ".morris",
  //   meta: { dark: mode, auth: true, name: "Mirris Chart" },
  //   component: MorrisCharts,
  // },
  {
    path: 'chartJS',
    name: prop + '.chartJS',
    meta: { auth: true, name: 'ChartJs' },
    component: ChartJS
  }
]


const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: Layout1,
    meta: { auth: true },
    children: childRoutes('dashboard')
  },
  {
    path: '/table',
    name: 'table',
    component: Layout1,
    meta: { auth: true },
    children: tableChildRoute('table')
  },
  {
    path: '/chart',
    name: 'chart',
    component: Layout1,
    meta: { auth: true },
    children: chartChildRoutes('chart')
  },
  {
    path: '/form-wizard',
    name: 'formWizard',
    component: Layout1,
    meta: { auth: true },
    children: formWizardRoute('formWizard')
  },

]

const router = createRouter({
  history: createWebHistory(process.env.VUE_APP_BASE_URL),
  base: process.env.VUE_APP_BASE_URL,
  routes
})

export default router
