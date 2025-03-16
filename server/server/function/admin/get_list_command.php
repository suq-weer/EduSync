<?php
include('../../../function.php');

if(!is_empty_request([$_REQUEST['page'],$_REQUEST['length'],$_REQUEST['uid'],$_REQUEST['key']])){
    die(get_result(
        0,
        "result_failure_get_list_command",
        "含空参",
    ));
}
$result = fun_get_list_command($_REQUEST['data'],$_REQUEST['value'],$_REQUEST['page'],$_REQUEST['length'],$_REQUEST['uid'],$_REQUEST['key']);
echo get_result($result['states'],"result_success_get_list_command",$result['data'][$_REQUEST['page']],$result['data']['total_list']);