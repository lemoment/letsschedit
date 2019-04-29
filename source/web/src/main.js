// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueGAPI from 'vue-gapi'
import { APITHING, CLIENTTHING } from './secrets'

Vue.config.productionTip = false

const apiConfig = {
  apiKey: 'AIzaSyBHaQ8UZkBv-VD9hUg9mAF08C6pA-rrdXY',
  clientId: '261348805351-0sjk6vlfu5v446pg3uciuaevmd4nms79.apps.googleusercontent.com',
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