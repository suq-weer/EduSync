<script setup lang="ts">
import { ref } from 'vue'
import MarkdownIt from 'markdown-it'
import AiPoop from '@/components/AIPoop.vue'
import UserPoop from '@/components/UserPoop.vue'

// 初始化Markdown解析器
const md = new MarkdownIt({ html: true })
// 用户输入文本的响应式引用
const inputText = ref('')
// 文本的引用id，此处未使用
const chatId = ref(0)
// 渲染后的Markdown文本引用
const renderedMarkdown = ref('')
// 加载状态的引用，用于控制UI显示
const loading = ref(false)
// 聊天记录的引用，包含渲染后的Markdown和是否为响应标识
interface ChatItem {
  chatId: number
  renderedMarkdown: string
  is_response: boolean
}
const chats = ref<ChatItem[]>([])

async function sendMessage(inputText:string) {
  chatId.value += 1
  if (inputText) {
    //向聊天列表新增数据
    chats.value.push({
      chatId: chatId.value,
      renderedMarkdown: inputText,
      is_response: false
    })

    chatId.value += 1
    loading.value = true
    chats.value.push({
      chatId: chatId.value,
      renderedMarkdown: '',
      is_response: true
    })


    try {
      // 发送POST请求到AI接口
      const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
        method: 'POST',
        headers: {
          Authorization:
            'Bearer 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',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          model: 'deepseek/deepseek-r1:free',
          stream: true,
          messages: [
            {
              role: 'user',
              content: inputText
            }
          ]
        })
      })

      //处理返回数据
      if (response.ok) {
        let currentContent = ''
        if (response.body instanceof ReadableStream) {
          const reader = response.body.getReader()
          // eslint-disable-next-line no-constant-condition
          while (true)
          {
            const { done, value } = await reader.read()
            if (done) break

            const chunk = new TextDecoder('utf-8').decode(value, { stream: true })
            if (chunk === ': OPENROUTER PROCESSING\n\n') continue

            console.log(chunk);
            // 将 chunk 按行分割并逐行处理
            const lines = chunk.split('\n')
            for (const line of lines) {
              if (line.trim() === 'data: [DONE]') {
                console.log('Stream ended with [DONE]');
                // 处理完当前累积的内容后结束
                if (currentContent) {
                  renderedMarkdown.value = md.render(currentContent)
                  console.log('Final rendered Markdown:', renderedMarkdown.value); // 调试信息
                  const item = chats.value.find(item => item.chatId === chatId.value);
                  if (item) {
                    item.renderedMarkdown = renderedMarkdown.value;
                  }
                  currentContent = ''
                }
                break;
              }
              if (line.startsWith('data: ')) {
                const dataLine = line.slice(6).trim(); // 去掉 'data: ' 前缀
                console.log('Received data:', dataLine)
                const responseJson = JSON.parse(dataLine)
                let deltaContent = ''
                if (responseJson.object === 'chat.completion.chunk') {
                  if (responseJson.choices[0].delta.content === '') {
                    try { deltaContent = responseJson.choices[0].delta.logprob.content[0].token } catch (e) { /* empty */ }
                  } else {
                    deltaContent = responseJson.choices[0].delta.content
                  }
                  if (deltaContent) {
                    currentContent += deltaContent
                    renderedMarkdown.value = md.render(currentContent)
                    // const chatIndex = chats.value.findIndex(chat => chat.chatId === chatId);
                    // chats[chatId.value].renderedMarkdown = renderedMarkdown.value
                    const item = chats.value.find(item => item.chatId === chatId.value);
                    if (item) {
                      item.renderedMarkdown = renderedMarkdown.value;
                    }
                    // console.log()
                  }
                  if (responseJson.choices[0].finish_reason) {
                    console.log('Final rendered Markdown:', renderedMarkdown.value); // 调试信息
                    currentContent = ''
                  }
                }
              }
            }
          }
        }else{
          console.error('Response is not a ReadableStream:', response)
        }
      }
    } catch (error) {
      console.log(error)
    }
  }
  loading.value = false
}
</script>

<template>
  <!-- 卡片组件，包含聊天记录和输入区域 -->
  <mdui-card class="card">
    <h2>DeepSeek-R1</h2>
    <!-- 循环渲染聊天记录 -->
    <div v-for="(chat) in chats" :key="chat.chatId">
      <!-- 如果是AI响应，显示为用户消息 -->
<!--      <mdui-card v-if="chat.is_response" class="user-message" >{{ chat.renderedMarkdown }}</mdui-card>-->
      <AiPoop v-if="chat.is_response" :response="chat.renderedMarkdown" avatar = "/src/assets/logo_DeepSeek.png"/>
      <!-- 如果是用户消息，使用AiPoop组件渲染 -->
      <UserPoop v-else :response="chat.renderedMarkdown" avatar = "/src/assets/logo.svg"/>
    </div>
    <!-- 如果处于加载状态，显示加载指示器 -->
    <mdui-circular-progress v-if="loading" class="loading-indicator"></mdui-circular-progress>
    <div class="text">
      <!-- 用户输入文本框 -->
      <mdui-text-field v-model="inputText" placeholder="输入你的问题..."></mdui-text-field>
      <!-- 发送按钮，点击时调用sendMessage函数 -->
      <mdui-button @click="sendMessage(inputText)">发送</mdui-button>
    </div>
  </mdui-card>
</template>

<style scoped>
/* 卡片样式 */
.card {
  width: 100%;
  padding: 1rem;
  background: rgba(var(--mdui-color-secondary-container));
}

/* 用户消息样式 */
.user-message {
  background: rgba(var(--mdui-color-primary-container));
  padding-left: calc(20% - 1rem);
  margin-bottom: 1rem;
}

/* 输入区域样式 */
.text {
  width: 100%;
  padding: 1rem;

  * {
    display: inline-block;
    vertical-align: top;
  }

  /* 文本输入框样式 */
  mdui-text-field {
    width: calc(80% - 1.5rem);
    height: 3rem;
    margin-right: 0.5rem;
  }

  /* 发送按钮样式 */
  mdui-button {
    width: calc(20% - 1.5rem);
    height: 3rem;
    margin-left: 0.5rem;
  }
}
</style>
