import json
import time
import uuid

from client.config import General
from client.event import Event
from client.network import Network, NetworkResource


class TokenInput:
    """
    接收服务器的Token并创建对象。
    """
    token: str = ""

    def __init__(self, general: General):
        if general.token == "" or general.token_is_out == True:
            print("refresh")
            self.query_token(general)
        else:
            self.token = general.token

    def query_token(self, general: General):
        password_book = general.password_book
        device_id: str = uuid.UUID(int=uuid.getnode()).__str__()
        response = Network(NetworkResource.GET_TOKEN).get(
            '?bookCode=' + password_book + '&device_id=' + device_id
        )
        self.token = response['data']
        general.token = self.token


class DataScanInput:
    def __init__(self, data: TokenInput, general: General, type_: str):
        self.data: str = data.token
        response = Network(NetworkResource.USE_TOKEN).get(
            '?type=' + type_ + '&data=' + self.data
        )
        self.output: dict = {}
        if response['error'] == 0:
            self.output = json.loads(
                response['data']
            )
            general.token_is_out = False
        else:
            general.token_is_out = True


# 测试用
class ScanEventTest(Event):
    def __init__(self, thread_id: int, name: str, counter: int):
        super().__init__(thread_id, name, counter)
        self.a = General()  # 密码本存储
        self.a.input_password_book(Network(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK))

    def run(self):
        while True:
            self.sleepTime = 10
            i = DataScanInput(TokenInput(self.a), self.a, "token")  # 将用密码本获取的Token放入数据检测API
            print(i.output)
            time.sleep(self.sleepTime)


if __name__ == '__main__':  # 放入密码本
    i = ScanEventTest(1, "Scan", 1)
    i.start()
