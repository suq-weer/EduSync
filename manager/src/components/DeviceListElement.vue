<template>
  <mdui-card class="card">
    <mdui-text-field clearable label="搜索..." placeholder="搜索设备名"></mdui-text-field>
    <mdui-button-icon icon="search"></mdui-button-icon>
    <div class="actions">
      <mdui-chip icon="add">新增</mdui-chip>
      <mdui-chip icon="check">启用</mdui-chip>
      <mdui-chip icon="block">禁用</mdui-chip>
      <mdui-chip icon="close">删除</mdui-chip>
    </div>
    <mdui-list>
      <!--suppress JSVoidFunctionReturnValueUsed -->
      <div  v-for="item in device_list" :key="item.device_id" >
        <OnceDeviceListElement :OnceDeviceListElement_id="item.device_id"
                               :OnceDeviceListElement_time="formatTimestamp(item.time*1000)"
                               :OnceDeviceListElement_avatar="getDeviceSystemAvatar(item.data)"/>
      </div>
    </mdui-list>
    <div class="count">
      <mdui-chip icon="arrow_back" @click="backPage">上一页</mdui-chip>
      <mdui-chip>1</mdui-chip>
      <mdui-chip>2</mdui-chip>
      <mdui-chip>3</mdui-chip>
      <mdui-chip>……</mdui-chip>
      <mdui-chip>10</mdui-chip>
      <mdui-chip icon="arrow_forward" @click="nextPage">下一页</mdui-chip>
    </div>
  </mdui-card>
</template>

<script lang="ts">
import { get_list_device } from '@/api/server'
import { cookie_read_user } from '@/api/manage'
import OnceDeviceListElement from '@/components/OnceDeviceListElement.vue'
import { ref, onMounted } from 'vue'
import { pageController } from '@/api/pages'

const device_list = ref<{ device_id: string; time: number; data: string }[]>([])
const list_length = "2"


export default {
  data() : { data: { device_id: string , time: number , data : string} [] } {
    this.deviceList("3",list_length)
    this.start()
    return {
      device_list : [],
    }
  },
  components: {
    OnceDeviceListElement
  },
  methods:{
    start(){
      this.page_controller = new pageController(null)
      this.page_controller.value = new pageController(2, 2)
    },
    async nextPage(){
      const data = this.page_controller.nextPage()
      // console.log(data)
      await this.deviceList(data['current_page'],list_length)
    },
    async backPage(){
      await this.deviceList(page_controller.backPage()['current_page'],list_length)
    },
    async deviceList(page:string,length:string){
      const key = cookie_read_user()['key']
      const uid = cookie_read_user()['uid']

      const result = await get_list_device(uid, key, page, length)
      if (result['status'] === 0) {
        this.device_list = []
      }else {
        this.device_list =  JSON.parse(result['data'])
      }

      device_list.value = this.device_list

      this.page_controller.value = new pageController(1, device_list.value.length)
      // console.log(device_list.value.length)

    },formatTimestamp(timestamp: number) {
      const date = new Date(timestamp);
      const year = date.getFullYear()
      const month = String(date.getMonth() + 1).padStart(2, '0')
      const day = String(date.getDate()).padStart(2, '0')
      const hours = String(date.getHours()).padStart(2, '0')
      const minutes = String(date.getMinutes()).padStart(2, '0')
      const seconds = String(date.getSeconds()).padStart(2, '0')
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
    },getDeviceSystemAvatar(data: string){
      const obj_data = JSON.parse(atob(data))

      let system:string = obj_data['SystemOutput']['system']
      let local = './src/assets/logo/'
      const theme = window.matchMedia('(prefers-color-scheme: light)').matches;

      if (system.indexOf('Windows')!==-1){
        local = local+'Windows-'
        if (theme) local = local+"Light.svg"
        else local = local+'Dark.svg'
      }else if (system.indexOf('Linux')!==-1){
        local = local+'Linux-'
        if (theme) local = local+"Light.svg"
        else local = local+'Dark.svg'
      }else{
        local = local+'../../logo.svg'
      }
      return local
    }
  }
}


</script>

<style scoped>
@keyframes start {
  from {
    opacity:0;
    left: 1000px;
  }
  to {
    opacity:1;
    left: 0;
  }
}
@-moz-keyframes start {
  from {
    opacity:0;
    left: 1000px;
  }
  to {
    opacity:1;
    left: 0;
  }
}
@-webkit-keyframes start {
  from {
    opacity:0;
    left: 1000px;
  }
  to {
    opacity:1;
    left: 0;
  }
}

.card {
  animation: start var(--mdui-motion-duration-long4) var(--mdui-motion-easing-emphasized) 0s 1 normal;
  -moz-animation: start var(--mdui-motion-duration-long4) var(--mdui-motion-easing-emphasized) 0s 1 normal;
  display: block;
  background: rgba(var(--mdui-color-secondary-container));
  width: 100%;
  padding: 1rem;

  * {
    display: block;
  }

  .actions {
    margin-top: 1rem;

    * {
      display: inline-block;
    }
  }

  .count {
    margin-top: 1rem;

    * {
      display: inline-block;
    }
  }

  mdui-chip {
    margin-left: 0.25rem;
    margin-right: 0.25rem;
    background: rgba(var(--mdui-color-secondary-container));
  }

  mdui-text-field {
    display: inline-block;
    vertical-align: middle;
    width: calc(90% - 0.5rem);
    margin-right: 0.5rem;
    height: 4rem;
  }

  mdui-button-icon {
    display: inline-block;
    vertical-align: middle;
    width: calc(10% - 0.5rem);
    margin-left: 0.5rem;
    height: 4rem;
  }
}
</style>
