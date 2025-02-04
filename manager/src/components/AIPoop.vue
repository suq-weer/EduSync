<script setup lang="ts">
defineProps<{
  response: string
}>()
</script>

<template>
  <div class="poop">
    <mdui-avatar class="avatar"></mdui-avatar>
    <mdui-card class="card">
      <div class="contents" v-html="response"></div>
    </mdui-card>
  </div>
</template>

<style scoped>
.poop {
  display: flex;
  align-items: flex-start;
  width: calc(100% - 1rem);
  margin-right: 20%;
  vertical-align: top;
}

.card {
  padding: 1rem;
  margin: 1rem;
  background: rgba(var(--mdui-color-secondary-container));
}
</style>
