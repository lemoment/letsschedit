import Vue from 'vue'
import Router from 'vue-router'

import Login from './views/Login.vue'
import CreateEvent from './views/CreateEvent.vue' // secure route
import Calendar from './views/Calendar.vue' // secure route

Vue.use(Router)

const routes = [
  {
    path: '/',
    component: Login
  },
  {
    path: '/create-event',
    component: CreateEvent
  },
  {
    path: '/cal',
    component: Calendar
  }
]

export default new Router({
  mode: 'history',
  routes
})
