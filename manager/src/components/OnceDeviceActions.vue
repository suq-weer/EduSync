<script setup lang="ts">

</script>

<template>
  <div>
    <mdui-card class="card actions">
      <h2>Actions</h2>
      <mdui-chip>一键自爆</mdui-chip>
      <mdui-chip>为所有设备报告“我是个傻逼”</mdui-chip>
      <mdui-chip>远程启动《原神》</mdui-chip>
      <mdui-chip>回来吧《刺激战场》～</mdui-chip>
    </mdui-card>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    OnceDeviceListElement_id: {
      type: String,
      required: true,
      default: ''
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