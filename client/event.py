import threading
import time


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


"""
class StatusUploadEvent(Event):
    def __init__(self, thread_id: int, name: str, counter: int):
        super().__init__(thread_id, name, counter)
        self.general = General()
        self.general.input_password_book(Network(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK))
"""
