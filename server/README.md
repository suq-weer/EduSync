服务端
======
---

## 运行环境

**PHP 7.3 + MySQL 5.7.44 + Nginx 1.24.0**

## 配置信息
在config.php里进行修改：
1. **找到`info_server()`函数**
2. **修改如下代码：**<br>
```php
//域名
"domain_main" => "部署域名",//主域名
"domain_sub" => "部署域名+运行目录",//运行目录

//代码级权限用户
"admin_uid" => "xiaoyi",
"admin_password" => "xiaoyi..",
```
3. **次要信息配置(可略过)**

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
## 导入数据库

### 登录

```commandline
mysql -u 用户名 -p
```

### 创建并导入数据库

```sql
CREATE DATABASE edusync;
USE edusync;
SOURCE .\server\edusync-无重置.sql
```

> *可以使用phpMyadmin来配置数据库*</br>
> *如果懒得在源代码里面配置信息的话，就：*</br>
> *数据库名称：edusync*</br>
> *账号：edusync*</br>
> *密码：xiaoyi..*</br>
> *(这是项目默认的)*

### 自定义数据库账号

在`config.php`里进行修改：

1. 找到`info_server()`函数

2. 修改如下代码：

```php
"database_servername" => "localhost",
"database_username" => "数据库账号",
"database_password" => "数据库密码",
"database_dbname" => "数据库名称",
```