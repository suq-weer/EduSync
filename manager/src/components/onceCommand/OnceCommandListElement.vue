<script lang="ts" setup></script>

<template>
  <mdui-list-item class="main"
                  :description="OnceCommandListElement_time"
                  :headline="'@'+OnceCommandListElement_device_id+' (Id:'+OnceCommandListElement_id+') '+OnceCommandListElement_code+' '+getExecutionStatus(OnceCommandListElement_effective)">
<!--    @id [00:00:00] (INFO) 已成功启动原神-->
  </mdui-list-item>
</template>

<script lang="ts">
// import router from '@/router'
import { alert } from 'mdui'
import { confirm } from 'mdui'
import { delete_command } from '@/api/server'
import { cookie_read_user } from '@/api/manage'

export default {
  methods: {
    // editDevice(OnceCommandListElement_id:string) {
    //   // console.log(OnceCommandListElement_id)
    //   router.push({name: 'Device', params: { device_id: OnceCommandListElement_id }})
    // },
    async deleteCommand(OnceCommandListElement_id : string) {
      await confirm({
        headline: "警告",
        description: "此操作会抹掉该指令的信息",
        confirmText: "删除",
        cancelText: "取消",
        onConfirm: async () => {

          try {
            const { uid, key } = cookie_read_user()
            const delete_device_result = await delete_command(uid, key, OnceCommandListElement_id)
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
    },getExecutionStatus(OnceCommandListElement_effective: string) {
      const EXECUTED = '(已执行)';
      const NOT_EXECUTED = '(未执行)';

      if (OnceCommandListElement_effective === '0') {
        return NOT_EXECUTED;
      } else {
        return EXECUTED;
      }
    }
  },
  data(){
    return {
    }
  },
  props: {
    // 定义 props
    OnceCommandListElement_time: {
      type: String, // 参数类型
      required: true, // 是否必传
      default: '2025-03-02 12:16:50' // 默认值
    },
    OnceCommandListElement_id: {
      type: String,
      required: true,
      default: '@id [00:00:00] (INFO) 已成功启动原神'
    },OnceCommandListElement_device_id: {
      type: String,
      required: true,
      default: 'Xiaoyi 的笔记本'
    },OnceCommandListElement_code: {
      type: String,
      required: true,
      default: ''
    },OnceCommandListElement_effective: {
      type: String,
      required: true,
      default: ''
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
