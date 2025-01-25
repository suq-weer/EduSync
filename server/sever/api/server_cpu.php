<?php
include("../../api.php");

$uid = $_REQUEST["uid"];
$key = $_REQUEST["key"];

//无效截断
if_admin_key($uid,$key);
$api = new bt_api();
$r_data = $api->GetInfo();

echo get_result(
    1,
    "result_success_get",
    $r_data,
);