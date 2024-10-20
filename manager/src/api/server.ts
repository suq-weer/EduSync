import instance from '../utils/request'
import type { UnwrapRef } from 'vue'
import { cookie_write_user } from './manage.ts'
import { alert } from 'mdui/functions/alert.js'

export const postLogin = async (body: { uid: UnwrapRef<string>, password: UnwrapRef<string> }) => {
  try {
    const response = await instance.post('/function/admin/login.php', body)
    return response.data
  } catch (err) {
    console.error(err)
    return err
  }
}

export const Login = async (uid: string, password: string) => {
  // console.log({ uid: uid.value, password: pass.value })
  if (uid&&password) {
    const result = await postLogin({ uid: uid, password: password })
    console.log(result)

    //判断结果
    if (result['states'] === 1) {

      await cookie_write_user({ uid: uid, pass: password })
      this.$router.replace('home')

    } else {

      alert({
        headline: document.title,
        description: result['data'],
        confirmText: "好",
        onConfirm: () => password = '',
      })

    }
  }
  else alert({ headline: document.title, description: "请输入完整!", confirmText: "好" })

}