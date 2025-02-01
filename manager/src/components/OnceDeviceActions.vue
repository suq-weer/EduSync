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
  <mdui-card class="card commands">
    <h2>Commands</h2>
    <p>[11:45:14](INFO)已成功启动《原神》</p>
    <div>
    <mdui-text-field label="输入命令" placeholder="sudo rm -rf /*"></mdui-text-field>
    <mdui-button-icon icon="upload"></mdui-button-icon>
    </div>
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
.commands {
  mdui-text-field {
    width: 100%;
  }
  p {
    background: rgb(var(--mdui-color-surface-container-low));
    padding: 0.5rem;
    border-radius: var(--mdui-shape-corner-small);
  }
  div {
    display: inline-flex;
    width: 100%;
    mdui-button-icon {
      width: 4rem;
      height: 4rem;
    }
    mdui-text-field {
      width: calc(100% - 5rem);
      margin-right: 0.5rem;
    }
  }
}
</style>