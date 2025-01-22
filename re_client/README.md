Java FX 版客户端
======
---

![wakatime](https://wakatime.com/badge/user/e70a83fc-1577-4ce4-8eb0-e9d9aa6d313d/project/8214cc1c-67bf-46b3-9805-fda0aa66fe80.svg)

> **提示：** 客户端现已分为 Pyside6 端与 Java FX 端

## 说明

> 环境需求：
> * JDK 21
> * Intellij IDEA 2024.3.2+
> * gradle 8.8+

### 编译

构建项目：
```commandline
gradlew clean build
```

可以使用 Gradle 项目预设指令`jpackage`编译：
```commandline
gradlew jpackage
```

### 测试

IDEA 并不会直接知道如何测试 JavaFX 应用，所以需要手动运行`run`任务：
```commandline
gradlew run
```
运行完成后，会自动启动客户端。