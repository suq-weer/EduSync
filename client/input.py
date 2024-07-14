import json
import uuid

from client.config import General
from client.network import Network, NetworkResource


class TokenInput:
    """
    接收服务器的Token并创建对象。
    """
    token: str = ""

    def __init__(self, general: General):
        password_book = general.password_book
        device_id: str = uuid.UUID(int=uuid.getnode()).__str__()
        self.token = Network(NetworkResource.GET_TOKEN).get(
            '?bookCode=' + password_book + '&device_id=' + device_id
        )


class DataScanInput:
    def __init__(self, data: str, type_: str):
        self.data : str = data
        self.output : dict = json.loads(
            Network(NetworkResource.USE_TOKEN).get(
                '?type=' + type_ + '&data=' + self.data
            )
        )


if __name__ == '__main__':
    a = General()  # 密码本存储
    a.input_password_book(Network(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK))  # 放入密码本
    i = DataScanInput(TokenInput(a).token, "token")  # 将用密码本获取的Token放入数据检测API
    print(i.output)
