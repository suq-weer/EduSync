function CommandsList(system:string){
  const Linux_commandList = [
    {
      "name":"关机",
      "command":"shutdown"
    },
    {
      "name":"重启",
      "command":"reboot"
    },]

  const Windows_commandList = [
    {
      "name":"关机",
      "command":"Stop-Computer -Delay 2"
    },
    {
      "name":"重启",
      "command":"Restart-Computer -Delay 2"
    },]

  if (system=='Linux') return Linux_commandList
  else if (system=='Windows') return Windows_commandList
}

export { CommandsList }