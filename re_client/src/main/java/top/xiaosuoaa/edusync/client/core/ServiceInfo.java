package top.xiaosuoaa.edusync.client.core;

import com.google.gson.JsonObject;
import oshi.SystemInfo;

import java.util.Arrays;

public class ServiceInfo {
	public SystemInfo systemInfo;

	public ServiceInfo() {
		systemInfo = new SystemInfo();
	}

	public SystemInfo getSystemInfo() {
		return systemInfo;
	}

	public JsonObject getJSONInfo() {
		JsonObject cPUInfo = new JsonObject();
		cPUInfo.addProperty("count", systemInfo.getHardware().getProcessor().getPhysicalProcessorCount());
		cPUInfo.addProperty("percent", Arrays.toString(systemInfo.getHardware().getProcessor().getProcessorCpuLoad(10)));

		JsonObject output = new JsonObject();
		output.add("CPUStatus", cPUInfo);
		return output;
	}
}
