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

### 客户端

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

**给 Windows：**

```commandline
python -m nuitka --lto=yes --output-dir=build --output-file=edusync-client.exe --enable-plugin=pyside6 --windows-uac-admin --onefile .\client\main.py
```

### 服务端

#### 运行环境

**PHP 7.3+MySQL 5.7.44+Nginx 1.24.0**
#### 配置信息
在config.php里进行修改：
1. 找到info_server函数
2. 修改如下代码：<br>
```php
//域名
"domain_main" => "部署域名",//主域名
"domain_sub" => "部署域名+运行目录",//运行目录

//代码级权限用户
"admin_uid" => "xiaoyi",
"admin_password" => "xiaoyi..",
```
3. 次要信息配置(可略过)

```php
//输出
"result_success_get" => "获取成功",
"result_failure_if_adminUser" => "最高权限用户信息错误",
"result_success_add_token" => "申请token成功",
"result_failure_add_token" => "申请token失败",
"result_failure_read_token" => "读取token失败",
"result_success_read_token" => "读取token成功",
"result_failure_upload_device" => "上传设备信息失败",
"result_success_upload_device" => "上传设备信息成功",
"result_failure_read_device" => "读取设备信息失败",
"result_success_read_device" => "读取设备信息成功",
"result_success_get_command" => "读取指令成功",
"result_failure_get_command" => "读取指令失败",
"result_success_create_command" => "创建指令成功",
"result_failure_create_command" => "创建指令失败",
"result_success_login_admin_user" => "登录管理员成功",
"result_failure_login_admin_user" => "登录管理员失败",
"result_success_read_admin_key" => "读取key成功",
"result_failure_read_admin_key" => "读取key失败",
```
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

>*可以使用phpMyadmin来配置数据库
如果懒得在源代码里面配置信息的话，就：
数据库名称：edusync
账号：edusync
密码：xiaoyi..
(这是项目默认的)*

##### 自定义数据库账号

在config.php里进行修改：

1. 找到info_server函数

2. 修改如下代码：

```php
"database_servername" => "localhost",
"database_username" => "数据库账号",
"database_password" => "数据库密码",
"database_dbname" => "数据库名称",
```


## TODO
* ~~实时上传多媒体设备状态（已完成）~~
* 多媒体设备状态可视化
* ~~多媒体设备状态采集（已完成）~~
* ~~服务器数据库设计（已完成）~~
* 教育资源平台可视化
* 教育资源平台数据库设计
* 多端教育资源文件流传逻辑