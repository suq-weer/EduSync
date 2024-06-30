import base64

from client.network import Network


class General:
    """
    需要从服务端获取的配置参数。
    """
    password_book: str
    token: str

    def input_password_book(self, network: Network):
        self.password_book = base64.b64decode(network.get("").encode()).decode()
