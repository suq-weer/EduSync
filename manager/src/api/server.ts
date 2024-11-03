import instance from '@/utils/request'
import type { UnwrapRef } from 'vue'

export const postLogin = async (body: { uid: UnwrapRef<string>, password: UnwrapRef<string> }) => {
  try {
    const response = await instance.post('/function/admin/login.php', body)
    return response.data
  } catch (err) {
    console.error(err)
    return err
  }
}
export const postKey = async (body: { uid: UnwrapRef<string>, key: UnwrapRef<string> }) => {
  try {
    const response = await instance.post('/api/if_key.php', body)
    return response.data
  } catch (err) {
    console.error(err)
    return err
  }
}

export const Login = async (uid: string, password: string) => {

  // console.log({ uid: uid.value, password: pass.value })
    return await postLogin({ uid: uid, password: password})

}

export const is_valid_key = async (uid: string, key: string) => {
  return await postKey({ uid: uid, key: key })
}