<template>
  <mdui-card class="main">
    <mdui-card class="part all">
      <div class="cpu_mem">
        <div>
          <!--注：py端CPU使用率是单核使用率，你可以相加除以核心数（JSON数组长度）-->
          <mdui-circular-progress max="100" :value="device_cpu_usage"></mdui-circular-progress>
          <p>CPU: {{ Math.ceil(device_cpu_usage) }}%</p>
        </div>
        <div>
          <!--直接拿客户端数据填充（客户端传输来的数据以 iB 为单位）-->
          <mdui-circular-progress
            :max="device_memory_total"
            :value="device_memory_usage"
          ></mdui-circular-progress>
          <p>Mem: {{ Math.ceil(device_memory_total / device_memory_total) }}%</p>
        </div>
      </div>
      <div class="info">
        <b>设备 ID: {{ device_id }}</b>
        <br />
        <b>操作系统: {{ device_system }}</b>
        <br />
        <b>处理器名称: {{ device_cpu_name }}</b>
        <br />
        <b>上次上线: {{ device_time }}</b>
        <!--剩下的放这里咯-->
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
  </mdui-card>
</template>

<script setup lang="ts">
interface DeviceStatus {
  device_id: string;
  device_system: string;
  device_time: string;
  device_cpu_usage: number;
  device_cpu_name: string;
  device_memory_usage: number;
  device_memory_total: number;
  device_disk_status: Array<{
    name: string;
    total: number;
    used: number;
    percent: number;
  }>;
}
defineProps<DeviceStatus>()
</script>

<style scoped>
.main {
  display: block;
  background: rgba(var(--mdui-color-secondary-container));
  padding: 1rem;
}

.part {
  width: 100%;
  padding: 1rem;
  margin-bottom: 1rem;
}

.all {
  div {
    display: inline-block;
    vertical-align: top;
    height: 100%;
  }
}

.cpu_mem {
  width: 100%;
  vertical-align: center;
  display: inline-flex;
  div {
    text-align: center;
    margin: 0.5rem;
  }
}

.disk_status {
  width: 100%;
  display: inline-flex;
  vertical-align: center;
  div {
    text-align: center;
    margin: 0.5rem;
  }
}
</style>
