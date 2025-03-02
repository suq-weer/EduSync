<script setup lang="ts">
import { ref } from 'vue'
import { cookie_read_user } from '@/api/manage'
import { send_commands } from '@/api/server'
import { alert } from 'mdui'

const input_code  = ref('')
const commands_list = ref([])

const props = defineProps({
  device_id: {
    type: String,
    required: true,
    default: ''
  }
})

const send_command = async () => {
  const lines = input_code.value.split(/\r?\n/)
  const list = []

  console.log(lines)

  for (let i = 0;i < lines.length; i++) {
    commands_list.value.push({
      "id": i,
      "type":1,
      "code": lines[i],
      "time":Date.now(),
      "deviceId": props.device_id,
    })

    list.push({
      "type":1,
      "code": lines[i],
      "deviceId": props.device_id,
    })
  }
  console.log(list)

  const result = await send_commands(cookie_read_user()['uid'], cookie_read_user()['key'], list)
  if (result){
    await alert({
      headline: "结果",
      description: result['data'],
      confirmText: "好的",
    })
  }
};
</script>

<template>
  <div>
    <mdui-card class="card commands">
      <h2>Commands</h2>
      <p v-for="command in commands_list" :key="command.id">[{{command.time}}]({{command.code}}){{command.id}}</p>
      <div>
        <mdui-text-field
          label="输入命令(一行一条)"
          placeholder="sudo rm -rf /*"
          rows="5"
          @input="input_code = $event.target.value"
        ></mdui-text-field>
        <mdui-button-icon icon="send" @click="send_command"></mdui-button-icon>
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