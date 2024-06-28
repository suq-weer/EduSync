<?php
include("config.php");
//获取配置信息
function get_info($aim,$type): string
{
    if($type=="software")
    {
        return info_software($aim);
    }
    elseif ($type=="server")
    {
        return info_server($aim);
    }
    return "";
}