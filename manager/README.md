# manager 管理端

调试环境使用 Vite 驱动的 Vue 3。

## IDE设置

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (禁用 Vetur).

Webstorm 直接启动即可。

## TypeScript .vue 文件支持

TypeScript 默认无法处理 `.vue` 导入的类型信息，因此我们将 `tsc` CLI 替换为 `vue-tsc` 进行类型检查。在编辑器中，我们需要 [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) 来使 TypeScript 语言服务能够识别 '.vue' 类型。

## 自定义配置

见 [Vite Configuration Reference](https://vitejs.dev/config/).

## 项目设置

```sh
npm install
```

### 编译并启动热更新调试环境

```sh
npm run dev
```

### 类型检查并打包成生产环境

```sh
npm run build
```

### 运行 [Vitest](https://vitest.dev/) 来进行单元测试

```sh
npm run test:unit
```

### 运行 [Cypress](https://www.cypress.io/) 来进行端到端测试

```sh
npm run test:e2e:dev
```

这将针对 Vite 开发服务器运行端到端测试。
它比生产版本快得多。

但仍然建议在部署之前使用 `test:e2e` 测试生产版本（例如在 CI 环境中）：

```sh
npm run build
npm run test:e2e
```

### 使用 [ESLint](https://eslint.org/) 来检查代码

```sh
npm run lint
```
