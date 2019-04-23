<template>
  <div id="app">
    <CreateLogin/>
  </div>
</template>

<script>
import CreateLogin from './components/CreateLogin'

export default {
  name: 'App',
  components: {
    CreateLogin
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
