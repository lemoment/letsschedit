<template>
<div class="container">
      <header class="page-header">
      </header>
      <div class="page-content">
        <h1 class="title">WHEN2MEET</h1>
        <h2 class="title">IS CHANGING</h2>
     </div>
    </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
	return {
	  msg: 'Welcome to Your Vue.js App'
	}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@keyframes colorchange
    {
        0%   {background: #009bdf;}
        25%  {background: #00aa69;}
        50%  {background: #cf128c;}
        75% {background: #ffd400;}
        90%   {background: #999999;}
        100%   {background: #009bdf;}
    }

@-webkit-keyframes colorchange
    {
        0%   {background: #009bdf;}
        25%  {background: #00aa69;}
        50%  {background: #cf128c;}
        75% {background: #ffd400;}
        90%   {background: #999999;}
        100%   {background: #009bdf;}
    }

html {
    animation: colorchange 20s infinite;
    -webkit-animation: colorchange 20s infinite;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    /* background-color: #3D3D3D; */
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
    font-size: 20rem;
		text-align: left;  
		font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    /* background-color: #3D3D3D; */
		color: rgb(255, 255, 255); 
		padding-left: 20px;
}
h2 {
    font-size: 15rem;
		text-align: left;   
		font-family: 'Montserrat', sans-serif;
		font-weight: 700;
		padding-left: 20px;
    /* background-color: #3D3D3D; */
    color: rgb(255, 255, 255);
}

p {
  text-align: center;
  margin-top:-40px;
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
</style>
