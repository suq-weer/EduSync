import instance from '@/utils/request'
import type { UnwrapRef } from 'vue'
import { postLogin } from '@/api/server'

export const postInfo = async (body: { uid: UnwrapRef<string>, key: UnwrapRef<string> }) => {
  try {
    const response = await instance.post('/api/server_cpu.php', body)
    return response.data
  } catch (err) {
    console.error(err)
    return err
  }
}
export const info_server = async (uid: string, key: string) => {

  // console.log({ uid: uid.value, password: pass.value })
  const result = await postInfo({ uid: uid, key: key})
  const data = result['data']
  // console.log(data)
  return data
}