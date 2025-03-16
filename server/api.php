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

function json($states, $msg, $data = "", $total_list="")//输出
{
    return json_encode(array('states' => $states, 'msg' => $msg, "data" => $data, "total_list" => $total_list));
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
     * u改写 特殊值u_aim,u_data
     * //l特殊的r
     */
    /*
     * data,json格式
     * 参数:
     * "token" => "" //value where,
     * "sortWay" => "DESC" ,
     * sortWayBy => "id",
     * ORDER BY `id` DESC
     * DELETE FROM `list_fri` WHERE `id` = '{$id}'
     */
    //print_r($code);
    $data = json_decode($code['data'],true);//解data
    $sortWay = $code['sortWay'];
    $sortWayBy = $code['sortWayBy'];
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
    elseif ($code['type']=="r"||$code['type']=="l") {
        $i = 0;
        //获取键及其键值并组合
        foreach ($data as $key => $value) {
            if ($i === count(array_values($data))-1) {
                $sqlCodeEnd = $sqlCodeEnd . "`$key` = '$value'";//`uid`='{$uid}'
            }else $sqlCodeEnd = $sqlCodeEnd . "`$key` = '$value'" . " AND ";
            $i++;
        }
//        echo '<br>'.$sqlCodeEnd;
        if ($sqlCodeEnd=="`` = ''") {
            $order = "";
            if ($sortWay != "" && $sortWayBy != "") $order = " ORDER BY `" . $sortWayBy . "` " . $sortWay;
            $sqlCode = "SELECT * FROM `" . $code['dataSheet'] . "` "  . $order;
        }else {
            //$sortWay = "DESC";
            //$sortWayBy = "id";
            $order = "";
            if ($sortWay != "" && $sortWayBy != "") $order = " ORDER BY `" . $sortWayBy . "` " . $sortWay;
            $sqlCode = "SELECT * FROM `" . $code['dataSheet'] . "` WHERE " . $sqlCodeEnd . $order;
        }
    }
    elseif ($code['type']=="l_s"){//search
        $i = 0;
        //获取键及其键值并组合
        foreach ($data as $key => $value) {
            if ($i === count(array_values($data))-1) {
                $sqlCodeEnd = $sqlCodeEnd . "`$key` LIKE '$value'";//`uid`='{$uid}'
            }else $sqlCodeEnd = $sqlCodeEnd . "`$key` LIKE '$value'" . " AND ";
            $i++;
        }

//        echo '<br>'.$sqlCodeEnd;
//        print_r($data);
        //$sortWay = "DESC";
        //$sortWayBy = "id";
        $order = "";
        if ($sortWay != "" && $sortWayBy != "") $order = " ORDER BY `" . $sortWayBy . "` " . $sortWay;
        $sqlCode = "SELECT * FROM `" . $code['dataSheet'] . "` WHERE " . $sqlCodeEnd . $order;
//        echo $sqlCode;
    }
    elseif ($code['type']=="d"){
        $i = 0;
        //获取键及其键值并组合
        foreach ($data as $key => $value) {
            if ($i === count(array_values($data))-1) {
                $sqlCodeEnd = $sqlCodeEnd . "`$key` = '$value'";//`uid`='{$uid}'
            }else $sqlCodeEnd = $sqlCodeEnd . "`$key` = '$value'" . " AND ";
            $i++;
        }

        $sqlCode = "DELETE FROM `" . $code['dataSheet'] . "` WHERE" . $sqlCodeEnd;
    }
    elseif ($code['type']=="u"){
        $i = 0;
        //获取键及其键值并组合
        foreach ($data as $key => $value) {
            if($key != "u_aim" && $key != "u_data"){
                //echo count(array_values($data))-1;
                if ($i === count(array_values($data))-3) {//3=一个uaim一个udata还有一个基础值1
                    $sqlCodeEnd = $sqlCodeEnd . "`$key` = '$value'";//`uid`='{$uid}'
                }else $sqlCodeEnd = $sqlCodeEnd . "`$key` = '$value'" . " AND ";
            }
            $i++;
        }

        //$sortWay = "DESC";
        //$sortWayBy = "id";
        $order = "";
        if ($sortWay!="" && $sortWayBy!="") $order=" ORDER BY `" . $sortWayBy . "` " . $sortWay;
        $sqlCode = "UPDATE `" . $code['dataSheet'] . "` SET `" . $data["u_aim"] . "` = '" . $data["u_data"] . "' WHERE " . $sqlCodeEnd . $order;
        //echo $sqlCode;
    }

//    echo $sqlCode;
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
    //echo $sqlCode;
    //echo $sortWay;

    if ($type=="w"||$type=="d") return $connect -> query($sqlCode);
    elseif ($type=="r") return mysqli_fetch_assoc($connect -> query($sqlCode));
    elseif ($type=="l"){
        $list = [];
        $cx_connect = mysqli_query($connect, $sqlCode);

        while ($data =  mysqli_fetch_assoc($cx_connect)){
                $list[] = $data;
        }

        return $list;
    }
    elseif ($type=="l_s"){
        $list = [];
        $cx_connect = mysqli_query($connect, $sqlCode);

        while ($data =  mysqli_fetch_assoc($cx_connect)){
            $list[] = $data;
        }

        return $list;
    }
    elseif ($type=="u") return $connect -> query($sqlCode);


    return "";
}

function get_result($states,$type,$data="",$total_list="")//获取标准化输出结果
{
//    echo $total_list;
    return json($states,info_server($type),$data,$total_list);
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

    //print_r(operate_database("r","user_token",$data,"DESC","id"));
    return json_encode(operate_database("r","user_token",$data,"DESC","id"));
}

//token->etffectiveDuration
function get_user_token_etffectiveDuration($data)
{
//    echo $data;
    $token = json_decode($data,true);//tokenAll
    $timeStamp_token = $token['time'];//tokenTime
    $timeStamp_now = time();//now

    if ($timeStamp_now-$timeStamp_token <= get_info("user_token_effectiveDuration" , "software")){
        return $timeStamp_now-$timeStamp_token;
    }
    else{
        return false;
    }
    return "";
}

//此处封装了一个函数以节约代码，函数发挥判断token有效性作用
function if_user_token($deviceId,$token)
{
    if (!get_user_token_etffectiveDuration(read_user_token("token",$token))){
        die(get_result(
            0,
            "result_failure_read_token",
            "token已失效",
        ));
    }
    elseif ($deviceId!=json_decode(read_user_token("token",$token),true)['device_id']){
        die(get_result(
            0,
            "result_failure_read_token",
            "与token绑定设备不一",
        ));
    }
}

//上传设备信息
function upload_user_device($deviceId,$data): int
{
    $timeStamp = time();//now
    $code = json_encode([
        "device_id" => $deviceId,
        "data" => $data,
        "time" => $timeStamp,
        "notes" => operate_database("r","user",json_encode(["device_id" => $deviceId]))['notes']
    ]);
    operate_database("d","user",json_encode(["device_id" => $deviceId]));
    return operate_database("w","user",$code) ? 1 : 0;
}

function upload_user_device_notes($deviceId,$notes)
{
    $code = operate_database("r","user",json_encode(["device_id" => $deviceId]));
    $code['notes'] = $notes;
    $code = json_encode($code);
//    echo $code;

    operate_database("d","user",json_encode(["device_id" => $deviceId]));
    return operate_database("w","user",$code) ? 1 : 0;
}

function read_user_device($deviceId)
{
    $data = json_encode([
        "device_id" => $deviceId,

    ]);

    //print_r(operate_database("r","user",$data));
    return operate_database("r","user",$data);
}

//创建指令
function create_user_command($type,$code,$deviceId)
{
    $timeStamp = microtime(true)*10000;//now
//    echo $timeStamp;
    $data = json_encode([
        "id" => $timeStamp,
        "type" => $type,
        "code" => $code,
        "time" => $timeStamp,
        "effective" => 0,
        "device_id" => $deviceId,
    ]);

    //print_r($data);
    return operate_database("w","user_command",$data) ? 1 : 0;
}

//获取指令
function get_user_command($deviceId)
{
    $data = json_encode([
        "effective" => 0,
        "device_id" => $deviceId,
    ]);

    //print_r(operate_database("l","user_command",$data,"DESC","id"));
    return operate_database("l","user_command",$data,"DESC","id");
}

//上传指令退出码
function upload_user_command($commandId,$result)
{
    $code = operate_database("r","user_command",json_encode(["id" => $commandId]));
    $code['result'] = $result;
    $code = json_encode($code);
//    echo $code;

    operate_database("d","user_command",json_encode(["id" => $commandId]));
    return operate_database("w","user_command",$code) ? 1 : 0;
}


//检查 uid 是否存在
function if_exist_admin_user($uid){
    $data = json_encode([
        "uid" => $uid,
    ]);
    
    return operate_database("r","admin_user",$data) ? 1 : 0;
}


//管理员登录
function read_admin_user($uid)
{
    $data = json_encode([
        "uid" => $uid,
    ]);

    return operate_database("r","admin_user",$data);
}

//创建 key
function create_admin_key($uid){
    $timeStamp = microtime(true);
    $key = code_base64($timeStamp."edusync".rand(0,10000),"encode");
    
    $data = json_encode([
        "id" => $timeStamp,
        "admin_user_id" => read_admin_user($uid)['id'],
        "user_key" => $key,
        "time" => $timeStamp,
    ]);
    
    return operate_database("w","admin_key",$data) ? $key : 0;
}

//读取 key
function read_admin_key($key){
    $data = json_encode([
        "user_key" => $key,
    ]);

    return operate_database("r","admin_key",$data);
}

//key 是否存在或者过期
function if_admin_key($uid,$key){
    $result = read_admin_key($key);
    
    if (!$result){
        die(get_result(
            0,
            "result_failure_read_admin_key",
            "查询不到该key",
        ));
    }
    if (time()-$result['time']>=get_info("admin_key_etffectiveDuraion","software")){
        die(get_result(
            0,
            "result_failure_read_admin_key",
            "该key已经失效",
        ));
    }

    if (read_admin_user($uid)['id']!=$result["admin_user_id"]){
        die(get_result(
            0,
            "result_failure_read_admin_key",
            "该key绑定账号与操作账号不一致",
        ));
    }

}


//获得list数据
//设备列表
function get_list_data_device($key="",$value="")
{
    if ($key==""){
        $data = json_encode([
            ""=>"",
        ]);
        return operate_database("l","user",$data,"DESC","time");
    }else{
        $data = json_encode([
            $key=>"%".$value."%",
        ]);
        return operate_database("l_s","user",$data,"DESC","time");
    }
}

function get_list_device($key,$value,$page=0,$length=10): array
{
    $page = $page-1;
    $list_data = get_list_data_device($key,$value);
    $chunkedArrays = array_chunk($list_data, $length);
    $chunkedArrays['total_list'] = count($list_data);
//    print_r($chunkedArrays);
    return $chunkedArrays;
}

//指令列表
function get_list_data_command($key="",$value="")
{
    if ($key==""){
        $data = json_encode([
            ""=>"",
        ]);
        return operate_database("l","user_command",$data,"DESC","time");
    }else{
        $data = json_encode([
            $key=>"%".$value."%",
        ]);
        return operate_database("l_s","user_command",$data,"DESC","time");
    }
}

function get_list_command($key,$value,$page=0,$length=10): array
{
    $page = $page-1;
    $list_data = get_list_data_command($key,$value);
    $chunkedArrays = array_chunk($list_data, $length);
    $chunkedArrays['total_list'] = count($list_data);
    return $chunkedArrays;
}


function delete_device($deviceId)
{
    $data = json_encode([
        "device_id" => $deviceId,
    ]);
    return operate_database("d","user",$data);
}