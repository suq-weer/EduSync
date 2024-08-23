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
        print("refresh")
        self.query_token(general)

    def query_token(self, general: General):
        password_book = general.password_book
        device_id: int = uuid.UUID(int=uuid.getnode()).int
        response = Network(NetworkResource.GET_TOKEN).get(
            '?bookCode=' + password_book + '&device_id=' + device_id.__str__()
        )
        self.token = response['data']
        general.token = self.token
        if general.token == "" or general.token_is_out is True:
            print("refresh")
            self.query_token(general)


class DataScanInput:
    def __init__(self, data: str, general: General, type_: str):
        self.data: str = data
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
