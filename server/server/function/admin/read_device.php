<?php
include('../../../function.php');

if(!is_empty_request([$_REQUEST['deviceId'],
    $_REQUEST['uid'],
    $_REQUEST['key']]
)){
    die(get_result(
        0,
        "result_failure_admin_read_device",
        "含空参",
    ));
}
$result = fun_admin_read_device($_REQUEST['uid'], $_REQUEST['key'], $_REQUEST['deviceId']);
echo get_result($result['states'],"result_success_admin_read_device",$result['data']);