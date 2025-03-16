<script setup lang="ts">
</script>

<template>
  <div class="poop">
    <mdui-avatar class="avatar" slot="icon">
      <img :src="avatar" alt="" style="height:100%;width: 100%;"/>
    </mdui-avatar>
    <mdui-card class="card" style="">
      <div class="contents" v-html="response" ></div>
    </mdui-card>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    response: {
      type: String,
      required: true,
      default: ''
    },
    avatar: {
      type: String,
      required: true,
      default: '@/assets/logo.svg'
    }
  }
}
</script>

<style scoped>
.poop {
  display: flex;
  flex-direction: row-reverse;
  align-items: flex-start;
  width: calc(100% - 1rem);
  vertical-align: top;
}

.card {
  padding: 1rem;
  margin: 1rem;
  background: rgba(var(--mdui-color-tertiary-container));
}
</style>
