<template>
  <mdui-top-app-bar style="position: relative">
    <mdui-button-icon ref="button"><mdui-icon name="menu"></mdui-icon></mdui-button-icon>
    <mdui-top-app-bar-title>EduSync 后台</mdui-top-app-bar-title>
    <div style="flex-grow: 1"></div>
  </mdui-top-app-bar>
  <mdui-navigation-drawer close-on-overlay-click close-on-esc ref="drawer">
    <mdui-list>
      <mdui-list-item headline="首页" end-icon="arrow_right" href="#"></mdui-list-item>
    </mdui-list>
  </mdui-navigation-drawer>
</template>
<style></style>
<script lang="ts">
import 'mdui/components/button-icon.js'
import 'mdui/components/icon.js'
import { ButtonIcon, NavigationDrawer } from 'mdui'

export default {
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
