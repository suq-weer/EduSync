<script lang="ts" setup></script>

<template>
  <mdui-list-item class="main"
                  :description="OnceDeviceListElement_time"
                  :headline="OnceDeviceListElement_id">
    <mdui-avatar slot="icon" style="--mdui-shape-corner-extra-small: 0.3rem;">
      <img :src="OnceDeviceListElement_avatar" width="100" height="100" style="max-width: 100%;" alt="">
    </mdui-avatar>
    <div slot="end-icon">
      <mdui-button-icon title="编辑" icon="edit" @click="editDevice(OnceDeviceListElement_id)"></mdui-button-icon>
      <mdui-button-icon title="删除" icon="delete" @click="deleteDevice(OnceDeviceListElement_id)"></mdui-button-icon>
<!--      <mdui-button-icon icon="visibility"></mdui-button-icon>-->
    </div>
  </mdui-list-item>
</template>

<script lang="ts">
import router from '@/router'
import { alert } from 'mdui'
import { confirm } from 'mdui'
import { delete_device } from '@/api/server'
import { cookie_read_user } from '@/api/manage'

export default {
  methods: {
    editDevice(OnceDeviceListElement_id:string) {
      // console.log(OnceDeviceListElement_id)
      router.push({name: 'Device', params: { device_id: OnceDeviceListElement_id }})
    },
    async deleteDevice(OnceDeviceListElement_id : string) {
      await confirm({
        headline: "警告",
        description: "此操作会抹掉该设备的信息",
        confirmText: "删除",
        cancelText: "取消",
        onConfirm: async () => {

          try {
            const { uid, key } = cookie_read_user()
            const delete_device_result = await delete_device(uid, key, OnceDeviceListElement_id)
            if (delete_device_result){
              await alert({
                headline: "结果",
                description: delete_device_result['msg'],
                confirmText: "好的",
              })
            }
          }catch (error){
            console.error('Error deleting device:', error)
          }
        },
        onCancel: () => {
          console.log('取消')
        }

      });
    }
  },
  data(){
    return {
    }
  },
  props: {
    // 定义 props
    OnceDeviceListElement_time: {
      type: String, // 参数类型
      required: true, // 是否必传
      default: '快远控它把它炸了！！！' // 默认值
    },
    OnceDeviceListElement_id: {
      type: String,
      required: true,
      default: 'Xiaoyi 的笔记本'
    },
    OnceDeviceListElement_avatar: {
      type: String,
      required: true,
      default: '@/assets/logo.svg'
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

mdui-chip {
  margin-left: 0.25rem;
  margin-right: 0.25rem;
}

.main {
  animation: start var(--mdui-motion-duration-long4) var(--mdui-motion-easing-emphasized) 0.1s 1 normal;
  -moz-animation: start var(--mdui-motion-duration-long4) var(--mdui-motion-easing-emphasized) 0.1s 1 normal;
}
</style>
