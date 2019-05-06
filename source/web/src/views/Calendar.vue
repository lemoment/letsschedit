<template>
    <div id="cal">
      <div id="flow">
      	<div id="header">
        	<router-link to="/">
          		<img src="../assets/clock.png" alt="Clock" id="logo">
        	</router-link>
        	<h3 class="title">LET'S SCHED IT</h3>
    	</div>
        <div class="actions">
            <button class="button"  v-on:click="sync()">Sync</button>
            <button class="button"  v-on:click="logout()">Logout</button>
        </div>
      </div>
        <full-calendar id="overrider" :events="events"
                       :config="config"></full-calendar>
    </div>
</template>

<style>
html {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  background-color: #FFFFFF;
  color: #000000;
  text-align: left;
}
h3 {
  padding: 0;
}
#flow {
	display: flex;
	flex-flow: row nowrap;
	justify-content: space-between;
	align-items: baseline;
}
#header {
	padding-top: 0.3rem;
	flex: 2 0px;
    min-width: 23rem
}
.title {
    margin: 0.1rem 1rem 0.8rem 0.5rem;
    font-size: 2rem;
}
#logo {
    float: left;
    padding: 0 1rem 0 1rem
}
overrider .fc-state-default {
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
    margin-right: 1rem;
}
.actions .button {
    border: 2px solid #52BDDF;
    box-sizing: border-box;
    border-radius: 10px;
    padding: 0.5rem 1.1rem 0.5rem 1.1rem;
    background-color: #FFFFFF;
    margin: 1rem 0 2rem 1rem;
    cursor: pointer;
    font-size: 2rem;
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
    color: #52BDDF;
}
.actions .button:hover{
    background-color: #52BDDF;
    color: #FFFFFF;
}

@media (max-width: 725px) {
	#flow {
		flex-flow: column wrap;
		align-items: flex-start;
	}
    #header {
        min-width: 22rem
    }
    .actions .button {
        font-size: 1.5rem;
    }
}

</style>

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
