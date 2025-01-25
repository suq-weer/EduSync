<?php
include("../../api.php");

$uid = $_REQUEST["uid"];
$key = $_REQUEST["key"];

//无效截断
if_admin_key($uid,$key);

//有效输出
echo get_result(
    1,
    "result_success_get",
    "该key有效",
);