import json
import warnings
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

    def get(self, data: str):
        print(self.ip + self.resource + data)
        request: Response = requests.get(self.ip + self.resource + data)
        try:
            json_re = json.loads(request.content.decode())
            if json_re['states'] == 1:
                return json_re['data']
            else:
                warnings.warn("虽然已经建立对服务器的连接，但是服务器状态码为0。服务器警告："+json_re['msg']+"服务器附加原因："+json_re['data'])
        except IOError:
            warnings.warn("服务器返回值不符合预期格式。返回值：" + request.content.decode())


class NetworkResource:
    """
    服务端API资源映射。
    """

    def __init__(self):
        pass

    GET_INFO_SOFTWARE_CODEBOOK: str = "api/get_info_software_codeBook.php/"
    GET_TOKEN: str = "function/user/get_token.php"
