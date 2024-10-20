<template>
  <mdui-card class="login">
    <h1>login 登录页面</h1>
    <mdui-text-field clearable label="账号"></mdui-text-field>
    <mdui-text-field type="password" toggle-password label="密码"></mdui-text-field>
    <mdui-button full-width @click="login">Login</mdui-button>
  </mdui-card>
</template>

<script setup>
import { ref } from 'vue'
import '@mdui/icons/password.js'
import { postLogin } from '../api/server.ts'

const uid = ref('df')
const pass = ref('df')

async function login() {
  const result = await postLogin({ uid: uid.value, pass: pass.value })
  console.log(result)
}
</script>

<style scoped>
.login {
  display: block;
  padding: 1rem;
  margin: auto;

  h1 {
    text-align: center;
  }

  mdui-text-field {
    margin-bottom: 0.3rem;
  }
}
</style>
