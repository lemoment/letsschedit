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
import HelloWorld from './components/HelloWorld'
import Vue from 'vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
</style>
