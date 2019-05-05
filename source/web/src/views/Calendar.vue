<template>
    <div id="cal">
      <div>
        <router-link to="/">
          <img src="../assets/clock.png" alt="Clock" id="logo">
        </router-link>
        <h3 class="title">LET'S SCHED IT</h3>
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
            config: {
                height: "auto",
                editable: false,
            },
        }
    },
    methods: {
        getcal () {
            var date = new Date();
            // set a date seven days in the future,
            // get a week of events
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
                console.log(response.result)
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
</style>