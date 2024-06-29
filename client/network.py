class Network:
    def __init__(self, resource: str):
        """
        服务器网络基础配置
        :param resource: 对应服务端资源
        """
        self.ip = 'http://edusync619.yiyu14.top/server/api/'
        self.resource = resource


class NetworkResource:
    """
    服务端API资源映射。
    """
    GET_INFO_SOFTWARE_CODEBOOK: str = "get_info_software_codeBook.php/"
