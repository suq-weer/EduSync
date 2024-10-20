<script setup lang="ts">
import { setColorScheme, setTheme } from 'mdui'
import { RouterView } from 'vue-router'
import NavigationView from './components/NavigationView.vue'

setColorScheme('#4A92CB')
setTheme('auto')
</script>

<template>
  <div id="app">
    <NavigationView />
    <mdui-layout>
      <RouterView />
    </mdui-layout>
  </div>
</template>
