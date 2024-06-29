import threading
import time

from client.network import Network


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

    def __todo(self):
        """
        继承该类时可以重写该函数以执行事件触发时的代码。
        """
        return self

    def run(self):
        """
        会自动调用__todo()函数
        """
        i = self.__todo()
        if i:
            self.output = i
        time.sleep(self.sleepTime)


class GetPasswordBookEvent(Event):
    """
    暂时弃用
    """

    def __init__(self, network: Network, thread_id: int, name: str, counter: int):
        super().__init__(thread_id, name, counter)
        self.network = network

    def __todo(self):
        self.sleepTime = 10.0
