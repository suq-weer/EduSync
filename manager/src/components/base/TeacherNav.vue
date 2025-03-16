<script setup lang="ts">
import { cookie_read_user } from '@/api/manage'
import { get_list_device } from '@/api/server'
import { onMounted, onUnmounted, ref } from 'vue'
import type { ServerDeviceResponseDataItem } from '@/core/interface'
import { ButtonIcon, NavigationDrawer } from 'mdui'
import { useRouter } from 'vue-router'
import AiChat from '@/components/ai/AiChat.vue'
import AiView from '@/views/AiView.vue' // 添加路由导入

//ref
const device_list = ref<ServerDeviceResponseDataItem[]>([])
const scroll = ref<HTMLDivElement | null>(null)
const button = ref<ButtonIcon | null>(null);
const drawer = ref<NavigationDrawer | null>(null);

//status control
const loading = ref<boolean>(false)
const ai = ref<boolean>(false)
const router = useRouter() // 初始化路由实例

/**
 * 异步获取设备列表函数
 *
 * @param {number} page 当前页码
 * @param {number} length 每页的长度
 * @param {string} data 可选的筛选条件，默认为空字符串
 * @param {string} value 可选的筛选值，默认为空字符串
 */
async function fetchDeviceList(page: number, length: number, data: string="",value: string="") {
  loading.value = true
  try {
    // 从用户cookie中读取key和uid，用于身份验证
    const key = cookie_read_user()['key']
    const uid = cookie_read_user()['uid']

    // 调用后端API获取设备列表
    const result = await get_list_device(uid, key, (page-1).toString(), length.toString(),data,value)

    if (result['states'] !== 0) {
      device_list.value = result['data']? [...result['data']] : device_list.value
      console.log(device_list.value)
    }
  } catch (error) {
    // 捕获并记录获取设备列表时的错误
    console.error('Error fetching device list:', error)
  }
  loading.value = false
}

onMounted(() => {
  fetchDeviceList(1, 10)
  if (scroll.value) {
    scroll.value.addEventListener('scroll', () => {
      if (loading.value || (scroll.value?.scrollTop ?? 0) + (scroll.value?.clientHeight ?? 0) >= (scroll.value?.scrollHeight ?? 0) - 50) {
        fetchDeviceList(Math.floor(device_list.value.length / 10) + 1, 10)
      }
    })
  }
  if (button.value != null && drawer.value != null) {
    button.value.addEventListener('click', () => {
      if (drawer.value) {
        drawer.value.open = !drawer.value.open
      }
    });
  }
})
onUnmounted(() => {
  if (scroll.value) { // 移除事件监听器以避免内存泄漏
    scroll.value.removeEventListener('scroll', () => {})
  }
})

// 添加点击事件处理函数
const navigateToDevice = (deviceId: string) => {
  router.push(`/${deviceId}`)
}

</script>

<template>
  <mdui-top-app-bar style="position: relative">
    <mdui-button-icon ref="button"><mdui-icon name="menu"></mdui-icon></mdui-button-icon>
    <mdui-top-app-bar-title><mdui-avatar><img src="../../assets/logo.svg" style="max-width: 100%;max-height: 100%" alt=""></mdui-avatar> EduSync 教师后台</mdui-top-app-bar-title>
    <div style="flex-grow: 1"></div>
  </mdui-top-app-bar>
  <mdui-navigation-drawer close-on-overlay-click close-on-esc ref="drawer">
    <div style="padding: 20px;">
      <mdui-avatar  style="margin-right: 0.5rem">
        <img src="../../assets/logo.svg" alt="" style="max-width: 100%;max-height: 100%">
      </mdui-avatar>
      <b style="font-size: 20px;text-align: center; vertical-align: middle;">EduSync 教师后台</b>
    </div>
    <mdui-list ref="scroll" class="list">
      <mdui-list-item v-for="device in device_list" v-bind:key="device.device_id" icon="people" @click="navigateToDevice(device.device_id)">
        <b class="list-item-content">
          {{ device.notes ? (device.notes.length >= 25 ? device.notes.slice(0, 25) + '...' : device.notes) : (device.device_id.length >= 25 ? device.device_id.slice(0, 25) + '...' : device.device_id) }}
        </b>
      </mdui-list-item>
    </mdui-list>
  </mdui-navigation-drawer>
  <mdui-fab extended icon="chat" class="fab" v-if="!ai" @click="ai = !ai">AI聊天</mdui-fab>
  <mdui-fab extended icon="close" class="fab" v-if="ai" @click="ai = !ai">关闭</mdui-fab>
  <AiView class="fab_new" v-if="ai"></AiView>
</template>

<style scoped>
.list {
  max-width: 100%;
}
.list-item-content {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 1ch;
}
.fab {
  position: fixed;
  top: calc(100vh - 5rem);
  left: calc(100vw - 10rem);
}
.fab_new {
  position: fixed;
  width: 50rem;
  height: 30rem;
  top: calc(100vh - 36rem);
  left: calc(100vw - 52rem);
}
</style>