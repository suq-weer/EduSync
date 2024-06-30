<?php
include("config.php");

//基本api
function is_empty_request($data): int
{
    foreach ($data as $value) {
        if ($value=="") {
            return 0;
        }
    }
    return 1;
}

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
    $connect = new mysqli(info_server("database_servername"),
        info_server("database_username"),
        info_server("database_password"),
        info_server("database_dbname")
    );

    if ($connect->connect_error) {
        //return json(0,"连接失败: " . $connect->connect_error);
        die();
    }
    return $connect;
    //$connect->close();
}

function get_sqlCode($code): string//生成sql指令
{
    /*
     * w写入
     * r读取
     * d删除
     * //l特殊的r
     */
    /*
     * data,json格式
     * 参数:
     * "token" => "" //value where,
     * "sortWay" => "ORDER" ,
     * sortWayBy => "id",
     * ORDER BY `id` DESC
     */
    $data = json_decode($code['data'],true);
    $sqlCode="";

    if ($code['type']=="w") {

        $sqlCodeCenter = "(`" . implode('` , `', array_keys($data)) . "`)";
        $sqlCodeEnd="";
        $i = 0;

        foreach (array_values($data) as $value) {
            if ($i === count(array_values($data))-1) {
                $sqlCodeEnd= $sqlCodeEnd.$value."'";
            }else $sqlCodeEnd= $sqlCodeEnd.$value."','";
            $i++;
        }

        $sqlCodeEnd = "('" . $sqlCodeEnd . ")";
        $sqlCode = "INSERT INTO"." `".$code['dataSheet']."` ".$sqlCodeCenter." VALUE ".$sqlCodeEnd;
    }
    elseif ($code['type']=="r") {
        $sqlCode = "SELECT COUNT(*)";
    }
    return $sqlCode;
}

function operate_database($type,$dataSheet,$data)//操作数据库
{
    $connect = database();

    $code = [
        "type" => $type,
        "dataSheet" => $dataSheet,
        "data" => $data,
    ];
    $sqlCode = get_sqlCode($code);

    if ($type=="w"||$type=="d") return $connect -> query($sqlCode);
    elseif ($type=="r") return $connect -> query($sqlCode) -> fetch_assoc();
    return "";
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