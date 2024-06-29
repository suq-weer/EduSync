<?php
include("../../api.php");
echo get_result(1,"result_success_get",code_base64(get_info("system_codeBook","software"),"encode"));