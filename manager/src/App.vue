<script setup lang="ts">
import { setColorScheme, setTheme } from 'mdui'
import { RouterView } from 'vue-router'
import NavigationView from '@/components/NavigationView.vue'

setColorScheme('#34495E')
setTheme('auto')


</script>

<template>
  <div id="app">
    <NavigationView />
    <mdui-layout class="app_layout">
      <RouterView></RouterView>
    </mdui-layout>
  </div>
</template>

<style>
.app_layout {
  padding: 1.5rem;
}
</style>
<!--<template>-->
<!--  <div id="app">-->
<!--      <RouterView></RouterView>-->
<!--  </div>-->
<!--</template>-->