import base64
import json
import warnings

import requests
from requests import Response

from client.main import Network


class General:
    """
    需要从服务端获取的配置参数。
    """
    password_book: str = ""

    def input_password_book(self, network: Network):
        request: Response = requests.get(network.ip + network.resource)
        try:
            json_re = json.loads(request.content.decode())
            if json_re['states'] == 1:
                self.password_book = json_re['data']
                self.password_book = base64.b64decode(self.password_book.encode()).decode()
            else:
                warnings.warn("虽然已经建立对服务器的连接，但是服务器状态码为0。")
        except IOError:
            warnings.warn("服务器返回值不符合预期格式。返回值："+request.content.decode())
