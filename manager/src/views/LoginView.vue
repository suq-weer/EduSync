<template>
  <mdui-card class="login" >
    <h1>EduSync管理端 登录页面</h1>
    <mdui-text-field :value="uid" @input="uid = $event.target.value"  clearable label="账号"></mdui-text-field>
    <mdui-text-field :value="pass" @input="pass = $event.target.value"  type="password" toggle-password label="密码"></mdui-text-field>
    <mdui-button full-width @click="login">Log-in</mdui-button>
  </mdui-card>
</template>

<script>
import { ref } from 'vue'
import { Login } from '@/api/server.ts'
import Cookies from 'js-cookie'
import router from '@/router/index.ts'
import { alert } from 'mdui/functions/alert.js'
import { cookie_write_user } from '@/api/manage.ts'

export default {
  data() {
    return {
      uid: 'xiaoyi',
      pass: 'xiaoyi..',
    }
  },
  methods: {
    async login() {

      // console.log(Cookies.get())
      if (!(this.uid && this.pass)) {
        await alert({ headline: 'login', description: '请输入完整!', confirmText: '好' })
      } else {

        const result = await Login(this.uid, this.pass)
        // console.log(result)
        //判断结果
        if (result['states'] === 1) {
          console.log("登录成功")
          await cookie_write_user({ uid: this.uid, pass: this.pass, key: result['data'] })
          await router.replace({ name: 'home' })
        } else {

          await alert({
            headline: 'login',
            description: result['data'],
            confirmText: '好',
            onConfirm: () => {
              this.pass = ''
            }
          })
        }
      }//判断结果结束

    }
  }

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
