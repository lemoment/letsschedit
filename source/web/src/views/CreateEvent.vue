<template>
<div class="container">
      <header class="page-header">
      </header>
      <div>
        <img src="../assets/clock.png" alt="Clock" id="logo">
        <h3 class="title">LET'S SCHED IT</h3>
      </div>

      <div class="page-content">
        <form class="form"> 
          <div class="form-inline">
            <label for="name">Create an event named</label>
            <input type="text" id="name" name="name" placeholder="Name">
            <label for="startDate">between</label>
            <input type="text" id="startDate" name="startDate" placeholder="Start Date">
            <label for="startDate">and</label>
            <input type="text" id="endDate" name="endDate" placeholder="End Date">
            <label for="startTime">within</label>
            <input type="text" id="startTime" name="startTime" placeholder="Start Time">
            <label for="endTime">to</label>
            <input type="text" id="endTime" name="endTime" placeholder="End Time">
            <label>.</label>
          </div>
          <div class="jump">
            <button class="button" type="submit" style="display:block;">SCHED IT!</button>
          </div>
        </form>
     </div>
    </div>
</template>

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

<script>
export default {
  name: 'CreateEvent',
  data () {
  return {
    msg: 'Welcome to Your Vue.js App'
  }
  }
}
</script>
