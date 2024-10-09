<?php
include('../../../function.php');

if (!is_empty_request([$_REQUEST['deviceId'], $_REQUEST['token'], $_REQUEST['commandId'], $_REQUEST['result']])) {
    die(get_result(
        0,
        "result_failure_upload_command",
        "含空参",
    ));
}
//echo code_base64($_REQUEST['data'],"encode");
$result = fun_upload_user_command($_REQUEST['deviceId'], $_REQUEST['token'], $_REQUEST['commandId'], $_REQUEST['result']);
if ($result['states'])echo get_result($result['states'], "result_success_upload_command");
else echo get_result($result['states'], "result_failure_upload_command");