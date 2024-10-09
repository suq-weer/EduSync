<?php
include ("../../../function.php");

$bookCode = $_REQUEST['bookCode'];
$device_id = $_REQUEST['device_id'];
if(!is_empty_request([$bookCode,$device_id])){
    die(get_result(
        0,
        "result_failure_add_token",
        "含空参",
    ));
}

$get_token = get_token($bookCode,$device_id);
if ($get_token['states']) {
    echo get_result(
        1,
        "result_success_add_token",
        $get_token['data'],
    );
}
else{
    echo get_result(
        0,
        "result_failure_add_token",
        "数据库未响应",
    );
}