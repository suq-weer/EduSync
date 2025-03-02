<script setup lang="ts">
import { ref } from 'vue';

const messages = ref([
  { sender: 'AI', text: '你好！有什么我可以帮忙的吗？' }
]);

const userInput = ref('');

const sendMessage = () => {
  if (userInput.value.trim()) {
    messages.value.push({ sender: 'User', text: userInput.value });
    userInput.value = '';

    // 模拟AI回复
    setTimeout(() => {
      messages.value.push({ sender: 'AI', text: '这是AI的回复。' });
    }, 1000);
  }
};
</script>

<template>
  <mdui-container>
    <mdui-card>
      <mdui-card-header>
        <mdui-card-header-avatar>
          <mdui-avatar>
            <img src="https://via.placeholder.com/50" alt="AI Avatar" />
          </mdui-avatar>
        </mdui-card-header-avatar>
        <mdui-card-header-title>AI 聊天</mdui-card-header-title>
      </mdui-card-header>
      <mdui-card-content>
        <div class="chat-box">
          <div v-for="(message, index) in messages" :key="index" class="message" :class="{'user-message': message.sender === 'User', 'ai-message': message.sender === 'AI'}">
            <mdui-avatar v-if="message.sender === 'AI'" class="message-avatar">
              <img src="https://via.placeholder.com/50" alt="AI Avatar" />
            </mdui-avatar>
            <mdui-avatar v-if="message.sender === 'User'" class="message-avatar">
              <img src="https://via.placeholder.com/50" alt="User Avatar" />
            </mdui-avatar>
            <div class="message-text">{{ message.text }}</div>
          </div>
        </div>
      </mdui-card-content>
      <mdui-card-actions>
        <mdui-textfield class="mdui-textfield-expandable">
          <mdui-btn class="mdui-btn-icon" @click="sendMessage" mdui-tooltip="{content: '发送'}">
            <i class="mdui-icon material-icons">send</i>
          </mdui-btn>
          <input class="mdui-textfield-input" type="text" v-model="userInput" @keyup.enter="sendMessage" placeholder="输入你的消息..." />
        </mdui-textfield>
      </mdui-card-actions>
    </mdui-card>
  </mdui-container>
</template>

<style scoped>
.chat-box {
  height: 300px;
  overflow-y: auto;
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.message {
  margin-bottom: 10px;
  display: flex;
  align-items: flex-start;
}

.user-message {
  justify-content: flex-end;
}

.ai-message {
  justify-content: flex-start;
}

.message-avatar {
  margin-right: 10px;
}

.user-message .message-avatar {
  margin-left: 10px;
  margin-right: 0;
}

.message-text {
  display: inline-block;
  padding: 8px 12px;
  border-radius: 18px;
  background-color: #f1f1f1;
  max-width: 70%;
}

.user-message .message-text {
  background-color: #dcf8c6;
}
</style>
