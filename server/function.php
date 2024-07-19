<?php
include("api.php");

//申请token
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
        "data" => $result
    ];
}

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
        "data" => $result
    ];
}