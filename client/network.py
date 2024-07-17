import json
import time
import warnings
from json import JSONDecodeError

import requests
from requests import Response


class Network:
    """
    网络类定义。
    """

    def __init__(self, resource: str):
        """
        服务器网络基础配置
        :param resource: 对应服务端资源
        """
        self.ip = 'http://edusync619.yiyu14.top/server/'
        self.resource = resource

    def get(self, data: str) -> dict:
        print(self.ip + self.resource + data)
        request: Response = requests.get(self.ip + self.resource + data)
        # 不知道为什么Token获取会时不时发抽，只好堵塞线程。
        time.sleep(0.5)
        try:
            json_re = json.loads(request.content.decode())
            if json_re['states'] == 1:
                return {'data': json_re['data'], 'error': 0}
            else:
                print("虽然已经建立对服务器的连接，但是服务器状态码不为1。服务器附加原因："+json_re['data'])
                return {'error': 1}
        except (JSONDecodeError, IOError):
            warnings.warn("服务器返回值不符合预期格式。返回值：" + request.content.decode())
            return {'error': 2}

    def post(self, data: str) -> dict:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"}
        print(data)
        request: Response = requests.post(self.ip + self.resource, data, headers=headers)
        # 不知道为什么Token获取会时不时发抽，只好堵塞线程。
        time.sleep(0.5)
        try:
            json_re = json.loads(request.content.decode())
            if json_re['states'] == 1:
                return {'data': json_re['data'], 'error': 0}
            else:
                print("虽然已经建立对服务器的连接，但是服务器状态码不为1。服务器回复：" + str(json_re))
                return {'error': 1}
        except (JSONDecodeError, IOError):
            print("服务器返回值不符合预期格式。返回值：" + request.content.decode())
            return {'error': 2}


class NetworkResource:
    """
    服务端API资源映射。
    """

    def __init__(self):
        pass

    GET_INFO_SOFTWARE_CODEBOOK: str = "api/get_info_software_codeBook.php/"
    GET_TOKEN: str = "function/user/get_token.php"
    USE_TOKEN: str = "function/user/read_token.php"
    UPLOAD_STATUS: str = "function/user/upload_device.php"
