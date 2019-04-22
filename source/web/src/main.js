// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueGAPI from 'vue-gapi'
import { APITHING, CLIENTTHING } from './secrets'

Vue.config.productionTip = false

const apiConfig = {
  apiKey: APITHING,
  clientId: CLIENTTHING + '.apps.googleusercontent.com.apps.googleusercontent.com',
  discoveryDocs: ['https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest'],
  scope: 'https://www.googleapis.com/auth/calendar.readonly'
}

Vue.use(VueGAPI, apiConfig)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
