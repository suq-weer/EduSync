package top.xiaosuoaa.edusync.client.core;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import oshi.SystemInfo;
import oshi.hardware.CentralProcessor;
import oshi.software.os.FileSystem;
import oshi.software.os.OSFileStore;
import oshi.software.os.OperatingSystem;

import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.TimeUnit;

public class ServiceInfo {
	private static final Logger LOGGER = LoggerFactory.getLogger(ServiceInfo.class);

	private SystemInfo systemInfo;

	public SystemInfo getSystemInfo() {
		return systemInfo;
	}

	public CentralProcessor getProcessor() {
		return processor;
	}

	public int getCpuCount() {
		return cpuCount;
	}

	public String getCpuArchitecture() {
		return cpuArchitecture;
	}

	public String getSystem() {
		return system;
	}

	public List<OnceDisk> getDiskInfo() {
		return diskInfo;
	}

	public long getCpuTime() {
		return cpuTime;
	}

	public double getCpuPercent() {
		return cpuPercent;
	}

	public String getCpuName() {
		return cpuName;
	}

	public MemoryMXBean getMemory() {
		return memory;
	}

	public long getMemoryTotal() {
		return memoryTotal;
	}

	public long getMemoryUsed() {
		return memoryUsed;
	}

	public OperatingSystem getOperatingSystem() {
		return operatingSystem;
	}

	public String getSystemVersion() {
		return systemVersion;
	}

	private CentralProcessor processor;
	private long cpuTime;
	private int cpuCount;
	private double cpuPercent;
	private String cpuName;
	private String cpuArchitecture;
	private MemoryMXBean memory;
	private long memoryTotal;
	private long memoryUsed;
	private OperatingSystem operatingSystem;
	private List<OnceDisk> diskInfo;
	private String system;
	private String systemVersion;

	public static final int FORMAT_VERSION = 2;

	public ServiceInfo() {
		this.systemInfo = new SystemInfo();
		collectSystemInfo();
	}

	private void collectSystemInfo() {
		try {
			collectCPUStatus();
			collectMemoryStatus();
			collectDiskStatus();
			collectSystemStatus();
		} catch (Exception e) {
			LOGGER.error("Error collecting system information", e);
		}
	}

	private void collectCPUStatus() {
		processor = systemInfo.getHardware().getProcessor();
		long[] prevTicks = processor.getSystemCpuLoadTicks();
		try {
			TimeUnit.MILLISECONDS.sleep(500);
		} catch (InterruptedException e) {
			Thread.currentThread().interrupt();
			LOGGER.warn("Interrupted during CPU status collection", e);
		}
		long[] ticks = processor.getSystemCpuLoadTicks();
		cpuTime = ticks[CentralProcessor.TickType.USER.getIndex()] - prevTicks[CentralProcessor.TickType.USER.getIndex()];
		cpuCount = processor.getLogicalProcessorCount();
		cpuPercent = processor.getSystemCpuLoadBetweenTicks(prevTicks) * 100;
		cpuName = processor.getProcessorIdentifier().getName();
		cpuArchitecture = processor.getProcessorIdentifier().getMicroarchitecture();
	}

	private void collectMemoryStatus() {
		memory = ManagementFactory.getMemoryMXBean();
		memoryUsed = memory.getNonHeapMemoryUsage().getUsed();
		memoryTotal = memory.getNonHeapMemoryUsage().getMax();
	}

	private void collectDiskStatus() {
		operatingSystem = systemInfo.getOperatingSystem();
		FileSystem fileSystem = operatingSystem.getFileSystem();
		List<OSFileStore> fileStores = fileSystem.getFileStores();
		diskInfo = new ArrayList<>();
		for (OSFileStore fileStore : fileStores) {
			diskInfo.add(new OnceDisk(fileStore));
		}
	}

	private void collectSystemStatus() {
		system = operatingSystem.getFamily();
		systemVersion = operatingSystem.getVersionInfo().getVersion();
	}

	/**
	 * 获取系统信息的JSON表示
	 * 此方法收集系统CPU、内存、磁盘和系统输出信息，并将其组织成一个JsonObject返回
	 *
	 * @return JsonObject 包含系统信息的JSON对象
	 */
	public JsonObject getJSONInfo() {
	    // 实例化系统信息对象
	    systemInfo = new SystemInfo();
	    // 创建一个JsonObject来存储所有系统信息
	    JsonObject output = new JsonObject();
	    // 创建并填充CPU信息
	    JsonObject cpuInfo = new JsonObject();
	    cpuInfo.addProperty("time", cpuTime);
	    cpuInfo.addProperty("count", cpuCount);
	    cpuInfo.addProperty("percent", cpuPercent);
		//warn: name被要求改成processor
	    cpuInfo.addProperty("processor"/*"name"*/, cpuName);
	    cpuInfo.addProperty("architecture", cpuArchitecture);
	    // 创建并填充内存状态
	    JsonObject memStatus = new JsonObject();
	    memStatus.addProperty("total", memoryTotal);
	    memStatus.addProperty("used", memoryUsed);
	    // 创建磁盘状态数组，并遍历每个磁盘信息添加到数组中
	    JsonArray diskStatus = new JsonArray();
	    for (OnceDisk onceDisk : diskInfo) {
	        diskStatus.add(onceDisk.forJson());
	    }
	    // 创建并填充系统输出信息
	    JsonObject systemOutput = new JsonObject();
	    systemOutput.addProperty("system", system);
	    systemOutput.addProperty("version", systemVersion);

		// 存放格式版本
		output.addProperty("format_version", FORMAT_VERSION);
	    // 将CPU、内存、磁盘和系统输出信息添加到输出对象中
	    output.add("CPUStatus", cpuInfo);
	    output.add("MemoryStatus", memStatus);
	    output.add("DiskStatus", diskStatus);
	    output.add("SystemOutput", systemOutput);
	    // 返回包含所有系统信息的JSON对象
	    return output;
	}

	public static class OnceDisk {
		private final OSFileStore osFileStore;

		public String getName() {
			return name;
		}

		public long getTotal() {
			return total;
		}

		public long getUsed() {
			return used;
		}

		public long getFree() {
			return free;
		}

		public double getPercent() {
			return percent;
		}

		private final String name;
		private final long total;
		private final long used;
		private final long free;
		private final double percent;

		public OnceDisk(OSFileStore fs) {
			this.osFileStore = fs;
			this.name = fs.getName();
			this.total = fs.getTotalSpace();
			this.free = fs.getUsableSpace();
			this.used = total - free;
			double percent = used * 1.0 / total;
			this.percent = Double.isNaN(percent) ? 0 : percent;
		}

		public JsonObject forJson() {
			JsonObject output = new JsonObject();
			output.addProperty("name", Objects.requireNonNullElse(name, "null"));
			output.addProperty("total", total);
			output.addProperty("used", used);
			output.addProperty("free", free);
			output.addProperty("percent", percent);
			return output;
		}

		public OSFileStore getOsFileStore() {
			return osFileStore;
		}
	}
}
