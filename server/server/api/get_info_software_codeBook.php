<?php
include("../../api.php");
echo json(1,"获取成功",code_base64(get_info("system_codeBook","software"),"encode"));