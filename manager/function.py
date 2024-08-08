import json

from manager.key import KeyInput
from manager.network import Network, NetworkResource
from manager.status import StatusInput


def outputStatus(token: str, device_id: str):
    status = StatusInput(token, device_id).outputBus()
    print(device_id + "的查询结果：")
    print("\t|-返回格式版本：", status.format_version)
    print("\t|-CPU情况：")
    print("\t\t|-CPU名字：", status.cpu_status.processor)
    print("\t\t|-CPU型号：", status.cpu_status.name)
    print("\t\t|-CPU核心数：", status.cpu_status.count)
    print("\t\t|-线程运行占用率：", status.cpu_status.percent)
    print("\t\t|-CPU系统内核名：", status.cpu_status.architecture)
    print("\t\t|-CPU运行时间：")
    print("\t\t\t|-用户操作时间：", status.cpu_status.time['user'])
    print("\t\t\t|-系统操作时间：", status.cpu_status.time['system'])
    print("\t|-内存情况（已使用/总共）：", status.memory_status.virtual_memory[0], "/",
          status.memory_status.virtual_memory[1])
    print("\t|-磁盘情况：")
    for i in range(len(status.disk_status.disk_partitions)):
        pan = status.disk_status.disk_partitions[i]
        print("\t\t|-盘符：", pan['name'])
        print("\t\t\t|-占用情况（已使用/空闲/总共/占用百分比）：", pan['used'], "/", pan['free'], "/", pan['total'], "/",
              pan['percent'], "%")
    print("\t|-系统信息：")
    print("\t\t|-名称：", status.rollback_system_status.system)
    print("\t\t|-版本：", status.rollback_system_status.version)


def postCommand(command: list, device_id: str, key: KeyInput):
    post_data = dict(code=command, deviceId=device_id)
    raw_data = json.dumps(post_data)
    response = Network(NetworkResource.POST_COMMAND).post('data='+raw_data+'&key='+key.key+'&uid='+key.uid)
    return response
