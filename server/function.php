<?php
include("api.php");

//token
function get_token($bookCode,$device_id)
{
    $timeStamp = time();
    $token = code_base64($timeStamp."edusync".rand(0,10000),"encode");

    $data = json_encode([
        "id" => $timeStamp,
        "device_id" => $device_id,
        "time" => $timeStamp,
        "token" => $token,
    ]);

    if(!if_codeBook($bookCode))die(get_result(
        0,
        "result_failure_add_token",
        "密码本错误",
    ));
    elseif (
        ($timeStamp-json_decode(read_user_token("device_id",$device_id),true)['time'])<=get_info("user_token_effectiveDuration","software")){
        //echo ($timeStamp-json_decode(read_user_token("device_id",$device_id),true)['time'])/60;
        return [
            "states" => 1,
            "data" => json_decode(read_user_token("device_id",$device_id),true)['token'],
        ];
    }


    return [
        "states" => operate_database("w","user_token",$data),
        "data" => $token,
    ];
}

function fun_read_user_token($type,$data)
{
    $result = read_user_token($type,$data);
    if ($result==null||$result=="null"){
        die(get_result(
            0,
            "result_failure_read_token",
            "结果为空",
        ));
    }
    elseif (!get_user_token_etffectiveDuration($result)){
        die(get_result(
            0,
            "result_failure_read_token",
            "token已失效",
        ));
    }

//return get_result(1,"result_success_read_token",$result);写错了
    return [
        "states" => 1,
        "data" => $result,
    ];
}


//设备
function fun_upload_user_device($deviceId,$data,$token): array
{
    if_user_token($deviceId,$token);

    return [
        "states" => upload_user_device($deviceId,$data),
    ];
}

function fun_read_user_device($deviceId,$token)
{
    $result = read_user_device($deviceId);

    if_user_token($deviceId,$token);
    if ($result==null||$result=="null"){
        die(get_result(
            0,
            "result_failure_read_device",
            "结果为空",
        ));
    }

    return [
        "states" => 1,
        "data" => $result,
    ];
}


//指令
function fun_get_user_command($deviceId,$token)
{
    if_user_token($deviceId,$token);
    $result = get_user_command($deviceId);
    if ($result=="[]"){
        die(get_result(
            0,
            "result_failure_get_command",
            "结果为空",
        ));
    }elseif ($result==null){
        die(get_result(
            0,
            "result_failure_get_command",
            "结果异常",
        ));
    }



    operate_database("w","admin_key",[
        "device_id" => $deviceId,
        "u_aim" => "effective",
        "u_data" => "1",
    ]);

    return [
        "states" => 1,
        "data" => $result
    ];
}

function fun_create_user_command($data,$uid,$key)
{
    $i=0;
    $ii = 0;//成功数
    if_admin_key($uid,$key);

    $data = json_decode($data,true);
    while ($code = $data){
        $i = $i+1;

        $ii = $ii+create_user_command($code['type'],$code['code'],$code['deviceId']);
    }

    return [
        "states" => 1,
        "data" => "创建了".$i."条，成功了".$ii."条，失败了".$i-$ii."条"
    ];
}

//回传指令的执行状态
function fun_upload_user_command($deviceId,$token,$commandId,$result)
{
    if_user_token($deviceId,$token);
    if (operate_database("r","user_command",json_encode(["id" => $commandId]))['device_id']!=$deviceId){
        die(get_result(
            0,
            "result_failure_upload_command",
            "设备不一",
        ));
    }

    $re = upload_user_command($deviceId,$commandId,$result);
    if (!$re){
        die(get_result(
            0,
            "result_failure_upload_command",
            "回传失败",
        ));
    }

    return [
        "states" => 1,
    ];
}

//返回成功或失败，成功则附加返回 key
function login_admin_user($uid,$password){
    if (!if_exist_admin_user($uid)){
        die(get_result(
            0,
            "result_failure_login_admin_user",
            "登录失败，账号不存在",
        ));
    }
    elseif ($password!=read_admin_user($uid)['password']){
        die(get_result(
            0,
            "result_failure_login_admin_user",
            "登录失败，密码错误",
        ));
    }

    $result = create_admin_key($uid);
    if (!$result){
        die(get_result(
            0,
            "result_failure_login_admin_user",
            "登录失败，无法申请key",
        ));
    }
    
    return [
        "states" => 1,
        "data" => $result,
    ];
}