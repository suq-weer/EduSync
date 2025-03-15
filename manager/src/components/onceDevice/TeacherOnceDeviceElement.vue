<script setup lang="ts">
const props = defineProps({
  device_id: String
})
</script>

<script lang="ts">
export default {
  data() {
    return {
      action_list: [
        {
          name: '远程关机',
          icon: 'stop',
          description: '如果该设备在线，远程关闭该设备。',
          command: 'shutdown /r /t 5000'
        },
        {
          name: '远程重启',
          icon: 'restart_alt',
          description: '如果该设备在线，远程重启该设备。',
          command: 'powershell.exe /c Restart-Computer'
        },
        {
          name: '远程锁机',
          icon: 'lock',
          description: '如果该设备在线，使该设备切换到锁屏状态。',
          command: 'rundll32.exe user32.dll,LockWorkStation'
        },
        {
          name: '重启设备至BIOS',
          icon: 'power_settings_new',
          description: '如果该设备在线，重启至BIOS（设备主板内置的管理界面）。',
          command: 'shutdown.exe /r /fw /t 5000'
        },
        {
          name: '整理 C 盘',
          icon: 'cleaning_services',
          description: '如果该设备在线，对 C 盘进行碎片整理。',
          command: 'defrag C:'
        },
        {
          name: '远程更新系统',
          icon: 'update',
          description: '如果该设备在线，检查并安装系统更新。',
          command: 'powershell.exe -Command "Start-Process wusa.exe -ArgumentList \'/quiet /norestart\'"'
        },
        {
          name: '远程清理临时文件',
          icon: 'delete',
          description: '如果该设备在线，清理临时文件以释放磁盘空间。',
          command: 'powershell.exe -Command "Get-ChildItem -Path $env:TEMP -Recurse -Force | Remove-Item -Force -Recurse"'
        },
        {
          name: '远程检查磁盘错误',
          icon: 'check',
          description: '如果该设备在线，检查磁盘错误。',
          command: 'chkdsk C: /f /r'
        },
        {
          name: '远程强制关机',
          icon: 'power_off',
          description: '如果该设备在线，强制关闭该设备。',
          command: 'shutdown /s /f /t 0'
        },
        {
          name: '远程注销用户',
          icon: 'logout',
          description: '如果该设备在线，注销当前用户。',
          command: 'shutdown /l'
        },
        {
          name: '远程打开命令提示符',
          icon: 'terminal',
          description: '如果该设备在线，打开命令提示符。',
          command: 'cmd'
        },
        {
          name: '远程打开文件资源管理器',
          icon: 'folder',
          description: '如果该设备在线，打开文件资源管理器。',
          command: 'explorer'
        },
        {
          name: '远程打开控制面板',
          icon: 'settings',
          description: '如果该设备在线，打开控制面板。',
          command: 'control'
        },
        {
          name: '远程打开任务管理器',
          icon: 'task',
          description: '如果该设备在线，打开任务管理器。',
          command: 'taskmgr'
        },
        {
          name: '远程打开设备管理器',
          icon: 'device_hub',
          description: '如果该设备在线，打开设备管理器。',
          command: 'devmgmt.msc'
        },
        {
          name: '远程打开注册表编辑器',
          icon: 'code',
          description: '如果该设备在线，打开注册表编辑器。',
          command: 'regedit'
        },
        {
          name: '远程打开系统信息',
          icon: 'info',
          description: '如果该设备在线，打开系统信息。',
          command: 'msinfo32'
        },
        {
          name: '远程打开事件查看器',
          icon: 'event',
          description: '如果该设备在线，打开事件查看器。',
          command: 'eventvwr'
        },
        {
          name: '远程打开网络连接',
          icon: 'network_check',
          description: '如果该设备在线，打开网络连接。',
          command: 'control netconnections'
        }
      ]
    }
  }
}
</script>

<template>
  <mdui-card class="card">
    <h1>快捷操作</h1>
    <mdui-tooltip
      variant="rich"
      headline="该设备的设备 ID"
      content="可将该 ID 交给学校管理员深度控制该设备。"
    >
      <p>对 {{props.device_id}}：</p>
    </mdui-tooltip>
    <div>
      <mdui-tooltip v-for="action in action_list" v-bind:key="action.name" variant="rich">
        <mdui-button style="margin: 0.25rem;" :icon="action.icon">{{action.name}}</mdui-button>
        <h3 slot="headline">{{action.name}}</h3>
        <div slot="content">
          {{action.description}}
        </div>
      </mdui-tooltip>
    </div>
  </mdui-card>
  <div style="display: inline">
    <mdui-card class="card line left">
      <h2>在线状态</h2>
      <mdui-tooltip
        variant="rich"
        content="该设备正在运行中且监管服务正常。"
      >
        <p style="color: rgba(var(--mdui-color-primary))">当前在线</p>
      </mdui-tooltip>
      <mdui-tooltip
        variant="rich"
        content="该设备未运行或无法连接到该设备。"
      >
        <p style="color: rgba(var(--mdui-color-error))">已离线</p>
      </mdui-tooltip>
      <mdui-tooltip
        variant="rich"
        content="该设备上次与服务器互动的时间。"
      >
        <p>上次在线：1145/1/4</p>
      </mdui-tooltip>
    </mdui-card>
    <mdui-card class="card line right">
      <h2>设备信息</h2>
      <mdui-tooltip
        variant="rich"
        content="设备的名称，请在对应设备修改。"
      >
        <p>备注名：desk</p>
      </mdui-tooltip>
      <mdui-tooltip
        variant="rich"
        content="如果该设备占用率长时间过高，设备可能无法正常连接，请检查该设备。"
      >
        <p>CPU占用率：0% 内存占用率：0% </p>
      </mdui-tooltip>
    </mdui-card>
  </div>
</template>

<style scoped>
.card {
  background-color: rgba(var(--mdui-color-secondary-container));
  padding: 1rem;
  width: 100%;
}
.line {
  width: calc(50% - 0.125rem);
  display: inline-grid;
}
.left {
  margin-right: 0.125rem;
}
.right {
  margin-left: 0.125rem;
}
</style>