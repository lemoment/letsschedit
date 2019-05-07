<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link to="create-event">create-event</router-link>
      <router-link to="cal">cal</router-link>
    </div>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'App',
}
</script>

<style>
html {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  background-color: #FFFFFF;
  color: #000000;
  text-align: left;
}
html, body {
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
</style>
