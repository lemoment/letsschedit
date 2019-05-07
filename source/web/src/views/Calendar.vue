<template>
    <div id="cal">
      <div>
        <router-link to="/">
          <img src="../assets/clock.png" alt="Clock" id="logo">
        </router-link>
        <h3 class="title">LET'S SCHED IT</h3>
      </div>
        <div class="actions">
            <button class="button"  v-on:click="sync()">Sync</button>
            <button class="button"  v-on:click="logout()">Logout</button>
        </div>
        <full-calendar id="overrider" :events="events"
                       :config="config"></full-calendar>
    </div>
</template>

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
            },
        }
    },
    props: {
        uuid: String,
        start: String,
        end: String,
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
            console.log("updated uuid!", this.currUuid)

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
                var vm = this;

                this.getcal() 
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
                
                // log data output
                console.log(JSON.stringify(data))

                // push to backend
                syncBackend(vm.$route.params.uuid, data)

                // retreive from the backend and update cal
                // it should have updated vm.backendres with the response
                vm.backendres.calendar.appointsments.forEach(element => {
                    let content = {}
                    content.start = element.start_time
                    content.end =  element.end_time
                    content.title = element.name
                    vm.events.push()
                })

                // should rerender automatically
            }
        },
        syncBackend(uuid, data) {
            // push data to the backend
            var vm = this;
            // only want to sync if auth is successful
            if (vm.$isAuthenticated() == true) {

                // push current user cal data to backend
                axios.put("http://127.0.0.1:5000/cal/" + toString(uuid) + "/sync",
                         data,
                         {
                            headers: {"Content-Type": "application/json"}
                        }) 
                    .then(r => console.log(vm.backendres = response))
                    .catch(e => console.log(e));
                
                console.log("sync happening!")
            } else {
                // attempt login
                vm.$login()
            }
        },
        getcal () {
            // TODO set min/max based on calendar info from backend get cal
            // get freebusy information from google of 
            // current user's primary calendar
            var vm = this;
            var date = new Date();
            date.setDate(date.getDate() + 7);

            this.$getGapiClient().then(gapi => {
                gapi.client.calendar.freebusy.query({
                'timeMin': (new Date()).toISOString(),
                'timeMax': (date.toISOString()),
                "items": [
                    {
                    "id": 'primary'
                    }
                ]
                }).then(function(response) {
                    vm.results = response.result
                    // console.log("google pull success!")
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

<style>
.title {
    margin: 0 0 0.7rem 0;
    font-size: 2rem;
}
#logo {
    float: left;
    padding: 0 1rem 0 1rem
}
#overrider .fc-state-default {
    background-color:white !important;
    text-shadow:none;
}
.comp-full-calendar {
    padding: 20px;
    background: #fff;
    max-width: 960px;
    margin: 0 auto;
}

.fc-state-default {
  /* non-theme */
  border: 1px solid;
  background-color: white;
  background-image: none; }
.actions {
    margin-bottom: 1rem;
}
.actions .button {
    border: 2px solid #52BDDF;
    box-sizing: border-box;
    border-radius: 10px;
    padding: 0.5rem 2.5rem 0.5rem 0.5rem;
    background-color: #FFFFFF;
    margin: 1rem 0 1rem 1rem;
    cursor: pointer;
    font-size: 1rem;
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
    color: #52BDDF;
}
.actions .button:hover{
    background-color: #52BDDF;
    color: #FFFFFF;
}
</style>