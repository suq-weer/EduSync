<script setup lang="ts">
import type { Dropdown } from 'mdui/components/dropdown.js';
</script>

<template>
  <div class="main">
    <mdui-card class="card">
      <h1>Command Panel</h1>
      <mdui-dropdown placement="bottom-start" ref="drop">
        <mdui-list-item slot="trigger">
          筛选设备
          <mdui-icon slot="end-icon" name="arrow_drop_down"></mdui-icon>
        </mdui-list-item>
        <mdui-menu>
          <mdui-menu-item>主机1</mdui-menu-item>
          <mdui-menu-item>主机1</mdui-menu-item>
        </mdui-menu>
      </mdui-dropdown>
      <mdui-card class="log">
        <div>
          <p>@id [00:00:00] (INFO) 已成功启动原神</p>
        </div>
      </mdui-card>
    </mdui-card>
    <mdui-card class="card">
      <div class="input">
        <mdui-dropdown placement="bottom-end" ref="drop">
          <mdui-list-item slot="trigger">
            全部设备
            <mdui-icon slot="end-icon" name="arrow_drop_down"></mdui-icon>
          </mdui-list-item>
          <mdui-menu>
            <mdui-menu-item>主机1</mdui-menu-item>
            <mdui-menu-item>主机1</mdui-menu-item>
          </mdui-menu>
        </mdui-dropdown>
        <mdui-text-field label="输入命令" placeholder="sudo rm -rf /*"></mdui-text-field>
        <mdui-button variant="filled">
          发送
        </mdui-button>
      </div>
    </mdui-card>
  </div>
</template>

<script lang="ts">
export default {
  mounted() {
    const dropdown = this.$refs.drop as Dropdown;
    dropdown.addEventListener('open', () => {
      // do something
    });
  }
};
</script>

<style scoped>
.main {
  width: 100%;
}
.card {
  background: rgba(var(--mdui-color-secondary-container));
  width: 100%;
  padding: 1rem;
  mdui-card {
    width: 100%;
    padding: 0.5rem;
  }
}
@media (max-width: 600px) {
  .input {
    text-align: right;
    mdui-text-field {
      margin-bottom: 1rem;
    }
  }
}
@media (min-width: 600px) {
  .input {
    vertical-align: bottom;
    display: inline-flex;
    width: 100%;
    mdui-list-item {
      width: calc(20% - 0.5rem);
      margin-right: 0.5rem;
    }
    mdui-text-field {
      width: 70%;
    }
    mdui-button {
      height: 3rem;
      width: calc(10% - 0.5rem);
      margin-left: 0.5rem;
      margin-top: 0.5rem;
      margin-bottom: 0.5rem;
    }
  }
}
</style>