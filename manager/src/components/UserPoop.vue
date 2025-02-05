<script setup lang="ts">
</script>

<template>
  <div class="poop">
    <mdui-card class="card" style="">
      <div class="contents" v-html="response" ></div>
    </mdui-card>
    <mdui-avatar class="avatar" slot="icon" style="">
      <img :src="avatar" alt="" style="max-height:100%;max-width: 100%;min-height: 100%;min-width: 100%"/>
    </mdui-avatar>
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
  align-items: flex-start;
  width: calc(100% - 1rem);
  vertical-align: top;
}

.card {
  padding: 1rem;
  margin: 1rem;
  background: rgba(var(--mdui-color-secondary-container));
}
</style>
