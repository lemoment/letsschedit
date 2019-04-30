<template>
<div class="container">
      <header class="page-header">
      </header>
      <div>
         <h1 class="title" style="line-height:120px" >LET'S<br />SCHED<br />IT.</h1>
         <h2 class="title2" >Create Event</h2>
       <div class="page-content" >
           <form class="form-inline">
             <button type="submit" >Login with Google</button>
              <br />
              <button type="submit" >Login with Outlook</button>
           </form>
           <br />
           <div class="footer">
              <h3 style="align-self: flex-start;" >Built<br />with ❤️ <br />by Oliners</h1>
           </div>
           <div class="w3-display-container">
             <img src="palmfronds.jpg" alt="Leaves">
             <div class="w3-display-topleft w3-container">Top Left</div>
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
  padding: 30px;
  align-items: left;
}
h1 {
    font-size: 7rem;
		text-align: left;
		font-family: 'Montserrat', sans-serif;
    font-weight: 600;
		color: #000000;
		padding-left: 30px;
    position: fixed;
}
h2 {
    font-size: 2rem;
    text-align: left;
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
    padding-left: 30px;
    color: #000000;
    position: fixed;
}
h3 {
    font-size: 1rem;
		text-align: left;
		font-family: 'Montserrat', sans-serif;
		font-weight: bold;
		padding-left: 30px;
    color: #000000;
    position: fixed;
}
.container {
  display: flex;

  flex-wrap: flex-end;
}

.form-inline {
  position: fixed;
  left: 35px;
  top: 480px;
 }

.form-inline button {
  border: 2px solid #000000;
  box-sizing: border-box;
  border-radius: 10px;
  background-color: #FFFFFF;
  cursor: pointer;
  display: block;
  font-size: 2rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #000000;
  position: sticky;

}
.form-inline button:hover {
  background-color: #C0C0C0;
  color: #FFFFFF;
}
.title {
    position: fixed;
    margin-top: auto;
    margin-bottom: auto;
}
.title2 {
    position: fixed;
    margin-top: auto;
    margin-bottom: auto;
    left: 7px;
    top: 420px;
}
.footer {
  width: 100%;
  height: 120px;
  border-radius: 3px;
  color: #ffffff;
  position: fixed;
  left: 10px;
  top:610px;
  margin-left: auto;
}
.w3-display-container {
  padding-right:0px;
  position: fixed;
  left: 900px;
  top: 0px;
}

</style>

<script>
export default {
  name: 'CreateLogin',
  data () {
	return {
	  msg: 'Welcome to Your Vue.js App'
	}
  }
}
</script>
