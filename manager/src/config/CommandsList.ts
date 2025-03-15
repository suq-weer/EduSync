import Windows_commandList from '@/assets/config/Windows_commandList.json'
import Linux_commandList from '@/assets/config/Linux_commandList.json'

function CommandsList(system:string){
  if (system=='Linux') return Linux_commandList
  else if (system=='Windows') return Windows_commandList
}

export { CommandsList }