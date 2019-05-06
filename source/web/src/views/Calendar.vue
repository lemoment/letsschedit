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

export default {
    name: 'Calendar',
    data() {
        return {
            events: [
                {
                    title  : 'event1',
                    start  : '2019-05-05',
                },
                {
                    title  : 'event2',
                    start  : '2010-01-05',
                    end    : '2010-01-07',
                },
                {
                    title  : 'event3',
                    start  : '2010-01-09T12:30:00',
                    allDay : false,
                },
            ],
            results: {},
            config: {
                height: "auto",
                editable: false,
            },
        }
    },
    methods: {
        logout(){
            if (this.$isAuthenticated() == true) {
                this.$logout()
            }
            this.$router.push('/')
        },
        sync() {
            this.getcal()
        },
        getcal () {
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
                    results = response.result
            })})
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