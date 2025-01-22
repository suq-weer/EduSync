Pyside6 客户端
======
---

## 说明

![wakatime](https://wakatime.com/badge/user/e70a83fc-1577-4ce4-8eb0-e9d9aa6d313d/project/8214cc1c-67bf-46b3-9805-fda0aa66fe80.svg)

> **提示：** 客户端现已分为 Pyside6 端与 Java FX 端。
> 
>*建议在 Anaconda 虚拟 Python 环境下开发。*

pip 安装：

```commandline
pip install -r .\requirements.txt
```

Anaconda 安装：

```commandline
conda env create -f .\environment.yml
```

## 编译方法

**给 Windows：**

```commandline
python -m nuitka --lto=yes --output-dir=build --output-file=edusync-client.exe --enable-plugin=pyside6 --windows-uac-admin --onefile .\client\main.py
```