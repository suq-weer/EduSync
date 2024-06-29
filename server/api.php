<?php
include("config.php");

//基本api
function json($states, $msg, $data = "")//输出
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

function get_result($states,$type,$data="")//获取标准化输出结果
{
    return json($states,info_server($type),$data);
}


//获取配置信息
function get_info($aim,$type): string
{
    if($type=="software")
    {
        return info_software($aim);
    }
    elseif ($type=="server")
    {
        return info_server($aim);
    }
    return "";
}

//判断密码本是否正确
function if_codeBook($data): bool
{
    return $data == info_software("system_codeBook");
}

//判断最高权限用户是否正确
function if_adminUser($admin_uid,$admin_password): bool
{
    return $admin_uid == info_server("admin_uid") && $admin_password == info_server("admin_password");
}