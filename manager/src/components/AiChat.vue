<script lang="ts">
import MarkdownIt from 'markdown-it';
import { ref } from 'vue'
export default {
  data() {
    const loading = ref(false);
    return {
      inputText: '',
      responseText: '',
      renderedMarkdown: '',
      loading
    };
  },
  methods: {
    async sendMessage() {
      this.loading = true;
      this.responseText = '';
      this.renderedMarkdown = '';

      try {
        const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
          method: "POST",
          headers: {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            "model": "deepseek/deepseek-r1:free",
            "messages": [
              {
                "role": "user",
                "content": this.inputText
              }
            ]
          })
        });

        // 检查 response 是否是一个可迭代的流对象
        if (response.body instanceof ReadableStream) {
          const reader = response.body.getReader();
          while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const decoder = new TextDecoder('utf-8');
            const chunk = decoder.decode(value, { stream: true });
            this.responseText += chunk;
            // console.log(this.responseText);
          }
          const responseText = JSON.parse(this.responseText)
          this.renderedMarkdown = this.md.render(responseText.choices[0].message.content);
          // console.log(response)
        } else {
          console.error('Response is not a ReadableStream:', response);
        }
      } catch (error) {
        console.error('Error:', error);
      }
      this.loading = false;
    },
  },
  computed: {
    md() {
      return new MarkdownIt();
    },
  },
};
</script>

<template>
  <mdui-card class="card">
    <h2>DeepSeek-R1</h2>
    <mdui-circular-progress v-if="loading" class="progress"></mdui-circular-progress>
    <div v-html="renderedMarkdown" class="contents"></div>
    <div class="text">
      <mdui-text-field v-model="inputText" placeholder="输入你的问题..."></mdui-text-field>
      <mdui-button @click="sendMessage">发送</mdui-button>
    </div>
  </mdui-card>
</template>

<style scoped>
.card {
  width: 100%;
  background: rgba(var(--mdui-color-secondary-container));
  padding: 1rem;
  margin-bottom: 1rem;
}
.contents {
  padding: 1rem;
  background: rgba(var(--mdui-color-surface-variant));
  box-shadow: var(--mdui-elevation-level1);
  border-radius: var(--mdui-shape-corner-small);
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
.progress {
  padding: 0.5rem;
}
</style>