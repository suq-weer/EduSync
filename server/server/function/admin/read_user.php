<?php
include('../../../function.php');

if(!is_empty_request([['uid'],
    $_REQUEST['key']]
)){
    die(get_result(
        0,
        "result_failure_read_admin_user",
        "含空参",
    ));
}
$result = fun_read_admin_user($_REQUEST['uid'], $_REQUEST['key']);
echo get_result($result['states'],"result_success_read_admin_user",$result['data']);