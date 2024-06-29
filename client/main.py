from client.output import *

if __name__ == '__main__':
    i = StatusBusOutput(CpuStatusOutput(), MemoryStatusOutput(), DiskStatusOutput(), SystemOutput(), UserOutput("Xiaosu"))
    print(i.output_to_json())
