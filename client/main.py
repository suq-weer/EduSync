import psutil
import socket
import threading
import time

class Event(threading.Thread):
    sleepTime = 0.0
    
    def __init__(self, threadID : int, name : str, counter : int):
        """初始化事件线程

        Args:
            threadID (int): 线程ID
            name (str): 线程名
            counter (int): 线程数量
        """
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def __TODO(self):
        pass
    
    def run(self):
        self.__TODO()
        time.sleep(self.sleepTime)
        

class CpuStatusOutput:

    def __init__(self):
        """初始化该对象时会自动查询最新状态。
        """
        self.time = psutil.cpu_times()
        self.count = psutil.cpu_count(logical=False)
        self.persent = psutil.cpu_percent(interval=1, percpu=True)

    def output(self) -> dict:
        """将状态对象整理并返回。

        Returns:
            dict: 返回的状态字典
        """
        root = {}
        outputTime = {}
        outputTime['system'] = self.time.system
        outputTime['user'] = self.time.user
        root['time'] = outputTime
        root['count'] = self.count
        root['persent'] = self.persent
        return root


class MemoryStatusOutput:
    def __init__(self):
        """初始化该对象时会自动查询最新状态。
        """
        self.virtual_memory = psutil.virtual_memory()

    def output(self) -> dict:
        """将状态对象整理并返回。

        Returns:
            dict: 返回的状态字典
        """
        root = {}
        root['total'] = self.virtual_memory.total
        root['used'] = self.virtual_memory.free
        return root


class DiskStatusOutput:
    def __init__(self):
        """初始化该对象时会自动查询最新状态。
        """
        self.disk_partitions = psutil.disk_partitions()

    def output(self) -> list:
        """将状态对象整理并返回。（注：未在工作中的驱动器会跳过整理。）

        Returns:
            dict: 返回的状态字典
        """
        root = []
        for i in range(len(self.disk_partitions)):
            try:
                usage = psutil.disk_usage(self.disk_partitions[i].device)
                once = {}
                once['name'] = self.disk_partitions[i].device
                once['total'] = usage.total
                once['used'] = usage.used
                once['free'] = usage.free
                once['persent'] = usage.percent
                root.append(once)
            except:
                pass
        return root
    
class UserOutput:
    def __init__(self, cpuStatus : CpuStatusOutput, memStatus : MemoryStatusOutput, name : str):
        """初始化用户对象

        Args:
            cpuStatus (CpuStatusOutput): CPU状态输出流
            memStatus (MemoryStatusOutput): 内存状态输出流
            name (str): 用户名
        """
        self.cpuStatus = cpuStatus
        self.meIP = socket.gethostbyname(socket.gethostname())
        self.memStatus = memStatus
    
    def output(self) -> dict:
        """将状态对象整理并返回。

        Returns:
            dict: 返回的状态字典
        """
        root = {}
        root['CPUStatus'] = self.cpuStatus.output()
        root['MeIP'] = self.meIP
        root['MemoryStatus'] = self.memStatus.output()
        return root

class StatusBusOutput:
    def __init__(self, cpuStatusOutput : CpuStatusOutput, memoryStatusOutput : MemoryStatusOutput, diskStatusOutput : DiskStatusOutput, userOutput : UserOutput):
        """初始化该对象时需将状态输出流对象做参数。
        """
        self.cpuStatusOutput = cpuStatusOutput.output()
        self.memoryStatusOutput = memoryStatusOutput.output()
        self.diskStatusOutput = diskStatusOutput.output()

    def output(self) -> dict:
        """将状态对象整理并返回。

        Returns:
            dict: 返回的状态字典
        """
        root = {}
        root['CPUStatus'] = self.cpuStatusOutput
        root['MemoryStatus'] = self.memoryStatusOutput
        root['DiskStatus'] = self.diskStatusOutput
        return root
    
class TokenInput:
    def __init__(self, id : str, ip : str, time : float, token : str):
        """初始化服务器发送的Token对象。

        Args:
            id (str): 服务器对应的‘id’字段
            ip (str): 服务器对应的‘ip’字段
            time (float): 服务器发送的时间戳
            token (str): 服务器发送的‘Token’字段
        """
        self.ip = ip
        self.id = id
        self.time = time
        self.token = token

class Network:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.host = '1145'
        
class ConnectEvent(Event):
    def __TODO(self):
        self.sleepTime = 10.0
        return super().__TODO()

if __name__ == '__main__':
    pass
