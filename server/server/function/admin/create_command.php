<?php
include('../../../function.php');
//$deviceId,$token

if(!is_empty_request([$_REQUEST['data'],$_REQUEST['uid'],$_REQUEST['key']])){
    die(get_result(
        0,
        "result_failure_create_command",
        "含空参",
    ));
}
$result = fun_create_user_command($_REQUEST['data'],$_REQUEST['uid'],$_REQUEST['key']);
echo get_result($result['states'],"result_success_create_command",$result['data']);