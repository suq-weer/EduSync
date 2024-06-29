import base64
import json
import warnings

import requests
from requests import Response

from client.main import Network


class General:
    password_book: str = ""

    def input_password_book(self, network: Network):
        request: Response = requests.get(network.ip + network.resource)
        json_re = json.loads(request.content.decode())
        if json_re['states'] == 1:
            self.password_book = json_re['data']
            self.password_book = base64.b64decode(self.password_book.encode()).decode()
        else:
            warnings.warn("Server no password book.")
