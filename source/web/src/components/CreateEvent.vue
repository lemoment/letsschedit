<template>
<div class="container">
      <header class="page-header">
      </header>
      <div>
        <img src="../assets/clock.png" alt="Clock" id="logo">
        <h3 class="title">LET'S SCHED IT</h3>
      </div>
      <div style="clear: both;"></div>
      <div class="page-content" style="background-color:#f2f5f9; margin-left:20px; float:left; padding:20px">
        <p class="title" style="float:left;">Create an event named</p>
        <p id="box" style="float:left;"> Meeting </p>
        <p class="title" style="float:left;">on</p>
        <p id="box" style="float:left;"> 5/16/20 </p>
        <p class="title" style="float:left;">to</p>
        <p id="box" style="float:left;"> 5/16/20 </p>
        <p class="title" style="float:left;">from</p>
        <p id="box" style="float:left;"> 7:00am </p>
        <p class="title" style="float:left;">to</p>
        <p id="box" style="float:left;"> 7:00pm </p>
        <p class="title" style="float:left;">.</p>

     </div>
    </div>
</template>

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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

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
.logo {
    height: 5rem;
    padding-top: 20px;
    padding-left: 20px;
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
		font-family: 'Montserrat';
    font-style: normal;
		font-weight: bold;
		padding-left: 30px;
    color: #000000;
}
p {
  font-size: 2.5rem;
  text-align: center;
  margin-top:-40px;
  text-align: left;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: bold;
  padding-left: 10px;
  color: #000000;
}
.title {
    margin-top: 0px;
    margin-bottom: 0px;
}
.date {
    margin-top: 0px;
    margin-bottom: 0px;

}
.lead {
    margin-top: 20px;
    margin-bottom: 20px;
}
#box {
  text-align: center;
  border-radius: 15px;
  border: 2px solid #000000;
  padding: 10px;
  width: 12rem;
  height: 3rem;
  margin-top: -0.8rem;
  margin-left: 1rem;
  vertical-align: middle;
  color: #7c8087;
}
#logo {
  padding-left: 30px;
  float: left;
  padding-right: 10px;
}
</style>
