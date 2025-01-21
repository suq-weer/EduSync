<?php
include("../../api.php");

$request_data = $_REQUEST;
//验证最高权限
if (!if_adminUser($request_data['admin_uid'],$request_data['admin_password'])) {
    die(get_result(0, "result_failure_if_adminUser"));
}

//执行
echo call_user_func_array($request_data['function'], json_decode($request_data['data'], true));