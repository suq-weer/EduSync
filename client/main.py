import psutil

class CpuStatusOutput:

    def __init__(self):
        self.time = psutil.cpu_times()
        self.count = psutil.cpu_count(logical=False)
        self.persent = psutil.cpu_percent(interval=1, percpu=True)

    def output(self) -> dict:
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
        self.virtual_memory = psutil.virtual_memory()

    def output(self) -> dict:
        root = {}
        root['total'] = self.virtual_memory.total
        root['used'] = self.virtual_memory.free
        return root


class DiskStatusOutput:
    def __init__(self):
        self.disk_partitions = psutil.disk_partitions()

    def output(self) -> list:
        root = []
        for i in range(len(self.disk_partitions)):
            usage = psutil.disk_usage(self.disk_partitions[i].device)
            once = {}
            once['total'] = usage.total
            once['used'] = usage.used
            once['free'] = usage.free
            once['persent'] = usage.percent
            root.append(once)
        return root

class StatusBusOutput:
    def __init__(self, cpuStatusOutput : CpuStatusOutput, memoryStatusOutput : MemoryStatusOutput):
        self.cpuStatusOutput = cpuStatusOutput.output()
        self.memoryStatusOutput = memoryStatusOutput.output()
        #self.diskStatusOutput = diskStatusOutput.output()

    def output(self) -> dict:
        root = {}
        root['CPUStatus'] = self.cpuStatusOutput
        root['MemoryStatus'] = self.memoryStatusOutput
        #root['DiskStatus'] = self.diskStatusOutput
        return root

class Network:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.host = '1145'

if __name__ == '__main__':
    cpu = CpuStatusOutput()
    mem = MemoryStatusOutput()
    allStatus = StatusBusOutput(cpu, mem)
    print(allStatus.output())
