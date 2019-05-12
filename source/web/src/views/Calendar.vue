<template>
  <div class="container">
		<div id="navbar">
			<h3 id="title">
				<router-link to="/">
					<img src="../assets/clock.png" alt="Clock" id="logo">
				</router-link>
				LET'S SCHED IT
			</h3>

			<div class="actions">
				<button class="button" @click="sync">Sync</button>
				<button v-if="this.$isAuthenticated()" class="button" @click="logout">Logout</button>
			</div>
		</div>

		<kalendar :configuration="config" :appointments="events" />
	</div>
</template>

<style scoped>
.container {
	padding: 0 2rem;
}

#navbar {
	display: flex;
	flex-direction: row;
	width: 100%;
	margin-top: 0rem;
	align-items: center;
}

#title {
	font-size: 2rem;
	flex: 1 0 auto;
}

#logo {
	float: left;
	padding: 0 1rem;
}

.actions {
	height: min-content;
	flex-shrink: 1;
	justify-content: right;
}

.actions .button {
	border: 2px solid #52BDDF;
	box-sizing: border-box;
	border-radius: 10px;
	padding: 0.5rem 1.1rem 0.5rem 1.1rem;
	background-color: #FFFFFF;
	cursor: pointer;
	font-size: 1rem;
	font-weight: bold;
	color: #52BDDF;
}

.actions .button:hover{
	background-color: #52BDDF;
	color: #FFFFFF;
}
</style>


<!-- JAVASCRIPT -->
<script>
import { Kalendar } from 'kalendar-vue'
import 'kalendar-vue/dist/KalendarVue.css'
import moment from 'moment'
import axios from 'axios'

export default {
  name: 'Calendar',
	components: { Kalendar },  
	data() {
		return {
			events: [],
      token: "",
      results: {},
      backendres: {},
      currUuid: "",
      config: {
				style: "material_design",
				view_type: "Month",
				split_value: 15,
				read_only: true,
				cell_height: 15
			},
      start: "",
      end: "",
    }
  },
  methods: {
		mounted () {
			// call when component is created
      this.fetchUUID
		},
    fetchUUID () {
			// this is a lifecycle hook on this component     
      // get the current uuid from the url
      this.currUuid = this.$route.params.uuid
      // pull the backend on component mount/update
      // based on uuid found on creation.
      this.getBackend(this.currUuid)
    }, 
    logout(){
      // gets called by the logout button directly
      if (this.$isAuthenticated() == true) this.$logout()
      // go back to the login screen
      this.$router.push('/')
    },
    sync() {
      // gets called by the sync button directly
			if (this.$isAuthenticated() !== true) this.$login()
      else if (this.$isAuthenticated() == true) {
        console.log("sync time!")
        var vm = this;
        this.getBackend(this.$route.params.uuid)
        this.getcal(vm.start,vm.end)
        this.gettoken()

				let data = {}
        data.events = [],
        data.provider = "Google",
        data.token = vm.token

        vm.results.calendars.primary.busy.forEach(element => {
          let ev = {}
          ev.start = element.start
          ev.end = element.end
          data.events.push(ev)
        });
                
        // push to backend
        this.syncBackend(this.$route.params.uuid, data)
               
        // retreive from the backend and update cal
        // it should have updated vm.backendres with the response
        // this.backendres.data.calendar.appointments.forEach(element => {
        //     let content = {}
        //     content.start = element.start_time
        //     content.end =  element.end_time
        //     content.title = element.name
        //     vm.events.push()
        // })
        // should rerender automatically
      }
    },
    syncBackend(uuid, data) {
			// push data to the backend
			var vm = this;
      // only want to sync if auth is successful
      if (vm.$isAuthenticated() == true) {
        // push current user cal data to backend
				axios.post("http://127.0.0.1:5000/cal/" + uuid + "/sync", data, {
					headers: {"Content-Type": "application/json"}
				}).then(r => {
					console.log(vm.backendres)
          vm.backendres = r
          vm.events = []

          vm.backendres.data.calendar.appointments.forEach(element => {
						let content = {}
						start_date = moment(element.start_time)
						end_date = moment(element.end_time)
						content.start = start_date.hours()
            content.end = end_date.hours()
            content.date = start_date.format("YYYY-MM-DD")
						vm.events.push(content)
          })
				}).catch(e => console.log(e));
      } else {
        // attempt login
        vm.$login()
      }
    },
    getBackend(uuid) {
			// push data to the backend
			var vm = this;
			// only want to sync if auth is successful
      if (vm.$isAuthenticated() == true) {
				// push current user cal data to backend
        axios.get("http://127.0.0.1:5000/cal/" + uuid, {
					headers: {"Content-Type": "application/json"}
				}).then(r => {
	        console.log("fetch start and end")
          vm.backendres = r
          vm.start = r.data.calendar.start_date
          vm.end = r.data.calendar.end_date
        }).catch(e => console.log(e));
      } else {
				// attempt login
        vm.$login()
      }
    },
    getcal (start, end) {
      // TODO set min/max based on calendar info from backend get cal
      // get freebusy information from google of 
      // current user's primary calendar
      var vm = this;
      var date = new Date();
           
			date.setDate(date.getDate() + 7);
      this.$getGapiClient().then(gapi => {
        gapi.client.calendar.freebusy.query({
					// 'timeMin': (new Date()).toISOString(),
					// 'timeMax': (date.toISOString()),
					'timeMin': start,
					'timeMax': end,
					"items": [{ "id": 'primary' }]
        }).then(function(response) {
					vm.results = response.result
          console.log(response)
        })
			})
    },
    gettoken () {
			var vm = this;
      // get the currently logged in users authentication token
      this.$getGapiClient().then(gapi => {
        // console.log("gapi", gapi)
        return gapi.auth2.getAuthInstance()
      }).then(authinst => {
			// console.log("authinst", authinst)
        return authinst.currentUser.get()
      }).then(user => {
        // console.log("user", user)
        return user.getAuthResponse()
      }).then(res => {
				// console.log(res.id_token)
       vm.token = res.id_token
      })
    }
  }
}
</script>
