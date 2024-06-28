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

    ];
    return $data[$aim];
}
function info_software($aim): string
{
    $data = [

        //系统信息
        "system_codeBook" => "Edusync619!",//密码本

    ];
    return $data[$aim];
}


//基本api
function json($states, $msg, $data = "")//输出api
{
    return json_encode(array('states' => $states, 'msg' => $msg, "data" => $data));
}

function code_base64($text,$type)//base64加解密
{
    if ($type=="encode")//加密
    {
        return base64_encode($text);
    }
    elseif ($type=="decode")
    {
        return base64_decode($text);
    }
    return "";
}

function database()//数据库连接
{
    $connect = new mysqli(info_server("datebase_servername"),
        info_server("datebase_username"),
        info_server("datebase_username"),
        info_server("datebase_dbname")
    );

    if ($connect->connect_error) {
        //return json(0,"连接失败: " . $connect->connect_error);
        die();
    }
    return $connect;
    //$connect->close();
}

