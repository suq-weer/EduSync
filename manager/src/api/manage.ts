import Cookies from 'js-cookie'
import type { UnwrapRef } from 'vue'

//写入用户数据
export const cookie_write_user = async (body: { uid: UnwrapRef<string>, pass: UnwrapRef<string> ,key: UnwrapRef<string>}) => {
  Cookies.set('uid', body['uid'], { expires: 7, path: '/' ,SameSite: "Lax" })
  Cookies.set('pass', body['pass'], { expires: 7, path: '/' ,SameSite: "Lax" })
  Cookies.set('key', body['key'], { expires: 7, path: '/' ,SameSite: "Lax" })
  return 1
}

//读取用户数据
export const cookie_read_user = () => {
  return Cookies.get()
}