<template>
<div class="container">
      <header class="page-header">
      </header>
      <div>
         <h1 class="title" style="line-height:120px" >LET'S<br />SCHED<br />IT.</h1>
         <h2 class="title2" >Create Event</h2>
       <div class="page-content" style="margin-bottom: 10px">
           <form class="form-inline">
             <button v-on:click="login()" type="submit" >Login with Google</button>
              <br/>
              <button v-on:click="login()" type="submit" >Login with Outlook</button>
           </form>
           <div class="footer">
              <hr>
              <h3 style="margin-bottom: 10px; align-self: flex-left;">Built<br />with ❤️ <br />by Oliners</h1>
           </div>
       </div>
   </template>



<!-- CSS -->
<style>

html {
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
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
  background-color:#FFFFFF;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  padding: 20px;
  align-items: left;
}
h1 {
    font-size: 7rem;
		text-align: left;
		font-family: 'Montserrat', sans-serif;
    font-weight: 600;
		color: #000000;
		padding-left: 30px;
    padding-top: 20px;
}
h2 {
    font-size: 2rem;
    text-align: left;
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
    padding-left: 30px;
    color: #000000;
}
h3 {
    font-size: 1rem;
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
hr {
  margin-top: 4em;
  margin-left: 10px;
  margin-right: 650px;
  text-align: left;
  border-style: inset;
  border-width: 2px;
  color: #000000;
  display: flex;
  justify-content: flex-end;
}
.form-inline {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
 }

.form-inline label {
  margin: 0 0 0 0;
  font-size: 3rem;
  text-align: center;
  text-align: left;
  padding-left: 10px;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #000000;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
}

.form-inline button {
  border: 2px solid #000000;
  box-sizing: border-box;
  border-radius: 10px;
  background-color: #FFFFFF;
  cursor: pointer;
  margin-top: auto;
  margin-right: auto;
  margin-bottom: -10px;
  display: block;
  font-size: 2rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #000000;
  align-self: flex-end;
}
.form-inline button:hover {
  background-color: #C0C0C0;
  color: #FFFFFF;
}
.title {
    margin-top: 0px;
    margin-bottom: 0px;
}
.date {
    margin-top: 0px;
    margin-bottom: 0px;
}

</style>

<script>
export default {
  name: 'CreateLogin',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    login () {
      // Handle google login
      if (this.$isAuthenticated() !== true) {
        this.$login()
      }
    }
  }
}
</script>
