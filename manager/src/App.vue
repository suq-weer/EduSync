<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavigationView from './components/NavigationView.vue'
</script>

<template>
  <header>
    <NavigationView />
  </header>

  <RouterView />
</template>

<style scoped></style>
