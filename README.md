# 学校多媒体设备互联系统计划书

## 目的

目前学校主流多媒体设备（如老式`Windows`台式机、希沃一体机等）配套的第一方软件生态，主要还是针对以本机为中心进行教学资源管理与其他课堂互动操作。而本系统可以实现私有的教学资源管理，也可以通过中心化的调配管理可以更好地让学校信息人员进行多媒体设备的机况评估与临时介入处理。

## 功能

### 一、实时的设备运行状况检测

通过让终端给中心服务器发送自身的使用信息，并在服务器上处理和在后台给管理员进行展示。

### 二、服务器介入远程处理终端

为了能更好地优化多媒体设备，可以使用服务端后台进行一些远程指令，比如远程停止进程等。

### 三、教育资源多端共享

将一些老师常用的学科课件及讲义上传至服务器后台，一键无物理介质下载所需课件。

## 参与贡献

### 客户端+管理端

>*建议在 Anaconda 虚拟 Python 环境下开发。*

pip 安装：

```commandline
pip install -r .\requirements.txt
```

Anaconda 安装：

```commandline
conda env create -f .\environment.yml
```

#### 编译方法

```commandline
python -m nuitka --lto --standalone .\client\main.py
python -m nuitka --lto --standalone .\manager\main.py
```

### 服务端

#### 运行环境

**PHP 7.3+MySQL 5.7.44+Nginx 1.24.0**

#### 导入数据库

##### 登录

```commandline
mysql -u 用户名 -p
```

##### 创建并导入数据库

```sql
CREATE DATABASE edusync;
USE edusync;
SOURCE .\server\edusync-无重置.sql
```

## TODO
* ~~实时上传多媒体设备状态（已完成）~~
* 多媒体设备状态可视化
* ~~多媒体设备状态采集（已完成）~~
* ~~服务器数据库设计（已完成）~~
* 教育资源平台可视化
* 教育资源平台数据库设计
* 多端教育资源文件流传逻辑