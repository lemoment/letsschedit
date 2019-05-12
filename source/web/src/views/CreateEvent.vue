<template>
	<div class="container">
		<h3 id="title">
			<router-link to="/"><img src="../assets/clock.png" alt="Logo" id="logo"></router-link>
			LET'S SCHED IT.
		</h3>

		<form id="event-form" @submit.prevent="schedit()"> 
			<label for="name">Create an event named</label>
			<input type="text" id="name" name="name" v-model="event.name" placeholder="Name">

			<label for="startDate">between</label>
			<input onfocus="(this.type='date')" id="startDate" v-model="event.startDate" onblur="(this.id='filledData')" placeholder="Start Date">

			<label for="endDate">and</label>
			<input onfocus="(this.type='date')" id="endDate" v-model="event.endDate" onblur="(this.id='filledData')" placeholder="End Date">

			<label for="startTime">within</label>
       <input onfocus="(this.type='time')" id="startTime" v-model="event.startTime" onblur="(this.id='filledData')" name="startTime" placeholder="Start Time">

       <label for="endTime">to</label>
       <input onfocus="(this.type='time')" id="endTime"  v-model="event.endTime" onblur="(this.id='filledData')" name="endTime" placeholder="End Time">
       <label>.</label>
		</form>
		
		<button form="event-form" type="submit" class="button" style="display: block;">SCHED IT!</button>
  </div>
</template>

<!-- CSS -->
<style scoped>
.container {
	padding: 2rem 2rem 0 2rem;
}

#title {
	margin: 0 0 3rem
}

#logo {
	float: left;
	padding: 0 1rem
}

h3 {
	font-size: 2rem
}

#event-form {
	flex-flow: row wrap;
	background-color: #e5e5e5;
	padding: 1.5rem
}

#event-form input {
	padding: 3px 0;
	margin: 7px 10px;
	box-sizing: border-box;
	border: 2px solid #000;
	border-radius: 10px;
	background-color: #FFF;
	text-align: center;
	color: #545454;
	width: 15rem;
	vertical-align: middle;
	font-weight: 700;
	font-size: 2.2rem;
}

#event-form input[type=date] {
	font-size: 1.5rem;
	color: #bab4b4;
	font-weight: 400;
	width: 17rem
}

#event-form input[type=time] {
	font-size: 1.5rem;
	font-weight: 400;
	color: #bab4b4
}

#event-form label {
	margin: 7px 0;
	font-size: 3rem
}

#event-form ::placeholder {
	color: #BAB4B4;
	font-weight: 400
}

.button {
	border: 2px solid #52BDDF;
	box-sizing: border-box;
	border-radius: 10px;
	padding: 1.1rem 4.5rem 1.1rem 1.3rem;
	background-color: #FFF;
	margin: 2rem 0 5rem;
	cursor: pointer;
	color: #52BDDF;
	font-weight: 700;
	font-size: 3rem;
}

.button:hover {
	background-color: #52BDDF;
	color: #FFF
}
</style>


<!-- JAVASCRIPT -->
<script>
import moment from 'moment'
import axios from 'axios'

export default {
	name: 'CreateEvent',
	data () {
		return {
			event: {
				name: '',
				startDate: '',
				endDate: '',
				startTime: '',
				endTime: '',
				event_name: '',
				start_date: '',
				end_date: ''
			},
			calendar: {
				uuid: "",
				start: "",
				end: "",
			}
		}
	},
  methods: {
		created() {
			if (this.$isAuthenticated() !== true) this.$router.push('/')
    },
    schedit() {
      var vm = this;

      if (this.$isAuthenticated() == true) {
        this.event.event_name = this.event.name
        this.event.start_date = moment(this.event.startDate + ' ' + this.event.startTime).toISOString();
        this.event.end_date = moment(this.event.endDate + ' ' + this.event.endTime).toISOString();

        let data = JSON.stringify({
          event_name: this.event.event_name,
          start_date: this.event.start_date,
          end_date: this.event.end_date
        });

				axios.put("http://127.0.0.1:5000/create/cal", data, {
					headers: { "Content-Type": "application/json" }
				}).then(r => {
					vm.calendar.uuid = r.data.calendar.uuid
          vm.calendar.start = r.data.calendar.start_date
					vm.calendar.end = r.data.calendar.end_date
          vm.$router.push('/cal/' + vm.calendar.uuid)
        }).catch(e => console.log(e));
			}
		}
	}
}
</script>
