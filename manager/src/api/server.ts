import instance from '../utils/request'

export const postLogin = async (body) => {
  try {
    const response = await instance.post('/function/admin/login.php', body)
    return response.data
  } catch(err) {
    console.error(err)
    return err
  }
}
