import base64
import json

from manager.network import Network, NetworkResource


class CpuStatus:
    """
    CPU状态对象
    """

    time: dict
    count: int
    percent: list
    processor: str
    architecture: list

    def __init__(self, rawtext: dict):
        try:
            self.time = rawtext['time']
            self.count = rawtext['count']
            self.percent = rawtext['percent']
            self.processor = rawtext['processor']
            self.architecture = rawtext['architecture']
        except (json.JSONDecodeError, IOError):
            print("\033[91m[异常] 解析CPU状态时遇到错误")


class MemoryStatus:
    """
    内存状态对象。
    """

    virtual_memory: list

    def __init__(self, rawtext: dict):
        try:
            self.virtual_memory = [rawtext['used'], rawtext['total']]
        except (json.JSONDecodeError, IOError):
            print("\033[91m[异常] 解析内存状态时遇到错误")


class DiskStatus:
    """
    磁盘状态对象。
    """

    disk_partitions: list

    def __init__(self, rawtext: list):
        try:
            self.disk_partitions = rawtext
        except (json.JSONDecodeError, IOError):
            print("\033[91m[异常] 解析磁盘状态时遇到错误")


class RollbackSystemStatus:
    """
    系统信息对象。
    """

    system: str
    version: str

    def __init__(self, rawtext: dict):
        try:
            self.system = rawtext['system']
            self.version = rawtext['version']
        except (json.JSONDecodeError, IOError):
            print("\033[91m[异常] 解析被检测设备系统状态时遇到错误")


class StatusBus:
    format_version: int = 1

    def __init__(self, cpu_status: CpuStatus, memory_status: MemoryStatus, disk_status: DiskStatus,
                 rollback_system_status: RollbackSystemStatus):
        self.cpu_status = cpu_status
        self.memory_status = memory_status
        self.disk_status = disk_status
        self.rollback_system_status = rollback_system_status


class StatusInput:
    device_id: int
    time: int
    data: dict

    def __init__(self, token: str, device_id: str):
        raw_status = Network(NetworkResource.READ_STATUS).get("?deviceId=" + device_id + "&token=" + token)
        self.device_id = json.loads(raw_status['data'])['device_id']
        self.time = json.loads(raw_status['data'])['time']
        raw_data: str = json.loads(raw_status['data'])['data']
        self.data = json.loads(base64.b64decode(raw_data.encode()).decode())

    def outputBus(self) -> StatusBus:
        return StatusBus(CpuStatus(self.data['CPUStatus']), MemoryStatus(self.data['MemoryStatus']),
                         DiskStatus(self.data['DiskStatus']), RollbackSystemStatus(self.data['SystemOutput']))
