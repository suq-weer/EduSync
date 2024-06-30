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
        "database_servername" => "localhost",
        "database_username" => "edusync",
        "database_password" => "xiaoyi..",
        "database_dbname" => "edusync",

        //输出
        "result_success_get" => "获取成功",
        "result_failure_if_adminUser" => "最高权限用户信息错误",
        "result_success_add_token" => "申请token成功",
        "result_failure_add_token" => "申请token失败",

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