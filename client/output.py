import socket

import psutil


class CpuStatusOutput:

    def __init__(self):
        """
        初始化该对象时会自动查询最新状态。
        """
        self.time = psutil.cpu_times()
        self.count = psutil.cpu_count(logical=False)
        self.percent = psutil.cpu_percent(interval=1, percpu=True)

    def output(self) -> dict:
        """
        将状态对象整理并返回。
        :return: 返回的CPU字典对象
        """
        root = {}
        output_time = {'system': self.time.system, 'user': self.time.user}
        root['time'] = output_time
        root['count'] = self.count
        root['percent'] = self.percent
        return root


class MemoryStatusOutput:
    def __init__(self):
        """
        初始化该对象时会自动查询最新状态。
        """
        self.virtual_memory = psutil.virtual_memory()

    def output(self) -> dict:
        """
        将状态对象整理并返回。
        :return: 返回的内存字典对象
        """
        root = {'total': self.virtual_memory.total, 'used': self.virtual_memory.free}
        return root


class DiskStatusOutput:
    def __init__(self):
        """
        初始化该对象时会自动查询最新状态。
        """
        self.disk_partitions = psutil.disk_partitions()

    def output(self) -> list:
        """
        将状态对象整理并返回。（注：未在工作中的驱动器会跳过整理。）
        :return: 返回的磁盘字典对象
        """
        root = []
        for i in range(len(self.disk_partitions)):
            try:
                usage = psutil.disk_usage(self.disk_partitions[i].device)
                once = {'name': self.disk_partitions[i].device, 'total': usage.total, 'used': usage.used,
                        'free': usage.free, 'percent': usage.percent}
                root.append(once)
            except IOError:
                pass
        return root


class UserOutput:
    def __init__(self, name: str):
        """
        初始化用户对象
        :param name: 用户名
        """
        self.meIP = socket.gethostbyname(socket.gethostname())
        self.name = name

    def output(self) -> dict:
        """
        将状态对象整理并返回。
        :return: 返回的用户字典对象
        """
        root = {'MeIP': self.meIP, 'name': self.name}
        return root


class StatusBusOutput:
    def __init__(self, cpu_status_output: CpuStatusOutput, memory_status_output: MemoryStatusOutput,
                 disk_status_output: DiskStatusOutput, user_output: UserOutput):
        """
        初始化该对象时需将状态输出流对象做参数。
        :param cpu_status_output: 引入CPU输出流信息
        :param memory_status_output: 引入内存输出流信息
        :param disk_status_output: 引入磁盘输出流信息
        :param user_output: 引入用户输出流信息
        """
        self.cpuStatusOutput = cpu_status_output.output()
        self.memoryStatusOutput = memory_status_output.output()
        self.diskStatusOutput = disk_status_output.output()
        self.user_output = user_output.output()

    def output(self) -> dict:
        """
        将状态对象整理并返回。
        :return: 返回的状态总线字典对象
        """
        root = {'CPUStatus': self.cpuStatusOutput, 'MemoryStatus': self.memoryStatusOutput,
                'DiskStatus': self.diskStatusOutput, 'UserOutput': self.user_output}
        return root
