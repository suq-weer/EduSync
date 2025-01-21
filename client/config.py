import base64

from network import Network, NetworkResource


class General:
    """
    需要从服务端获取的配置参数。
    """
    password_book: str = ""
    token: str = ""
    token_is_out: bool = False

    def input_password_book(self, network: Network):
        self.password_book = base64.b64decode(
            network.get(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK)['data'].encode()
        ).decode()
