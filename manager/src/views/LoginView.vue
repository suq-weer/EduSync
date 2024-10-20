<template>
  <mdui-card class="login">
    <h1>EduSync管理端 登录页面</h1>
    <mdui-text-field :value="uid" @input="uid = $event.target.value"  clearable label="账号"></mdui-text-field>
    <mdui-text-field :value="pass" @input="pass = $event.target.value"  type="password" toggle-password label="密码"></mdui-text-field>
    <mdui-button full-width @click="login">Login</mdui-button>
  </mdui-card>
</template>

<script setup>
import { ref } from 'vue'
import { Login } from '../api/server.ts'
import Cookies from 'js-cookie'

const uid = ref('')
const pass = ref('')

async function login() {
  //console.log(Cookies.get())
  await Login(uid.value, pass.value)
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
