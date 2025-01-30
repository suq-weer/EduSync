<script lang="ts" setup>
import OnceDeviceListElement from '@/components/OnceDeviceListElement.vue'
</script>

<template>
  <mdui-card class="card">
    <mdui-text-field clearable label="搜索..." placeholder="设备名或其他关键词"></mdui-text-field>
    <mdui-button-icon icon="search"></mdui-button-icon>
    <div class="actions">
      <mdui-chip icon="add">新增</mdui-chip>
      <mdui-chip icon="check">启用</mdui-chip>
      <mdui-chip icon="block">禁用</mdui-chip>
      <mdui-chip icon="close">删除</mdui-chip>
    </div>
    <mdui-list>
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
      <OnceDeviceListElement />
    </mdui-list>
    <div class="count">
      <mdui-chip icon="arrow_back">上一页</mdui-chip>
      <mdui-chip>1</mdui-chip>
      <mdui-chip>2</mdui-chip>
      <mdui-chip>3</mdui-chip>
      <mdui-chip>……</mdui-chip>
      <mdui-chip>10</mdui-chip>
      <mdui-chip icon="arrow_forward">下一页</mdui-chip>
    </div>
  </mdui-card>
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

.card {
  animation: start var(--mdui-motion-duration-long4) var(--mdui-motion-easing-emphasized) 0s 1 normal;
  -moz-animation: start var(--mdui-motion-duration-long4) var(--mdui-motion-easing-emphasized) 0s 1 normal;
  display: block;
  background: rgba(var(--mdui-color-secondary-container));
  width: 100%;
  padding: 1rem;

  * {
    display: block;
  }

  .actions {
    margin-top: 1rem;

    * {
      display: inline-block;
    }
  }

  .count {
    margin-top: 1rem;

    * {
      display: inline-block;
    }
  }

  mdui-chip {
    margin-left: 0.25rem;
    margin-right: 0.25rem;
    background: rgba(var(--mdui-color-secondary-container));
  }

  mdui-text-field {
    display: inline-block;
    vertical-align: middle;
    width: calc(90% - 0.5rem);
    margin-right: 0.5rem;
    height: 4rem;
  }

  mdui-button-icon {
    display: inline-block;
    vertical-align: middle;
    width: calc(10% - 0.5rem);
    margin-left: 0.5rem;
    height: 4rem;
  }
}
</style>
