<script setup lang="ts">
import { ref } from 'vue'
import MarkdownIt from 'markdown-it'
import AiPoop from '@/components/AIPoop.vue'

const md = new MarkdownIt()
const inputText = ref('')
const responseText = ref('')
const renderedMarkdown = ref('')
const loading = ref(false)
const chats = ref([
  {
    renderedMarkdown: '',
    is_response: false
  }
])

async function sendMessage() {
  loading.value = true
  responseText.value = ''
  renderedMarkdown.value = ''

  try {
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
            content: inputText.value
          }
        ]
      })
    })
    if (response.ok) {
      chats.value.push({
        renderedMarkdown: inputText.value ,
        is_response: false
      })
    }

    if (response.body instanceof ReadableStream) {
      const reader = response.body.getReader()
      let i = 0
      let currentContent = ''

      // eslint-disable-next-line no-constant-condition
      while (true) {
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
              if (chats.value.length <= i) {
                chats.value.push({
                  renderedMarkdown: renderedMarkdown.value,
                  is_response: true
                })
              } else {
                chats.value[i].renderedMarkdown = renderedMarkdown.value
              }
              i++
              currentContent = ''
            }
            break;
          }

          if (line.startsWith('data: ')) {
            const dataLine = line.slice(6).trim(); // 去掉 'data: ' 前缀
            try {
              console.log('Received data:', dataLine)
              const responseJson = JSON.parse(dataLine)
              if (responseJson.object === 'chat.completion.chunk') {
                const deltaContent = responseJson.choices[0].delta.content
                if (deltaContent) {
                  currentContent += deltaContent
                  renderedMarkdown.value = md.render(currentContent)
                  if (chats.value.length <= i) {
                    chats.value.push({
                      renderedMarkdown: renderedMarkdown.value,
                      is_response: true
                    })
                  } else {
                    chats.value[i].renderedMarkdown = renderedMarkdown.value
                  }
                }
                if (responseJson.choices[0].finish_reason) {
                  console.log('Final rendered Markdown:', renderedMarkdown.value); // 调试信息
                  i++
                  currentContent = ''
                }
              }
            } catch (e) {
              console.error('Failed to parse JSON:', e)
            }
          }
        }
      }
    } else {
      console.error('Response is not a ReadableStream:', response)
    }
  } catch (error) {
    console.error('Error:', error)
    alert('请求失败，请稍后再试')
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <mdui-card class="card">
    <h2>DeepSeek-R1</h2>
    <div v-for="(chat, index) in chats" :key="index">
      <mdui-card v-if="chat.is_response" class="user-message">{{ chat.renderedMarkdown }}</mdui-card>
      <AiPoop v-else :response="chat.renderedMarkdown" />
    </div>
    <mdui-circular-progress v-if="loading" class="loading-indicator"></mdui-circular-progress> <!-- 加载指示器 -->
    <div class="text">
      <mdui-text-field v-model="inputText" placeholder="输入你的问题..."></mdui-text-field>
      <mdui-button @click="sendMessage">发送</mdui-button>
    </div>
  </mdui-card>
</template>

<style scoped>
.card {
  width: 100%;
  padding: 1rem;
  background: rgba(var(--mdui-color-secondary-container));
}

.user-message {
  background: rgba(var(--mdui-color-primary-container));
  padding-left: calc(20% - 1rem);
  margin-bottom: 1rem;
}

.text {
  width: 100%;
  padding: 1rem;

  * {
    display: inline-block;
    vertical-align: top;
  }

  mdui-text-field {
    width: calc(80% - 1.5rem);
    height: 3rem;
    margin-right: 0.5rem;
  }

  mdui-button {
    width: calc(20% - 1.5rem);
    height: 3rem;
    margin-left: 0.5rem;
  }
}
</style>
