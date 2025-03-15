<template>
  <mdui-top-app-bar style="position: relative">
    <mdui-button-icon ref="button"><mdui-icon name="menu"></mdui-icon></mdui-button-icon>
    <mdui-top-app-bar-title><mdui-avatar><img src="../../assets/logo.svg" style="max-width: 100%;max-height: 100%" alt=""></mdui-avatar> EduSync 后台</mdui-top-app-bar-title>
    <div style="flex-grow: 1"></div>
  </mdui-top-app-bar>
  <mdui-navigation-drawer close-on-overlay-click close-on-esc ref="drawer">
    <div style="padding: 20px;">
      <mdui-avatar  style="margin-right: 0.5rem">
        <img src="../../assets/logo.svg" alt="" style="max-width: 100%;max-height: 100%">
      </mdui-avatar>
      <b style="font-size: 20px;text-align: center; vertical-align: middle;">EduSync 后台</b>
    </div>
    <mdui-list>
      <mdui-list-item v-for="item in items_list" :key="item.id" :headline="item.text" :icon="item.icon" :href="item.href"></mdui-list-item>
    </mdui-list>
  </mdui-navigation-drawer>
</template>

<script lang="ts">
import 'mdui/components/button-icon.js'
import 'mdui/components/icon.js'
import { ButtonIcon, NavigationDrawer } from 'mdui'

export default {
  data() {
    return {
      items_list: [
        {
          id:1,
          icon: 'home',
          text: '首页',
          href: '/'
        },
        {
          id:2,
          icon: 'devices',
          text: '设备列表',
          href: '/deviceList'
        },
        {
          id:3,
          icon: 'widgets',
          text: '指令列表',
          href: '/commandList'
        },
        {
          id:4,
          icon: 'android',
          text: 'AI',
          href: '/ai'
        }
      ]
    }
  },
  mounted() {
    const button: ButtonIcon = this.$refs.button as ButtonIcon;
    const drawer: NavigationDrawer = this.$refs.drawer as NavigationDrawer;

    if (button != null && drawer != null) {
      button.addEventListener('click', () => {
        drawer.open = !drawer.open
      });
    }
  }
}
</script>