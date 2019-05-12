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
				<button data-p="this.$isAuthenticated()" class="button" @click="logout">Logout</button>
			</div>
		</div>

    <full-calendar id="overrider" :events="events" :config="config"></full-calendar>
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

#overrider .fc-state-default {
	background-color:white !important;
  text-shadow:none;
}

.fc-state-default {
  /* non-theme */
  border: 1px solid;
  background-color: white;
  background-image: none;
  color: #52BDDF;
  font-weight: bold;
}

/* Shift the calendar button over from the edges */
.fc-view, .fc-view > table {
  padding-left: 2rem;
  padding-right: 2rem;
}

.fc-day.fc-widget-content.fc-today {
  background-color: white !important;
}

/* Shift the first arrow button left 1rem */
.fc .fc-button-group > :first-child {
  margin-left: 1rem;
}

/* Shift the "day Button" right 1rem */
.fc .fc-agendaDay-button{
  margin-right: 1rem;
}

/* Change active button color */
.fc-toolbar .fc-state-active {
  color: white;
  background-color: #52BDDF;
  border-color: #52BDDF;
  font-family: Montserrat, sans-serif;
  box-shadow: none;
  text-shadow: none;
}

/*Change the event color*/
.fc-event, .fc-event-dot {
  background: #52BDDF;
  opacity: 1;
}

.fc-unselectable { display: none; }
</style>


<!-- JAVASCRIPT -->
<script>
import 'fullcalendar/dist/fullcalendar.css'
import moment from 'moment'
import axios from 'axios'

export default {
    name: 'Calendar',
    data() {
        return {
            events: [],
            token: "",
            results: {},
            backendres: {},
            currUuid: "",
            config: {
                height: "auto",
                editable: false,
                timeZone: 'local',
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
            if (this.$isAuthenticated() == true) {
                this.$logout()
            }
            // go back to the login screen
            this.$router.push('/')
        },
        sync() {
            // gets called by the sync button directly

            if (this.$isAuthenticated() !== true) {
                this.$login()
            } else if (this.$isAuthenticated() == true) {
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
                axios.post("http://127.0.0.1:5000/cal/" + uuid + "/sync", data,
                         {headers: {"Content-Type": "application/json"}})
                    .then(r => {
                        console.log(vm.backendres)
                        vm.backendres = r
                        vm.events = []
                        vm.backendres.data.calendar.appointments.forEach(element => {
                            let content = {}
                            content.start = element.start_time
                            content.end =  element.end_time
                            content.title = element.name
                            vm.events.push(content)
                        })
                    })
                    .catch(e => console.log(e));
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
                axios.get("http://127.0.0.1:5000/cal/" + uuid,
                         {headers: {"Content-Type": "application/json"}})
                    .then(r => {
                        console.log("fetch start and end")
                        vm.backendres = r
                        vm.start = r.data.calendar.start_date
                        vm.end = r.data.calendar.end_date
                    })
                    .catch(e => console.log(e));
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
                "items": [
                    {
                    "id": 'primary'
                    }
                ]
                }).then(function(response) {
                    vm.results = response.result
                    console.log(response)
            })})
        },
        gettoken () {
            var vm = this;
            // get the currently logged in users authentication token
            this.$getGapiClient()
                .then(gapi => {
                    // console.log("gapi", gapi)
                    return gapi.auth2.getAuthInstance()
                })
                .then(authinst => {
                    // console.log("authinst", authinst)
                    return authinst.currentUser.get()
                })
                .then(user => {
                    // console.log("user", user)
                    return user.getAuthResponse()
                })
                .then(res => {
                    // console.log(res.id_token)
                    vm.token = res.id_token
                })
        }
    }
}
</script>
