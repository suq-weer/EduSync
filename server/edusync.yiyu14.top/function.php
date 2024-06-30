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