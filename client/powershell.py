import subprocess

from input import CommandInput


class PowershellCommand:
    def __init__(self, command: CommandInput):
        """
        Powershell 运行命令抽象。

        - 类成员变量：
            - ``popen``—— 即 ``subprocess.getstatusoutput()`` 的返回内容。
            - ``statusCode``—— 状态码。
            - ``output``—— 输出结果。
            - ``id``—— 指令ID。
        :param command: 单个指令内容，自动补充成 [``powershell.exe <CommandInput.code>``]。编码：``UTF-8``
        :type command: str
        """
        self.popen = subprocess.getstatusoutput(command.code, encoding="UTF-8")
        self.statusCode = self.popen[0]
        self.output = self.popen[1]
        self.id = command.id

def run(command: list) -> list:
    """
    根据 ``CommandInput`` 列表构建多个 ``PowershellCommand`` 对象，并组成列表返回。
    :param command: 需运行的 ``CommandInput`` 列表。
    :type command: str
    :return: 返回的 ``PowershellCommand`` 列表。
    :rtype: list
    """
    c_list = []
    for i in command:
        c_list.append(PowershellCommand(i))
    return c_list
