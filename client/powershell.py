import subprocess


class PowerShellCommand:
    def __init__(self, command: str):
        self.popen = subprocess.getstatusoutput("powershell.exe " + command, encoding="UTF-8")
        self.statusCode = self.popen[0]
        self.output = self.popen[1]
