interface ServerDeviceResponse {
  states: number
  msg: string
  data: [ ServerDeviceResponseDataItem ]
  total_list: number
}

interface ServerDeviceResponseDataItem {
  device_id: string
  time: number
  data: string
  notes: string
}

interface OnceDeviceData {
  CPUStatus: OnceDeviceCPUStatus
  MemoryStatus: OnceDeviceMemoryStatus
  DiskStatus: OnceDeviceDiskStatus
  SystemOutput: OnceDeviceSystemOutput
}

interface OnceDeviceCPUStatus {
  time: number
  count: number
  percent: number
  name: string
  architecture: string
}

interface OnceDeviceMemoryStatus {
  total: number
  used: number
}

interface OnceDeviceDiskStatus {
  total: number
  used: number
  name: string
  free: number
  percent: number
}

interface OnceDeviceSystemOutput {
  system: string
  version: string
}

interface DeviceStatus {
  device_id: string;
  device_system: string;
  device_time: string;
  device_cpu_usage: number;
  device_cpu_name: string;
  device_memory_usage: number;
  device_memory_total: number;
  device_disk_status: Array<{
    name: string;
    total: number;
    used: number;
    percent: number;
  }>;
}

export type { ServerDeviceResponse, ServerDeviceResponseDataItem, OnceDeviceData, OnceDeviceCPUStatus, OnceDeviceMemoryStatus, OnceDeviceDiskStatus, OnceDeviceSystemOutput, DeviceStatus }