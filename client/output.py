import json
import platform
import socket

import psutil


class CpuStatusOutput:
    """
    CPU状态输出对象
    """
    def __init__(self):
        """
        初始化该对象时会自动查询最新状态。
        """
        self.time = psutil.cpu_times()
        self.count = psutil.cpu_count(logical=False)
        self.percent = psutil.cpu_percent(interval=1, percpu=True)
        self.processor = platform.processor()
        self.architecture = platform.architecture()

    def output(self) -> dict:
        """
        将状态对象整理并返回。
        :return: 返回的CPU字典对象
        """
        root = dict(count=self.count, percent=self.percent, processor=self.processor, architecture=self.architecture)
        output_time = {'system': self.time.system, 'user': self.time.user}
        root['time'] = output_time
        return root


class MemoryStatusOutput:
    """
    内存输出流对象。
    """
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
        root = dict(total=self.virtual_memory.total, used=self.virtual_memory.free)
        return root


class DiskStatusOutput:
    """
    磁盘输出流对象。
    """
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
                once = dict(name=self.disk_partitions[i].device, total=usage.total, used=usage.used, free=usage.free,
                            percent=usage.percent)
                root.append(once)
            except IOError:
                pass
        return root


class SystemOutput:
    """
    系统信息输出流对象。
    """
    def __init__(self):
        """
        初始化系统对象
        """
        self.system = platform.system()
        self.version = platform.version()

    def output(self) -> dict:
        """
        处理系统信息并返回字典对象。
        :return: 包含系统信息的字典。
        """
        root = dict(system=self.system, version=self.version)
        return root


class UserOutput:
    """
    用户输出对象。
    """
    def __init__(self):
        """
        初始化用户对象
        """
        self.meIP = socket.gethostbyname(socket.gethostname())

    def output(self) -> dict:
        """
        将状态对象整理并返回。
        :return: 返回的用户字典对象
        """
        root = dict(MeIP=self.meIP)
        return root


class StatusBusOutput:
    def __init__(self, cpu_status_output: CpuStatusOutput, memory_status_output: MemoryStatusOutput,
                 disk_status_output: DiskStatusOutput, system_output: SystemOutput, user_output: UserOutput):
        """
        初始化该对象时需将状态输出流对象做参数。
        :param cpu_status_output: 引入CPU输出流信息
        :param memory_status_output: 引入内存输出流信息
        :param disk_status_output: 引入磁盘输出流信息
        :param system_output: 引入系统输出流信息
        :param user_output: 引入用户输出流信息
        """
        self.cpuStatusOutput = cpu_status_output.output()
        self.memoryStatusOutput = memory_status_output.output()
        self.diskStatusOutput = disk_status_output.output()
        self.systemOutput = system_output.output()
        self.UserOutput = user_output.output()

    def output(self) -> dict:
        """
        将状态对象整理并返回。
        :return: 返回的状态总线字典对象
        """
        root = dict(format_version=1, CPUStatus=self.cpuStatusOutput, MemoryStatus=self.memoryStatusOutput,
                    DiskStatus=self.diskStatusOutput, SystemOutput=self.systemOutput, UserOutput=self.UserOutput)
        return root

    def output_to_json(self) -> str:
        return json.dumps(self.output())
