import Vue from 'vue'
import Router from 'vue-router'

import CreateLogin from './views/CreateLogin.vue'
import CreateEvent from './views/CreateEvent.vue' // secure route
import Calendar from './views/Calendar.vue' // secure route

Vue.use(Router)

const routes = [
  {
    path: '/',
    component: CreateLogin,
  },
  {
    path: '/create-event',
    component: CreateEvent,
  },
  {
    path: '/cal',
    redirect: '/'
  },
  { path: '/cal/:uuid',
    component: Calendar,
  }
]

const router =  new Router({
  mode: 'history',
  routes
})

export default router