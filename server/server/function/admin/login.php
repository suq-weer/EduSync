<?php
include ("../../../function.php");

$uid = $_REQUEST['uid'];
$password = $_REQUEST['password'];
if(!is_empty_request([$uid,$password])){
    die(get_result(
        0,
        "result_failure_login_admin_user",
        "含空参",
    ));
}

$get_key = login_admin_user($uid,$password);
if ($get_key['states']) {
    echo get_result(
        1,
        "result_success_login_admin_user",
        $get_key['data'],
    );
}
else{
    echo get_result(
        0,
        "result_failure_login_admin_user",
        "数据库未响应",
    );
}