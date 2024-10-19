<template>
  <div class="login">
  <h1>login 登录页面</h1>
    <div class="mdui-table">
      <table>
        <mdui-text-field :value="uid" @input="uid = $event.target.value" label="Uid"></mdui-text-field>
        <mdui-text-field :value="pass" type="password" toggle-password label="Password"></mdui-text-field>
      </table>
      <br>
      <mdui-button full-width @click="login">Login</mdui-button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import '@mdui/icons/password.js'
import { postLogin } from '@/api/server.ts'

const uid = ref('df')
const pass = ref('df')

async function login() {
  const result = await postLogin({uid: uid.value, pass: pass.value})
  console.log(result)
}
</script>

<style scoped>
</style>
