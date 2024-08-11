from manager.config import General
from manager.input import TokenInput
from manager.key import KeyInput
from manager.network import Network, NetworkResource
from manager.function import outputStatus, postCommand

general = General()
general.input_password_book(Network(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK))
# key = KeyInput("Xiaosu", "0189191415411")
key = KeyInput("xiaoyi", "xiaoyi..")
token = TokenInput(general).token
device_id = input("device_id: ")
outputStatus(token, device_id)
command = []
while True:
    once = input("指令（输入T以终止多指令）： ")
    if once == "T":
        break
    else:
        command.append(once)
postCommand(command, device_id, key)