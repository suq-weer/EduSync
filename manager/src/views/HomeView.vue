<script setup lang="ts">
</script>

<template>
  <main>
    <mdui-card class="home_card_server" variant="elevated" style="width: auto;height: auto">
      <mdui-list>
        <mdui-collapse accordion value="item-1">
          <mdui-collapse-item value="item-1">
            <mdui-list-item slot="header">
              <h3>服务器</h3>
              <mdui-icon slot="end-icon" class="example-trigger" name="keyboard_arrow_down"></mdui-icon>
            </mdui-list-item>
            <div class="home_card_div_1">
              <mdui-card variant="filled" style="width: 400px;height: 350px;padding: 1rem;margin-right: 0.5rem">
                <b>服务器</b>
                <div class="home_card_div_2">
                  <b>操作系统信息：
                    {{info_server_system}}
                  </b><br>
                  <b>面板版本：
                    {{info_server_version}}
                  </b><br>
                  <b>上次开机到现在经过的时间：
                    {{info_server_time}}
                  </b><br>
                  <b>CPU 核心数：
                    {{info_server_cpuNum}}
                  </b><br>
                  <b>CPU 使用率 (百分比)：
                    {{info_server_cpuRealUsed}}%
                  </b>
                  <mdui-linear-progress :value="info_server_cpuRealUsed" @input="info_server_cpuRealUsed = $event.target.value" max="100"></mdui-linear-progress>
                  <b>物理内存容量 (MB)：
                    {{info_server_memTotal}}
                  </b><br>
                  <b>已使用的物理内存 (MB)：
                    {{info_server_memRealUsed}}
                  </b><br>
                  <b>可用的物理内存 (MB)：
                    {{info_server_memFree}}
                  </b><br>
                  <b>缓存化的内存 (MB)：
                    {{info_server_memCached}}
                  </b><br>
                  <b>系统缓冲 (MB)
                    {{info_server_memBuffers}}
                  </b><br>
                </div>
              </mdui-card>
              <mdui-card variant="filled" style="width: 400px;height: 350px;padding: 1rem;margin-left: 0.5rem">
                <b>软件</b>
                <div class="home_card_div_2">
                  <b>EduSync：
                    {{info_software_name}}
                  </b><br>
                </div>
              </mdui-card>
            </div>
          </mdui-collapse-item>
        </mdui-collapse>
      </mdui-list>
    </mdui-card>
  </main>
</template>

<style>
.home_card_server{
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  padding-bottom: 1.5rem;
  margin: auto;
}

.home_card_div_1{
  margin-top: 1rem;
}

.home_card_div_2{
  margin-top: 0.5rem;
}
</style>

<script>
import { info_server } from '@/api/info_server.ts'
import {cookie_read_user} from '@/api/manage.ts'

export default {
  data(){
    this.info_servers()
    return {
      info_server_system:"",//操作系统信息
      server_cpu_usage:10,
    }
  },
  methods: {
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