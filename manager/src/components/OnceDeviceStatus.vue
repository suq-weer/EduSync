<script lang="ts" setup></script>

<template>
  <mdui-card class="main">
    <mdui-card class="part all">
      <div class="cpu_mem">
        <div>
          <!--注：py端CPU使用率是单核使用率，你可以相加除以核心数（JSON数组长度）-->
          <mdui-circular-progress max="100" :value="device_cpu_usage"></mdui-circular-progress>
          <p>CPU: {{device_cpu_usage}}%</p>
        </div>
        <div>
          <!--直接拿客户端数据填充（客户端传输来的数据以 iB 为单位）-->
          <mdui-circular-progress :max="device_memory_total" :value="device_memory_usage"></mdui-circular-progress>
          <p>Mem: {{device_memory_total/device_memory_total}}%</p>
        </div>
      </div>
      <div class="info">
        <b>Device ID: {{ device_id }}</b>
        <br>
        <b>SystemOS: {{ device_system }}</b>
        <br>
        <b>CpuName: {{ device_cpu_name }}</b>
        <br>
        <b>上次上线: {{ device_time }}</b>
        <!--剩下的放这里咯-->
      </div>
    </mdui-card>
    <mdui-card class="part">
      <h3>Disk Status</h3>
      <div class="disk_status">
        <div>
          <!--直接拿客户端数据填充（客户端传输来的数据以 B 为单位）-->
          <mdui-circular-progress max="53687091200" value="5368709120"></mdui-circular-progress>
          <p>/: 5G/50G (10%)</p>
        </div>
        <div>
          <mdui-circular-progress max="53687091200" value="5368709120"></mdui-circular-progress>
          <p>/home: 5G/50G (10%)</p>
        </div>
      </div>
    </mdui-card>
  </mdui-card>
</template>

<script lang="ts">
export default {
  props: {
    device_id: {
      type: String,
      required: true,
      default: ''
    },
    device_system: {
      type: String,
      required: true,
      default: ''
    },
    device_time: {
      type: String,
      required: true,
      default: ''
    },
    device_cpu_usage: {
      type: Number,
      required: true,
      default: 0
    },
    device_cpu_name: {
      type: String,
      required: true,
      default: ''
    },
    device_memory_usage: {
      type: Number,
      required: true,
      default: 0
    },
    device_memory_total: {
      type: Number,
      required: true,
      default: 0
    }
  }
}
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
  width: 20%;
  div {
    display: inline-block;
    width: 50%;
    padding: 0.5rem;
    p {
      text-align: center;
    }
    mdui-circular-progress {
      display: block;
      width: 100%;
      height: auto;
    }
  }
}

.disk_status {
  width: 100%;
  display: inline-flex;
  vertical-align: center;
  div {
    text-align: center;
    height: 5rem;
    margin: 0.5rem;
  }
}
</style>
