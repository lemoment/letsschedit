<template>
<div class="container">
      <header class="page-header">
      </header>
      <div>
        <img src="../assets/clock.png" alt="Clock" id="logo">
        <h3 class="title">LET'S SCHED IT</h3>
      </div>

      <div class="page-content">
        <form class="form" @submit.prevent="schedit()"> 
          <div class="form-inline">
            <label for="name">Create an event named</label>
            <input type="text" id="name" name="name" v-model="event.name" placeholder="Name">

            <label for="startDate">between</label>
            <input onfocus="(this.type='date')" id="startDate" v-model="event.startDate" placeholder="Start Date">

            <label for="endDate">and</label>
            <input onfocus="(this.type='date')" id="endDate" name="endDate" v-model="event.endDate" placeholder="End Date">

            <label for="startTime">within</label>
            <input onfocus="(this.type='time')" id="startTime" name="startTime" v-model="event.startTime" placeholder="Start Time">

            <label for="endTime">to</label>
            <input onfocus="(this.type='time')" id="endTime" name="endTime" v-model="event.endTime" placeholder="End Time">

            <label>.</label>
          </div>
          <div class="jump">
            <button class="button" type="submit" style="display:block;">SCHED IT!</button>
          </div>
        </form>
     </div>
    </div>
</template>


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
      }
    }
  },
  methods: {
    schedit() {
      // if (this.$isAuthenticated() == true) {
      // {
      //   "message": {
      //     "event_name": "Missing required parameter in the JSON body",
      //     "start_date": "Missing required parameter in the JSON body",
      //     "end_date": "Missing required parameter in the JSON body"
      //   }
      // }
      if (this.$isAuthenticated() == true) {
        this.event.event_name = this.event.name
        
        this.event.start_date = moment(this.event.startDate + ' ' + this.event.startTime).toISOString();
        this.event.end_date = moment(this.event.endDate + ' ' + this.event.endTime).toISOString();
        // console.log(this.event.end_date)
        // console.log(this.event.startDate, this.event.startTime)   
        // console.log('You are already logged in,', this.$getUserData().firstName)
    
        let data = JSON.stringify({
          event_name: this.event.event_name,
          start_date: this.event.start_date,
          end_date: this.event.end_date
        })

        axios.put("http://127.0.0.1:5000/cal/new", data,
                  {headers: {"Content-Type": "application/json"}}) 
              .then(r => console.log(r.status))
              .catch(e => console.log(e));
        console.log("stuff happening!")
        this.$router.push('cal')
      }
    }
  }
}
</script>


<!-- CSS -->
<style scoped>
html {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  background-color: #FFFFFF;
  color: #00000;
  text-align: left;
}
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}
h1 {
  font-size: 9rem;
}
h2 {
  font-size: 5rem;
}
h3 {
  font-size: 2rem;
}
p {
  font-size: 3rem;
}
 .form {
  display: flex;
  flex-flow: column;
 }
.form-inline {
  flex-flow: row wrap;
  background-color:#e5e5e5;
  padding:20px;
 }
.form-inline input {
  padding: 3px 0 3px 0;
  margin: 7px 10px 7px 10px;
  box-sizing: border-box;
  border: 2px solid black;
  border-radius: 10px;
  /*background-color: #e5e5e5;*/
  background-color: #FFFFFF;
  text-align: center;
  color: #545454;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  font-size: 2.5rem;
  width: 15rem;
  vertical-align: middle;
}
.form-inline input[type=date]{
  font-size: 1.5rem;
}

.form-inline label {
  margin: 7px 0 7px 0;
  font-size: 3rem;
}
.form-inline ::placeholder {
  color: #bab4b4;
  font-weight: normal;
  /*color: #545454;
  font-weight: bold;*/
}
.button {
  border: 2px solid #52BDDF;
  box-sizing: border-box;
  border-radius: 10px;
  padding: 1.1rem 4.5rem 1.1rem 1.3rem;
  background-color: #FFFFFF;
  margin: 2rem 0 5rem 0;
  cursor: pointer;
  font-size: 3rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #52BDDF;
}
.button:hover {
  background-color: #52BDDF;
  color: #FFFFFF;
}
.jump{
  margin-top: 3rem
}
.title {
    margin: 0 0 0.7rem 0;
}
#logo {
  float: left;
  padding: 0 1rem 0 1rem
}
</style>