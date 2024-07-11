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
     * "sortWay" => "DESC" ,
     * sortWayBy => "id",
     * ORDER BY `id` DESC
     */
    //print_r($code);
    $data = json_decode($code['data'],true);//解data
    $sortWay = $code['sortWay'];
    $sortWayBy = $code['sortWayBY'];
    //初始化
    $sqlCode="";
    $sqlCodeEnd="";

    if ($code['type']=="w") {//写

        $sqlCodeCenter = "(`" . implode('` , `', array_keys($data)) . "`)";//键
        $i = 0;

        foreach (array_values($data) as $value) {//键值
            if ($i === count(array_values($data))-1) {
                $sqlCodeEnd= $sqlCodeEnd.$value."'";
            }else $sqlCodeEnd= $sqlCodeEnd.$value."','";
            $i++;
        }

        $sqlCodeEnd = "('" . $sqlCodeEnd . ")";
        $sqlCode = "INSERT INTO"." `".$code['dataSheet']."` ".$sqlCodeCenter." VALUE ".$sqlCodeEnd;//组合
    }
    elseif ($code['type']=="r") {

        $i = 0;
        //获取键及其键值并组合
        foreach ($data as $key => $value) {
            if ($i === count(array_values($data))-1) {
                $sqlCodeEnd = $sqlCodeEnd . "`$key` = '$value'";//`uid`='{$uid}'
            }else $sqlCodeEnd = $sqlCodeEnd . "`$key` = '$value'" . " AND ";
            $i++;
        }

        //$sortWay = "DESC";
        //$sortWayBy = "id";
        $order = "";
        if ($sortWay!="" && $sortWayBy!="") $order=" ORDER BY `" . $sortWayBy . "` " . $sortWay;
        $sqlCode = "SELECT * FROM `" . $code['dataSheet'] . "` WHERE " . $sqlCodeEnd . $order;
    }
    return $sqlCode;
}

function operate_database($type,$dataSheet,$data,$sortWay = "",$sortWayBy = "")//操作数据库
{
    $connect = database();

    $code = [
        "type" => $type,
        "dataSheet" => $dataSheet,
        "sortWay" => $sortWay,
        "sortWayBy" => $sortWayBy,
        "data" => $data,
    ];
    $sqlCode = get_sqlCode($code);

    if ($type=="w"||$type=="d") return $connect -> query($sqlCode);
    elseif ($type=="r") return mysqli_fetch_array($connect -> query($sqlCode));

    return "";
}

function get_result($states,$type,$data="")//获取标准化输出结果
{
    return json($states,info_server($type),$data);
}

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


//获取配置信息
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

//one->Alltoken
function read_user_token($type,$data)
{
    $data = json_encode([
        $type => $data,

    ]);

    return json_encode(operate_database("r","user_token",$data,"DESC","id"));
}