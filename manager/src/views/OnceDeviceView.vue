<template>
  <div class="main">
    <div class="status">
      <OnceDeviceStatus
        :device_id="device_id"
        :device_system="device_system"
        :device_time="device_time"
        :device_cpu_usage="device_cpu_usage"
        :device_cpu_name="device_cpu_name"
        :device_memory_usage="device_memory_usage"
        :device_memory_total="device_memory_total"
        :device_disk_status="device_disk_status"
      />
    </div>
    <div class="actionsAndCommands">
      <div>
        <OnceDeviceActions :device_id="device_id"  :device_system="device_system"/>
        <once-device-commands :device_id="device_id" />
        <AiView></AiView>
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
import AiView from '@/views/AiView.vue'
import { fetch_device_info } from '@/api/server'
import { cookie_read_user } from '@/api/manage'

export default defineComponent({
  components: { AiView, OnceDeviceStatus, OnceDeviceCommands, OnceDeviceActions },
  setup() {
    const device_id = ref<string | null>(null)

    const device_time = ref<string | null>(null)
    const device_system = ref<string | null>(null)
    const device_cpu_status = ref<object | null>(null)
    const device_cpu_name = ref<string | null>(null)
    const device_cpu_usage = ref<number | null>(null)
    const device_memory_status = ref<object | {}>({})
    const device_memory_total = ref<number | null>(null)
    const device_memory_usage = ref<number | null>(null)
    const device_disk_status = ref<string | null>(null)

    const route = useRoute()

    const fetchDeviceInfo = async (device_id: string) => {
      try {
        const response = await fetch_device_info(
          cookie_read_user()['uid'],
          cookie_read_user()['key'],
          device_id
        )
        if (response) {
          return response['data']
        }
      } catch (error) {
        console.error('Error deleting device:', error)
      }
    }

    onMounted(async () => {
      if (route.params.device_id) {
        device_id.value = route.params.device_id as string
      } else {
        console.error('device_id 参数缺失')
      }

      const fetchDeviceInfo_response = await fetchDeviceInfo(device_id.value)
      // const device_data = atob(fetchDeviceInfo_response['data']['data'])
      const device_data = JSON.parse(atob(fetchDeviceInfo_response['data']))
      console.log(device_data)

      device_cpu_status.value = device_data['CPUStatus']
      device_memory_status.value = device_data['MemoryStatus']
      device_cpu_name.value = device_cpu_status.value['name']

      device_time.value = new Date(fetchDeviceInfo_response['time'] * 1000).toLocaleString()
      device_system.value = device_data['SystemOutput']['system']
      // console.log(device_data['SystemOutput']['system'])
      device_cpu_usage.value = device_cpu_status.value['percent']
      device_memory_total.value = device_memory_status.value['total']
      device_memory_usage.value = device_memory_status.value['used']

      device_disk_status.value = device_data['DiskStatus']
    })

    return {
      device_id,
      device_cpu_status,
      device_memory_status,
      device_time,
      device_system,
      device_cpu_name,
      device_cpu_usage,
      device_memory_total,
      device_memory_usage,
      device_disk_status
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
