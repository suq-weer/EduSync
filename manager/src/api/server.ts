import instance from '@/utils/request'
import type { UnwrapRef } from 'vue'

/*
* 人生就是这样一直重复下去的……
* 既然不封装对象那我可就要用 any 了。
*/
const post = async (body: {}, resource: string) => {
  try {
    const response = await instance.post(resource, body)
    return response.data
  } catch (err) {
    console.error(err)
    return err
  }
}

export const postLogin = async (body: { uid: UnwrapRef<string>, password: UnwrapRef<string> }) => {
  return await post(body, '/function/admin/login.php')
}
export const postKey = async (body: { uid: UnwrapRef<string>, key: UnwrapRef<string> }) => {
  return await post(body, '/api/if_key.php')
}
export const getDeviceList = async (body: { uid: UnwrapRef<string>, key: UnwrapRef<string>, page:UnwrapRef<string>, length:UnwrapRef<string>, data:UnwrapRef<string>, value:UnwrapRef<string>}) => {
  return await post(body, '/function/admin/get_list_device.php')
}
export const deleteDevice = async (body: { uid: UnwrapRef<string>, key: UnwrapRef<string>, deviceId:UnwrapRef<string>}) => {
  return await post(body, '/function/admin/delete_device.php')
}
export const fetchDeviceInfo = async (body: { uid: UnwrapRef<string>, key: UnwrapRef<string>, deviceId:UnwrapRef<string>}) => {
  return await post(body, '/function/admin/read_device.php')
}
export const sendCommands = async(body: { uid: UnwrapRef<string>, key: UnwrapRef<string>, data:UnwrapRef<[string]>}) => {
  return await post(body, '/function/admin/create_command.php')
}
async function readUser(body: { uid: string; key: string }) {
  return await post(body, '/function/admin/read_user.php')
}


export const Login = async (uid: string, password: string) => {
  // console.log({ uid: uid.value, password: pass.value })
    return await postLogin({ uid: uid, password: password})
}
export const is_valid_key = async (uid: string, key: string) => {
  return await postKey({ uid: uid, key: key })
}
export const get_list_device = async (uid: string, key: string, page:string, length:string, data:UnwrapRef<string>, value:UnwrapRef<string>) => {
  return await getDeviceList({ uid: uid, key: key, page:page, length:length, data:data, value:value })
}
export const delete_device = async (uid: string, key: string, deviceId:string) => {
  return await deleteDevice({ uid: uid, key: key, deviceId:deviceId })
}
export const fetch_device_info = async (uid: string, key: string, deviceId:string) => {
  return await fetchDeviceInfo({ uid: uid, key: key, deviceId:deviceId })
}
export const send_commands = async (uid: string, key: string, data:UnwrapRef<[string]>) => {
  return await sendCommands({ uid: uid, key: key, data:data })
}
export const read_user = async (uid: string, key: string) => {
  return await readUser({ uid: uid, key: key })
}