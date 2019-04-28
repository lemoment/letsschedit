<template>
<div class="container">
      <header class="page-header">
      </header>
      <div>
        <img src="../assets/clock.png" alt="Clock" id="logo">
        <h3 class="title" style="margin-bottom: 30px">LET'S SCHED IT</h3>
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
    color: rgb(255, 255, 255);
}
html,
body {
  height: 100%;
  margin: 0;
  padding: 0;
}
.page-content{
  background-color:#e5e5e5; 
  margin-left:20px;
  margin-right: 20px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 20px;
  align-items: baseline;
}
h1 {
    font-size: 9rem;
		text-align: left;
		font-family: 'Montserrat', sans-serif;
    font-weight: 700;
		color: #000000;
		padding-left: 30px;
}
h2 {
    font-size: 5rem;
		text-align: left;
		font-family: 'Montserrat', sans-serif;
		font-weight: 700;
		padding-left: 30px;
    color: #000000;
}
h3 {
    font-size: 2rem;
		text-align: left;
		font-family: 'Montserrat', sans-serif;
		font-weight: bold;
		padding-left: 30px;
    color: #000000;
}
p {
  font-size: 3rem;
  text-align: center;
  text-align: left;
  padding-left: 10px;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #000000;
}

.form-inline {
  display: flex;
  flex-flow: row wrap;
 }
 .form {
   display: flex;
   flex-flow: column;
 }
.form-inline input {
  padding: 3px 0 3px 0;
  margin: 5px 10px 5px 10px;
  box-sizing: border-box;
  border: 2px solid black;
  border-radius: 10px;
  text-align: center;
  color: #545454;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  font-size: 2.5rem;
  width: 15rem;
  vertical-align: middle;
}
.form-inline label {
  margin: 0 0 0 0;
  font-size: 3rem;
  text-align: center;
  text-align: left;
  padding: 0 10 0 10;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #000000;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
}
.form-inline ::placeholder {
  color: #bab4b4;
  font-weight: normal;
}
.button {
  border: 2px solid #52BDDF;
  box-sizing: border-box;
  border-radius: 10px;
  background-color: #FFFFFF;
  cursor: pointer;
  font-size: 3rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #52BDDF;
  margin-top: 2rem;
}
.button:hover {
  background-color: #52BDDF;
  color: #FFFFFF;
}
.title {
    margin-top: 0px;
    margin-bottom: 0px;
}
#logo {
  padding-left: 30px;
  float: left;
  padding-right: 10px;
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
