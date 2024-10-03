<?php
include('../../../function.php');
//$deviceId,$token

if(!is_empty_request([$_REQUEST['deviceId'],$_REQUEST['token']])){
    die(get_result(
        0,
        "result_failure_get_command",
        "含空参",
    ));
}
$result = fun_get_user_command($_REQUEST['deviceId'],$_REQUEST['token']);
echo get_result($result['states'],"result_success_get_command",$result['data']);