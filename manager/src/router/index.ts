import { createRouter, createWebHistory } from 'vue-router'

const HomeView = () => import('@/views/HomeView.vue')
const LoginView = () => import('@/views/LoginView.vue')
const DeviceListView = () => import('@/views/DeviceListView.vue')
const OnceDeviceView = () => import('@/views/OnceDeviceView.vue')
const AiView = () => import('@/views/AiView.vue')
const CommandView = () => import('@/views/CommandView.vue')
const TeacherDeviceListElement = () => import('@/components/onceDevice/TeacherOnceDeviceElement.vue')

import { is_valid_key } from '@/api/server'
import { cookie_read_user } from '@/api/manage'
import { accountStates } from '@/states'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        title: 'Index of Edu-sync Manager'
      },
      children: [
        {
          path: ':device_id',
          name: 'DeviceListElement',
          component: TeacherDeviceListElement,
          meta: {
            title: '设备详情'
          },
          props: true
        }
      ]
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView,
      meta: {
        title: '登录管理员账号'
      }
    },
    {
      path: '/deviceList',
      name: 'DeviceList',
      component: DeviceListView,
      meta: {
        title: '设备列表'
      }
    },
    {
      path: '/device/:device_id',
      name: 'Device',
      component: OnceDeviceView,
      meta: {
        title: '设备详情'
      }
    },
    {
      path: '/commandList',
      name: 'CommandList',
      component: CommandView,
      meta: {
        title: '指令列表'
      }
    },
    {
      path: '/ai',
      name: 'AI',
      component: AiView,
      meta: {
        title: 'AI'
      }
    }
  ]
})

 router.beforeEach(async (to, from, next) => {
  document.title = to.meta.title as string
  // console.log(cookie_read_user())

  if (to.name !== 'Login') {
    const key = cookie_read_user()['key']
    const uid = cookie_read_user()['uid']
    const pass = cookie_read_user()['pass']
    const power = cookie_read_user()['power']
    const account = accountStates()

    const _is_valid_key = await is_valid_key(uid,key)
    //不存在key
    if (key==undefined||uid==undefined||pass==undefined) {
      next({ name: 'Login' })
    }
    //key存在
    else if (_is_valid_key['states']===0) {
      next({ name: 'Login' })
    }
    //key有效
    else if (_is_valid_key['states']===1) {
      account.setPower(power)
      next()
    }
    // console.log(_is_valid_key['states'])
  } else {
    next()
  }
})

export default router
export const account: string = ''
