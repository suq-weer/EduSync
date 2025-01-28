<script lang="ts" setup></script>

<template>
  <mdui-card class="home_card">
    <mdui-collapse>
      <mdui-collapse-item>
        <mdui-list-item slot="header" end-icon="arrow_drop_down" class="home_collapse">服务器</mdui-list-item>
        <div class="home_item">
          <mdui-card class="home_card_server home_card_content">
            <b>服务器</b>
            <b>操作系统信息： {{info_server_system}} </b><br />
            <b>面板版本： {{info_server_version}} </b><br />
            <b>上次开机到现在经过的时间： {{ info_server_time }} </b><br />
            <b>CPU 核心数： {{info_server_cpuNum}} </b><br />
            <b>CPU 使用率 (百分比)： {{info_server_cpuRealUsed}}% </b>
            <mdui-linear-progress :value="info_server_cpuRealUsed" max="100" @input="info_server_cpuRealUsed = $event.target.value"></mdui-linear-progress>
            <b>物理内存容量 (MB)： {{info_server_memTotal}} </b><br />
            <b>已使用的物理内存 (MB)： {{info_server_memRealUsed}} </b><br />
            <b>可用的物理内存 (MB)： {{info_server_memFree}} </b><br />
            <b>缓存化的内存 (MB)： {{info_server_memCached}} </b><br />
            <b>系统缓冲 (MB) ：{{info_server_memBuffers}} </b><br />
          </mdui-card>
          <mdui-card class="home_card_software home_card_content">
            <b>EduSync： {{ info_software_name }} </b>
          </mdui-card>
        </div>
      </mdui-collapse-item>
    </mdui-collapse>
  </mdui-card>
</template>

<style scoped>
.home_card {
  display: block;
  background: rgba(var(--mdui-color-secondary-container));
  width: 100%;
  height: auto;
}
@media screen and (max-width: 500px){
  .home_item {
    display: inline-block;
  }
}
@media screen and (min-width: 501px){
  .home_item {
    display: flex;
  }
}
.home_collapse {
  padding: 1rem;
}
.home_card_content {
  padding: 1rem;
  width: calc(100% - 1rem);
  margin: 0.5rem;
}
</style>

<script>
import { info_server } from '@/api/info_server'
import { cookie_read_user } from '@/api/manage'

export default {
  data() {
    this.info_servers()
    return {
      info_server_system: '', //操作系统信息
      server_cpu_usage: 10
    }
  },
  methods: {
    info_server_version: String,
    info_server_cpuNum: String,
    info_server_time: String,
    info_server_cpuRealUsed: String,
    info_server_memTotal: String,
    info_server_memRealUsed: String,
    info_server_memFree: String,
    info_server_memCached: String,
    info_server_memBuffers: String,
    info_software_name: String,

    async info_servers() {
      const user = cookie_read_user()
      const uid = user['uid']
      const key = user['key']
      const result = await info_server(uid, key)
      this.info_server_system = result['system']
      this.info_server_version = result['version']
      this.info_server_cpuNum = result['cpuNum']
      this.info_server_time = result['time']
      this.info_server_cpuRealUsed = result['cpuRealUsed']
      this.info_server_memTotal = result['memTotal']
      this.info_server_memRealUsed = result['memRealUsed']
      this.info_server_memFree = result['memFree']
      this.info_server_memCached = result['memCached']
      this.info_server_memBuffers = result['memBuffers']
      this.info_server_memCached = result['memCached']
      this.info_server_memCached = result['memBuffers']
      console.log(result)
    }
  }
}
</script>
