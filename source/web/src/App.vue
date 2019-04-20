<template>
  <div id="app">
    <CreateEvent/>
  </div>
</template>

<script>
import CreateEvent from './components/CreateEvent'

export default {
  name: 'App',
  components: {
    CreateEvent
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
