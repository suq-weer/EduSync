from client.network import Network


class TokenInput:
    """
    接收服务器的Token并创建对象。
    """
    def __init__(self, id: str, ip: Network, time: float, token: str):
        """
        初始化服务器发送的Token对象。
        :param id: 服务端字段
        :param ip: 设备当前IP
        :param time: 设备当前时间戳
        :param token: 服务端请求Token
        """
        self.ip = ip
        self.id = id
        self.time = time
        self.token = token