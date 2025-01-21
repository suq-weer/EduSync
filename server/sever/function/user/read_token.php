<?php
include('../../../function.php');

if(!is_empty_request([$_REQUEST['type'],$_REQUEST['data']])){
    die(get_result(
        0,
        "result_failure_read_token",
        "含空参",
    ));
}
$result = fun_read_user_token($_REQUEST['type'],$_REQUEST['data']);
echo get_result($result['states'],"result_success_read_token",$result['data']);