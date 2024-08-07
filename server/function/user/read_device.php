<?php
include('../../../function.php');
//$deviceId,$token

if(!is_empty_request([$_REQUEST['deviceId'],$_REQUEST['token']])){
    die(get_result(
        0,
        "result_failure_read_device",
        "含空参",
    ));
}
$result = fun_read_user_device($_REQUEST['deviceId'],$_REQUEST['token']);
echo get_result($result['states'],"result_success_read_device",$result['data']);