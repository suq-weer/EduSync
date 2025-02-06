<script setup lang="ts">

</script>

<template>
  <div>
    <mdui-card class="card actions">
      <h2>Actions</h2>
      <mdui-chip v-for="command in CommandsList(getCommandList(device_system))" :key="command.command">{{command.name}}</mdui-chip>
    </mdui-card>
  </div>
</template>

<script  lang="ts">
import { CommandsList } from '@/config/CommandsList'

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
      default: '' // 设置默认值为空字符串
    }
  },
  setup() {
    const getCommandList = (system: string)=>{
      if (system.includes('Windows')) {
          return 'Windows'
        } else if (system.includes('Linux')) {
          return 'Linux'
        } else {
          return []
      }
    }

    return {
      getCommandList
    }
  }
}
</script>

<style scoped>
.card {
  width: 100%;
  background: rgba(var(--mdui-color-secondary-container));
  padding: 1rem;
  margin-bottom: 1rem;
}
.actions {
  mdui-chip {
    margin-left: 0.25rem;
    margin-right: 0.25rem;
    background: rgba(var(--mdui-color-secondary-container));
  }
}
</style>