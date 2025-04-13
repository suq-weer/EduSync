<template>
  <mdui-top-app-bar style="position: relative">
    <mdui-button-icon ref="button"><mdui-icon name="menu"></mdui-icon></mdui-button-icon>
    <mdui-top-app-bar-title
      ><mdui-avatar
        ><img src="../../assets/logo.svg" style="max-width: 100%; max-height: 100%" alt=""
      /></mdui-avatar>
      EduSync 后台</mdui-top-app-bar-title
    >
    <div style="flex-grow: 1"></div>
    <mdui-dropdown>
      <mdui-button slot="trigger">open dropdown</mdui-button>
      <mdui-menu>
        <mdui-menu-item>个人信息</mdui-menu-item>
        <mdui-menu-item @click="quitLogin">退出登录</mdui-menu-item>
      </mdui-menu>
    </mdui-dropdown>
  </mdui-top-app-bar>
  <mdui-navigation-drawer close-on-overlay-click close-on-esc ref="drawer">
    <div style="padding: 20px">
      <mdui-avatar style="margin-right: 0.5rem">
        <img src="../../assets/logo.svg" alt="" style="max-width: 100%; max-height: 100%" />
      </mdui-avatar>
      <b style="font-size: 20px; text-align: center; vertical-align: middle">EduSync 后台</b>
    </div>
    <mdui-list>
      <mdui-list-item
        v-for="item in itemsList"
        :key="item.id"
        :headline="item.text"
        :icon="item.icon"
        :href="item.href"
      ></mdui-list-item>
    </mdui-list>
  </mdui-navigation-drawer>
</template>

<script lang="ts" setup>
import 'mdui/components/button-icon.js'
import 'mdui/components/icon.js'
import { ButtonIcon, NavigationDrawer } from 'mdui'
import { useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'

// 使用 ref 定义响应式数据
const itemsList = ref([
  {
    id: 1,
    icon: 'home',
    text: '首页',
    href: '/'
  },
  {
    id: 2,
    icon: 'devices',
    text: '设备列表',
    href: '/deviceList'
  },
  {
    id: 3,
    icon: 'widgets',
    text: '指令列表',
    href: '/commandList'
  },
  {
    id: 4,
    icon: 'android', // 原始代码中的拼写错误已修正为 'android'
    text: 'AI',
    href: '/ai'
  }
])

const router = useRouter() // 初始化路由实例
const quitLogin = () => {
  // 清除cookie
  document.cookie = 'key=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'
  document.cookie = 'uid=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'
  document.cookie = 'pass=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'
  document.cookie = 'power=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'
  // 跳转到登录页面
  router.push('/login')
}

onMounted(() => {
  const button = (document.querySelector('mdui-button-icon') as unknown) as ButtonIcon
  const drawer = (document.querySelector('mdui-navigation-drawer') as unknown) as NavigationDrawer

  if (button && drawer) {
    button.addEventListener('click', () => {
      drawer.open = !drawer.open
    })
  }
})
</script>
