<?php
include('../../../function.php');

if (!is_empty_request([$_REQUEST['deviceId'], $_REQUEST['data'], $_REQUEST['token']])) {
    die(get_result(
        0,
        "result_failure_upload_device",
        "含空参",
    ));
}
//echo code_base64($_REQUEST['data'],"encode");
$result = fun_upload_user_device_notes($_REQUEST['deviceId'], $_REQUEST['data'], $_REQUEST['token']);
if ($result['states'])echo get_result($result['states'], "result_success_upload_device");
else echo get_result($result['states'], "result_failure_upload_device");