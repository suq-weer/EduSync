<script lang="ts" setup>
import OnceDeviceStatus from '@/components/OnceDeviceStatus.vue'
import OnceDeviceActions from '@/components/OnceDeviceActions.vue'
import OnceDeviceCommands from '@/components/OnceDeviceCommands.vue'
import AiChat from '@/components/AiChat.vue'
</script>

<template>
  <div class="main">
    <div class="status">
      <OnceDeviceStatus />
    </div>
    <div class="actionsAndCommands">
      <div>
        <OnceDeviceActions />
        <once-device-commands/>
        <ai-chat/>
      </div>
    </div>
  </div>
</template>

<style scoped>
@media screen and (max-width: 900px) {
  .status {
    display: flex;
    width: 100%;
    margin-right: 0;
    margin-bottom: 1rem;
  }

  .actionsAndCommands {
    display: flex;
    width: 100%;
    margin-left: 0;
  }
}

@media screen and (min-width: 900px) {
  .main {
  display: inherit;
}
  .status {
    display: inline-block;
    width: calc(30% - 0.5rem);
    margin-right: 0.5rem;
  }

  .actionsAndCommands {
    display: inline-block;
    width: calc(70% - 0.5rem);
    margin-left: 0.5rem;
  }
}
</style>
