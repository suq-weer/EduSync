<script lang="ts" setup>
import ServerStatusElement from '@/components/ServerStatusElement.vue'
import DeviceListElement from '@/components/DeviceListElement.vue'
</script>

<template>
  <mdui-layout-main>
    <div class="server_status">
      <ServerStatusElement />
    </div>
    <div class="device_list">
      <DeviceListElement />
    </div>
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
