<script setup lang="ts">
import { computed, onMounted, ref ,watch } from 'vue'
import { CommandsList } from '@/config/CommandsList'
import { fetch_device_info, send_commands } from '@/api/server'
import { cookie_read_user } from '@/api/manage'
import { alert } from 'mdui'

const device_notes = ref<string | null>(null)
const device_time = ref<string | null>(null)
const device_system = ref<string | null>(null)
const device_cpu_status = ref<object | null>(null)
const device_cpu_name = ref<string | null>(null)
const device_cpu_usage = ref<number | null>(null)
const device_memory_status = ref<object | {}>({})
const device_memory_total = ref<number | null>(null)
const device_memory_usage = ref<number | null>(null)
const device_disk_status = ref<string | null>(null)

// 定义 props
const props = defineProps({
  device_id: {
    type: String,
    required: true,
    default: ''
  }
})

// 使用响应式变量存储 device_id 的值
const deviceId = ref<string | null>(props.device_id || null)

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
    console.error('Error fetching device info:', error)
  }
}

onMounted(async () => {
  if (!deviceId.value) {
    console.error('device_id 参数缺失')
    return
  }

  const fetchDeviceInfo_response = await fetchDeviceInfo(deviceId.value)
  if (!fetchDeviceInfo_response) {
    console.error('未能获取设备信息')
    return
  }

  // 解析设备数据
  const device_data = JSON.parse(atob(fetchDeviceInfo_response['data']))
  device_notes.value = fetchDeviceInfo_response['notes']

  device_cpu_status.value = device_data['CPUStatus']
  device_memory_status.value = device_data['MemoryStatus']
  device_cpu_name.value = device_cpu_status.value?.['name']

  device_time.value = new Date(fetchDeviceInfo_response['time'] * 1000).toLocaleString()
  device_system.value = device_data['SystemOutput']?.['system']
  device_cpu_usage.value = device_cpu_status.value?.['percent']
  device_memory_total.value = device_memory_status.value?.['total']
  device_memory_usage.value = device_memory_status.value?.['used']

  device_disk_status.value = device_data['DiskStatus']
})

const commandList = computed(() => {
  const system = device_system.value || '' // 处理可能的 null 或 undefined
  if (system.includes('Windows')) {
    return CommandsList('Windows')
  } else if (system.includes('Linux')) {
    return CommandsList('Linux')
  } else {
    return []
  }
})

function if_deviceStatus(time:number) {
  // console.log(Date.now() - Math.floor(new Date(time)))
  return Date.now() - Math.floor(new Date(time)) < 180000;
}


watch(() => props.device_id,
  async (newDeviceId) => {
    if (!newDeviceId) {
      console.error('device_id 参数缺失')
      return
    }

    deviceId.value = newDeviceId
    const fetchDeviceInfo_response = await fetchDeviceInfo(newDeviceId)
    if (!fetchDeviceInfo_response) {
      console.error('未能获取设备信息')
      return
    }

    // 解析设备数据
    const device_data = JSON.parse(atob(fetchDeviceInfo_response['data']))
    device_notes.value = fetchDeviceInfo_response['notes']

    device_cpu_status.value = device_data['CPUStatus']
    device_memory_status.value = device_data['MemoryStatus']
    device_cpu_name.value = device_cpu_status.value?.['name']

    device_time.value = new Date(fetchDeviceInfo_response['time'] * 1000).toLocaleString()
    device_system.value = device_data['SystemOutput']?.['system']
    device_cpu_usage.value = device_cpu_status.value?.['percent']
    device_memory_total.value = device_data['MemoryStatus']?.['total']
    device_memory_usage.value = device_data['MemoryStatus']?.['used']

    device_disk_status.value = device_data['DiskStatus']
  }
)

const sendCommands = async (command: string) => {
  const list = [
    {
      "type":1,
      "code": command,
      "deviceId": props.device_id,
    }
  ]
  const result = await send_commands(cookie_read_user()['uid'], cookie_read_user()['key'], list)
  if (result){
    await alert({
      headline: "结果",
      description: result['data'],
      confirmText: "好的",
    })
  }
}
</script>


<template>
  <mdui-card class="card">
    <h1>快捷操作</h1>
    <mdui-tooltip
      variant="rich"
      headline="该设备的设备 ID"
      content="可将该 ID 交给学校管理员深度控制该设备。"
    >
      <p>对 {{props.device_id}}：</p>
    </mdui-tooltip>
    <div>
      <mdui-tooltip v-for="command in commandList" v-bind:key="command.command" variant="rich" @click="sendCommands(command.command)">
        <mdui-button style="margin: 0.25rem;" :icon="command.icon">{{command.name}}</mdui-button>
        <h3 slot="headline">{{command.name}}</h3>
        <div slot="content">
          {{command.description}}
        </div>
      </mdui-tooltip>
    </div>
  </mdui-card>
  <div style="display: inline">
    <mdui-card class="card line left">
      <h2>在线状态</h2>
      <mdui-tooltip
        variant="rich"
        content="该设备正在运行中且监管服务正常。"
        v-if=if_deviceStatus(device_time)
      >
        <p style="color: rgba(var(--mdui-color-primary))">当前在线</p>
      </mdui-tooltip>
      <mdui-tooltip
        variant="rich"
        content="该设备未运行或无法连接到该设备。"
        v-else
      >
        <p style="color: rgba(var(--mdui-color-error))">已离线</p>
      </mdui-tooltip>
      <mdui-tooltip
        variant="rich"
        content="该设备上次与服务器互动的时间。"
      >
        <p>上次在线：{{ device_time || '未知' }}</p>
      </mdui-tooltip>
    </mdui-card>
    <mdui-card class="card line right">
      <h2>设备信息</h2>
      <mdui-tooltip
        variant="rich"
        content="设备的名称，请在对应设备修改。"
      >
        <p>备注名：{{device_notes}}</p>
      </mdui-tooltip>
      <mdui-tooltip
        variant="rich"
        content="如果该设备占用率长时间过高，设备可能无法正常连接，请检查该设备。"
      >
        <p>CPU占用率：{{ Math.ceil(device_cpu_usage) }}% 内存占用率：{{ Math.ceil(device_memory_total / device_memory_total) }}% </p>
      </mdui-tooltip>
      <div class="cpu_mem">
        <div>
          <!--注：py端CPU使用率是单核使用率，你可以相加除以核心数（JSON数组长度）-->
          <mdui-circular-progress max="100" :value="device_cpu_usage"></mdui-circular-progress>
          <p>CPU: {{ Math.ceil(device_cpu_usage) }}%</p>
        </div>
        <div>
          <!--直接拿客户端数据填充（客户端传输来的数据以 iB 为单位）-->
          <mdui-circular-progress
            :max="100"
            :value="Math.ceil(device_memory_total / device_memory_total)"
          ></mdui-circular-progress>
          <p>Mem: {{ Math.ceil(device_memory_total / device_memory_total) }}%</p>
        </div>
      </div>
    </mdui-card>
    <mdui-card class="part">
      <h3>磁盘状态</h3>
      <div class="disk_status">
        <div v-for="disk_status in device_disk_status" :key="disk_status.name">
          <!--直接拿客户端数据填充（客户端传输来的数据以 B 为单位）-->
          <mdui-circular-progress
            :max="disk_status.total"
            :value="disk_status.used"
          ></mdui-circular-progress>
          <p>{{disk_status.name}}: {{Math.ceil(disk_status.used/Math.pow(1024, 3))}}G/{{Math.ceil(disk_status.total/Math.pow(1024, 3))}}G {{ Math.ceil(disk_status.percent) }}%</p>
        </div>
      </div>
    </mdui-card>
  </div>
</template>

<style scoped>
.card {
  background-color: rgba(var(--mdui-color-secondary-container));
  padding: 1rem;
  width: 100%;
}
.line {
  width: calc(50% - 0.125rem);
  display: inline-grid;
}
.left {
  margin-right: 0.125rem;
}
.right {
  margin-left: 0.125rem;
}
</style>