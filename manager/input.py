import json
import uuid

from manager.config import General
from manager.network import NetworkResource, Network


class TokenInput:
    """
    接收服务器的Token并创建对象。
    """
    token: str = ""

    def __init__(self, general: General):
        if general.token == "" or general.token_is_out is True:
            print("refresh")
            self.query_token(general)
        else:
            self.token = general.token

    def query_token(self, general: General):
        password_book = general.password_book
        device_id: int = uuid.UUID(int=uuid.getnode()).int
        response = Network(NetworkResource.GET_TOKEN).get(
            '?bookCode=' + password_book + '&device_id=' + device_id.__str__()
        )
        print(response)
        self.token = json.loads(response['data'])['token']
        general.token = self.token
