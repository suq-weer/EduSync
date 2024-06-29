<?php
//配置信息
function info_server($aim): string//后端
{
    $data = [

        //域名
        "domain_main" => "http://edusync.yiyu14.top/",//主域名
        "domain_sub" => "http://edusync.yiyu14.top/",//运行目录

        //代码级权限用户
        "admin_uid" => "xiaoyi",
        "admin_password" => "xiaoyi..",

        //数据库
        "datebase_servername" => "localhost",
        "datebase_username" => "edusync",
        "datebase_password" => "xiaoyi..",
        "datebase_dbname" => "edusync",

        //输出
        "result_success_get" => "获取成功",
        "result_failure_if_adminUser" => "最高权限用户信息错误",

    ];
    return $data[$aim];
}
function info_software($aim): string//软件
{
    $data = [

        //系统信息
        "system_codeBook" => "Edusync619!",//密码本

    ];
    return $data[$aim];
}