import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          // 所有以 mdui- 开头的标签名都是 mdui 组件
          isCustomElement: (tag) => tag.startsWith('mdui-')
        }
      }
    }),
    vueJsx()
  ],
  resolve: {},
  server: {
    proxy: {
      '/server': 'http://edusync619.yiyu14.top',
      '/dev-api': 'http://edusync619.yiyu14.top',
      '/api': 'http://edusync619.yiyu14.top'
    }
  }
})
