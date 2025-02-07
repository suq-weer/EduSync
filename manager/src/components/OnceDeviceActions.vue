<script setup lang="ts">
import { defineProps, computed } from 'vue'
import { CommandsList } from '@/config/CommandsList'

// 定义 props
const props = defineProps({
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
})

// 计算命令列表
const commandList = computed(() => {
  const system = props.device_system || '' // 处理可能的 null 或 undefined
  if (system.includes('Windows')) {
    return CommandsList('Windows')
  } else if (system.includes('Linux')) {
    return CommandsList('Linux')
  } else {
    return []
  }
})
</script>

<template>
  <div>
    <mdui-card class="card actions">
      <h2>Actions</h2>
      <mdui-chip v-for="command in commandList" :key="command.command">{{
        command.name
      }}</mdui-chip>
    </mdui-card>
  </div>
</template>

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
