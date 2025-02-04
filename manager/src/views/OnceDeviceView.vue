<template>
  <div class="main">
    <div class="status">
      <OnceDeviceStatus  :once-device-list-element_id="device_id"/>
    </div>
    <div class="actionsAndCommands">
      <div>
        <OnceDeviceActions  :once-device-list-element_id="device_id"/>
        <once-device-commands :once-device-list-element_id="device_id"/>
        <ai-chat/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import OnceDeviceStatus from '@/components/OnceDeviceStatus.vue'
import OnceDeviceActions from '@/components/OnceDeviceActions.vue'
import OnceDeviceCommands from '@/components/OnceDeviceCommands.vue'
import AiChat from '@/components/AiChat.vue'

export default defineComponent({
  components: { OnceDeviceStatus, OnceDeviceCommands, OnceDeviceActions, AiChat },
  setup() {
    const device_id = ref<string | null>(null)
    const route = useRoute()

    onMounted(() => {
      if (route.params.device_id) {
        device_id.value = route.params.device_id as string
      } else {
        console.error('device_id 参数缺失')
      }
    })

    return {
      device_id,
    }
  }
})
</script>


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
