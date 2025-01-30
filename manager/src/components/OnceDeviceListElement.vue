<script lang="ts" setup></script>

<template>
  <mdui-list-item class="main" description="快远控它把它炸了！！！" headline="Xiaoyi 的笔记本">
    <mdui-avatar slot="icon"></mdui-avatar>
    <div slot="end-icon">
      <mdui-button-icon icon="edit"></mdui-button-icon>
      <mdui-button-icon icon="visibility"></mdui-button-icon>
      <mdui-button-icon icon="close"></mdui-button-icon>
    </div>
  </mdui-list-item>
</template>

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
