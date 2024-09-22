import threading
import time
import uuid

import output
from powershell import PowershellCommand
from input import commandDecode
from powershell import run
from config import General
from input import TokenInput
from network import NetworkResource, Network


def powershellCommandOutputUpload(input_command: list[PowershellCommand], device_id: int, token: TokenInput):
    """
    解析 ``PowershellCommand`` 列表并上传给服务器。
    :param input_command: 输入的 ``PowershellCommand`` 列表。
    :type input_command: list[PowershellCommand]
    :param device_id: 代码运行时的设备ID。
    :type device_id: int
    :param token: ``TokenInput`` 类，里面包含服务器 Token。
    :type token: TokenInput
    """
    for i in input_command:
        Network(NetworkResource.UPLOAD_COMMAND).get(
            "?deviceId=" + device_id.__str__() +
            "&token=" + token.token +
            "&commandId=" + i.id.__str__() +
            "&result=" + i.statusCode.__str__()
        )


class Event(threading.Thread):
    sleepTime = 0.0

    def __init__(self, thread_id: int, name: str, counter: int):
        """
        初始化事件线程。
        - 类成员变量：
            - ``sleepTime``—— 循环间隔。
        :param thread_id: 线程ID
        :param name: 线程名
        :param counter: 线程数量
        """
        threading.Thread.__init__(self)
        self.output = None
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        """
        继承该类时可以重写该函数以执行事件触发时的代码。
        """
        time.sleep(self.sleepTime)


class StatusUploadEvent(Event):
    def __init__(self, thread_id: int, name: str, counter: int):
        """
        新建一个设备状态上传线程。推荐用法 ``StatusUploadEvent(...).start()``

        - 类成员变量：
            - ``general``—— ``General`` 对象。
            - ``token``—— 顾名思义。
            - ``status``—— 状态码，改为1停止上传。
        :param thread_id: 线程ID（``threading`` 包）
        :type thread_id:
        :param name: 线程名（``threading`` 包）
        :type name:
        :param counter: 线程数？（``threading`` 包）
        :type counter:
        """
        super().__init__(thread_id, name, counter)
        self.general = General()
        self.general.input_password_book(Network(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK))
        self.token = TokenInput(self.general)
        self.status = 0

    def run(self):
        """
        设备上传逻辑，将主类成员变量 ``status`` 改为 1 停止上传。
        """
        while self.status == 0:
            self.sleepTime = 1
            device_id: int = uuid.UUID(int=uuid.getnode()).int
            bus_status = output.StatusBusOutput(output.CpuStatusOutput(), output.MemoryStatusOutput(),
                                                output.DiskStatusOutput(), output.SystemOutput())
            response_1 = Network(NetworkResource.UPLOAD_STATUS).post(
                "deviceId=" + device_id.__str__() +
                "&data=" + bus_status.output_to_json() +
                "&token=" + self.token.token
            )
            response_2 = Network(NetworkResource.CHECK_COMMAND).get(
                "?deviceId=" + device_id.__str__() +
                "&token=" + self.token.token
            )
            try:
                powershellCommandOutputUpload(run(commandDecode(response_2)), device_id, self.token)
            except KeyError:
                pass
            print(response_1, '\n', response_2)
            if response_1['error'] == 0 or response_2['error'] == 0:
                self.general.token_is_out = False
            else:
                self.general.token_is_out = True
            time.sleep(self.sleepTime)
