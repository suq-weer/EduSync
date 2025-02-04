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
      <mdui-button-icon title="删除" icon="delete"></mdui-button-icon>
<!--      <mdui-button-icon icon="visibility"></mdui-button-icon>-->
    </div>
  </mdui-list-item>
</template>

<script lang="ts">
import router from '@/router'

export default {
  methods: {
    editDevice(OnceDeviceListElement_id:string) {
      // console.log(OnceDeviceListElement_id)
      router.push({name: 'Device', params: { device_id: OnceDeviceListElement_id }})
    },
    deleteDevice(OnceDeviceListElement_id) {
      console.log(OnceDeviceListElement_id)
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
