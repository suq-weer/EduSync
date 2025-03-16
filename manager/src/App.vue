<script setup lang="ts">
import { setColorScheme, setTheme } from 'mdui'
import { RouterView } from 'vue-router'
import AdminNav from '@/components/base/AdminNav.vue'
import { accountStates } from '@/states'
import TeacherNav from '@/components/base/TeacherNav.vue'

setColorScheme('#34495E')
setTheme('auto')

const account = accountStates()
</script>

<template>
  <div id="app">
    <AdminNav v-if="account.power === 'admin'" />
    <TeacherNav v-if="account.power === 'teacher'" />
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