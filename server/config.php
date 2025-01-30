<?php
//配置信息
function info_server($aim): string//后端
{
    $data = [
        //域名
        "domain_main" => "http://edusync.yiyu14.top/",//主域名
        "domain_sub" => "http://edusync.yiyu14.top/",//运行目录

        //代码级权限用户
        "admin_uid" => "xiaoyi",
        "admin_password" => "xiaoyi..",

        //数据库
        "database_servername" => "localhost",
        "database_username" => "edusync",
        "database_password" => "xiaoyi..",
        "database_dbname" => "edusync",

        //输出
        "result_success_get" => "获取成功",
        "result_failure_if_adminUser" => "最高权限用户信息错误",
        "result_success_add_token" => "申请token成功",
        "result_failure_add_token" => "申请token失败",
        "result_failure_read_token" => "读取token失败",
        "result_success_read_token" => "读取token成功",
        "result_failure_upload_device" => "上传设备信息失败",
        "result_success_upload_device" => "上传设备信息成功",
        "result_failure_read_device" => "读取设备信息失败",
        "result_success_read_device" => "读取设备信息成功",
        "result_success_get_command" => "读取指令成功",
        "result_failure_get_command" => "读取指令失败",
        "result_success_create_command" => "创建指令成功",
        "result_failure_create_command" => "创建指令失败",
        "result_success_login_admin_user" => "登录管理员成功",
        "result_failure_login_admin_user" => "登录管理员失败",
        "result_success_read_admin_key" => "读取key成功",
        "result_failure_read_admin_key" => "读取key失败",
        "result_success_upload_command" => "回传指令成功",
        "result_failure_upload_command" => "回传指令失败",
        "result_success_get_list_device" => "获取设备列表成功",
        "result_failure_get_list_device" => "获取设备列表失败",
    ];
    return $data[$aim];
}
function info_software($aim): string//软件
{
    $data = [

        //系统信息
        "system_codeBook" => "Edusync619!",//密码本

        //token or key
        "user_token_effectiveDuration" => 180,//3 min
        "admin_key_etffectiveDuraion" => 600,//10 min

    ];
    return $data[$aim];
}


class bt_api {
    //服务器参数
    private $BT_KEY = "xV75F0DuY30EG5CAoq69kRGveu3lOzZP";  //接口密钥
    private $BT_PANEL = "https://154.12.40.63:38042";	   //面板地址

    //如果希望多台面板，可以在实例化对象时，将面板地址与密钥传入
    public function __construct($bt_panel = null,$bt_key = null){
        if($bt_panel) $this->BT_PANEL = $bt_panel;
        if($bt_key) $this->BT_KEY = $bt_key;
    }

    //示例取面板日志
    public function GetLogs(){
        //拼接URL地址
        $url = $this->BT_PANEL.'/data?action=getData';

        //准备POST数据
        $p_data = $this->GetKeyData();		//取签名
        $p_data['table'] = 'logs';
        $p_data['limit'] = 10;
        $p_data['tojs'] = 'test';

        //请求面板接口
        $result = $this->HttpPostCookie($url,$p_data);

        //解析JSON数据
        $data = json_decode($result,true);
        return $data;
    }


    public function GetInfo(){
        //拼接URL地址
        $url = $this->BT_PANEL.'/system?action=GetSystemTotal';

        //准备POST数据
        $p_data = $this->GetKeyData();		//取签名
        $p_data['table'] = 'logs';
        $p_data['limit'] = 10;
        $p_data['tojs'] = 'test';

        //请求面板接口
        $result = $this->HttpPostCookie($url,$p_data);

        //解析JSON数据
        $data = json_decode($result,true);
        return $data;
    }


    /**
     * 构造带有签名的关联数组
     */
    private function GetKeyData(){
        $now_time = time();
        $p_data = array(
            'request_token'	=>	md5($now_time.''.md5($this->BT_KEY)),
            'request_time'	=>	$now_time
        );
        return $p_data;
    }


    /**
     * 发起POST请求
     * @param String $url 目标网填，带http://
     * @param Array|String $data 欲提交的数据
     * @return string
     */
    private function HttpPostCookie($url, $data,$timeout = 60)
    {
        //定义cookie保存位置
        $cookie_file='./'.md5($this->BT_PANEL).'.cookie';
        if(!file_exists($cookie_file)){
            $fp = fopen($cookie_file,'w+');
            fclose($fp);
        }

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        curl_setopt($ch, CURLOPT_COOKIEJAR, $cookie_file);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookie_file);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        $output = curl_exec($ch);
        curl_close($ch);
        return $output;
    }
}