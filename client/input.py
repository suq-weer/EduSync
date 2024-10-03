import json
import uuid

from config import General
from network import Network, NetworkResource


class TokenInput:
    token: str = ""

    def __init__(self, general: General):
        """
        接收服务器的Token并创建对象。

        - 类成员变量：
            - ``token``—— 顾名思义。
        :param general: 输入的 ``General`` 对象。
        :type general: General
        """
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
        """
        暂弃。
        :param data:
        :type data:
        :param general:
        :type general:
        :param type_:
        :type type_:
        """
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


def commandDecode(raw_refuse: dict)->list:
    """
    将服务器返回内容解析成 ``CommandInput`` 列表。
    :param raw_refuse: 服务器返回内容
    :type raw_refuse: dict
    :return: 返回的 ``CommandInput`` 列表。
    :rtype: list
    """
    re = []
    for i in raw_refuse['data']:
        re.append(CommandInput(i))
    return re


class CommandInput:
    def __init__(self, raw_command: dict):
        self.code: str = raw_command['code']
        self.type: int = raw_command['type']
        self.id: int = raw_command['id']