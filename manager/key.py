from manager.network import Network, NetworkResource


class KeyInput:
    def __init__(self, uid: str, password: str):
        self.uid = uid
        self.key = Network(NetworkResource.LOGIN).get("?uid=" + uid + "&password=" + password)['data']
        print(self.key)
