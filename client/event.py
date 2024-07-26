import threading
import time
import uuid

import output
from client.config import General
from client.input import TokenInput
from client.network import NetworkResource, Network


class Event(threading.Thread):
    """
    事件基础类
    """
    sleepTime = 0.0

    def __init__(self, thread_id: int, name: str, counter: int):
        """
        初始化事件线程
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
        super().__init__(thread_id, name, counter)
        self.general = General()
        self.general.input_password_book(Network(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK))
        self.token = TokenInput(self.general)

    def run(self):
        while True:
            self.sleepTime = 1
            device_id: int = uuid.UUID(int=uuid.getnode()).int
            bus_status = output.StatusBusOutput(output.CpuStatusOutput(), output.MemoryStatusOutput(),
                                                output.DiskStatusOutput(), output.SystemOutput(), output.UserOutput())
            dict_post = dict(deviceId=device_id, data=bus_status.output(), token=self.token.token)
            response_1 = Network(NetworkResource.UPLOAD_STATUS).post(
                "deviceId=" + device_id.__str__() +
                "&data=" + bus_status.output_to_json() +
                "&token=" + self.token.token
            )
            if response_1['error'] == 0:
                self.general.token_is_out = False
            else:
                print(response_1)
                self.general.token_is_out = True
            response_2 = Network(NetworkResource.CHECK_COMMAND).get(
                "deviceId=" + device_id.__str__()
            )
            time.sleep(self.sleepTime)
