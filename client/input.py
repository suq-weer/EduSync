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


if __name__ == '__main__':
    a = General()
    a.input_password_book(Network(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK))
    i = TokenInput(a)
    print(i.token)
