<template>
  <mdui-top-app-bar style="position: relative">
    <mdui-button-icon ref="button"><mdui-icon name="menu"></mdui-icon></mdui-button-icon>
    <mdui-top-app-bar-title>EduSync 后台</mdui-top-app-bar-title>
    <div style="flex-grow: 1"></div>
  </mdui-top-app-bar>
  <mdui-navigation-drawer close-on-overlay-click close-on-esc ref="drawer">
    <div style="padding: 20px;">
      <mdui-avatar  style="margin-right: 20px">
        <img src="@/assets/logo.svg" alt="Project Logo" style="max-width: 100%;max-height: 100%">
      </mdui-avatar>
      <b style="font-size: 20px;text-align: center; vertical-align: middle;">EduSync 后台</b>
    </div>
    <mdui-list>
      <mdui-list-item headline="首页" icon="home" href="/"></mdui-list-item>
      <mdui-list-item headline="设备列表" icon="devices" href="/deviceList"></mdui-list-item>
      <mdui-list-item headline="单设备" icon="home" href="/device"></mdui-list-item>
    </mdui-list>
  </mdui-navigation-drawer>
</template>
<style></style>
<script lang="ts">
import 'mdui/components/button-icon.js'
import 'mdui/components/icon.js'
import { ButtonIcon, NavigationDrawer } from 'mdui'

export default {
  data() {
    return {
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
