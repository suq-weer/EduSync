<script lang="ts" setup>
import ServerStatusElement from '@/components/base/ServerStatusElement.vue'
import DeviceListElement from '@/components/base/DeviceListElement.vue'
import { accountStates } from '@/states'
import { ref } from 'vue'

const account = accountStates()
const power = ref('')

power.value = account.power
</script>

<template>
  <mdui-layout-main v-if="power === 'admin'">
    <div class="server_status">
      <ServerStatusElement />
    </div>
    <div class="device_list">
      <DeviceListElement />
    </div>
  </mdui-layout-main>
  <mdui-layout-main v-else>
    <mdui-tooltip variant="rich" content="点击左上角菜单按钮呼出侧边栏">
      <p style="text-align: center;font-size: smaller">请点击侧边栏任意设备进行控制</p>
    </mdui-tooltip>
    <RouterView />
  </mdui-layout-main>
</template>

<style scoped>
@media screen and (max-width: 700px) {
  .server_status {
    display: flex;
    width: 100%;
    margin-right: 0;
  }

  .device_list {
    display: flex;
    width: 100%;
    margin-left: 0;
  }
}

@media screen and (min-width: 700px) {
  .server_status {
    display: inline-flex;
    width: calc(30% - 0.5rem);
    margin-right: 0.5rem;
  }

  .device_list {
    display: inline-flex;
    width: calc(70% - 0.5rem);
    margin-left: 0.5rem;
  }
}
</style>
