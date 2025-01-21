import json
import time
import warnings
from json import JSONDecodeError

import requests
from requests import Response


class Network:
    """
    网络类定义。分为 ``get()`` 与 ``post()``
    """

    def __init__(self, resource: str):
        """
        服务器网络基础配置
        :param resource: 对应服务端资源
        """
        self.ip = 'http://edusync619.yiyu14.top/server/'
        self.resource = resource

    def get(self, data: str) -> dict:
        """
        网络模块 GET 方法。
        :param data: 要提交的数据，采用 ``application/x-www-form-urlencoded`` 请求头。
        :type data: str
        :return: 服务端的返回JSON（自动转字典）。
        :rtype: dict
        """
        print(self.ip + self.resource + data)
        request: Response = requests.get(self.ip + self.resource + data)
        # 不知道为什么Token获取会时不时发抽，只好堵塞线程。
        time.sleep(1)
        try:
            json_re = json.loads(request.content.decode())
            if json_re['states'] == 1:
                return {'data': json_re['data'], 'error': 0}
            else:
                print("虽然已经建立对服务器的连接，但是服务器状态码不为1。服务器附加原因：" + json_re['data'])
                return {'error': 1}
        except (JSONDecodeError, IOError):
            warnings.warn("服务器返回值不符合预期格式。返回值：" + request.content.decode())
            return {'error': 2}

    def post(self, data: str) -> dict:
        """
        网络模块的GET请求函数。
        :param data: 发送的数据，采用 ``application/x-www-form-urlencoded`` 请求头。
        :type data: str
        :return: 返回的 ``JSON`` 数据（自动转字典）。
        :rtype: dict
        """
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

    def __init__(self):
        """
        服务端API资源映射。

        - 类成员变量：
            - ``GET_INFO_SOFTWARE_CODEBOOK``
            - ``GET_TOKEN``
            - ``USE_TOKEN``
            - ``UPLOAD_STATUS``
            - ``CHECK_COMMAND``
            - ``READ_TOKEN``
        """
        pass

    GET_INFO_SOFTWARE_CODEBOOK: str = "api/get_info_software_codeBook.php/"
    GET_TOKEN: str = "function/user/get_token.php"
    USE_TOKEN: str = "function/user/read_token.php"
    UPLOAD_STATUS: str = "function/user/upload_device.php"
    CHECK_COMMAND: str = "function/user/get_command.php"
    READ_TOKEN: str = "function/adminr/read_token.php"
    UPLOAD_COMMAND: str = "function/user/upload_command.php"
