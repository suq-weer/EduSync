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
        memoryUsed = memory.getHeapMemoryUsage().getUsed();
        memoryTotal = memory.getHeapMemoryUsage().getMax();
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

    public JsonObject getJSONInfo() {
        systemInfo = new SystemInfo();

        JsonObject output = new JsonObject();

        JsonObject cpuInfo = new JsonObject();
        cpuInfo.addProperty("time", cpuTime);
        cpuInfo.addProperty("count", cpuCount);
        cpuInfo.addProperty("percent", cpuPercent);
        cpuInfo.addProperty("name", cpuName);
        cpuInfo.addProperty("architecture", cpuArchitecture);

        JsonObject memStatus = new JsonObject();
        memStatus.addProperty("total", memoryTotal);
        memStatus.addProperty("used", memoryUsed);

        JsonArray diskStatus = new JsonArray();
        for (OnceDisk onceDisk : diskInfo) {
            diskStatus.add(onceDisk.forJson());
        }

        JsonObject systemOutput = new JsonObject();
        systemOutput.addProperty("system", system);
        systemOutput.addProperty("version", systemVersion);

        output.add("CPUStatus", cpuInfo);
        output.add("MemoryStatus", memStatus);
        output.add("DiskStatus", diskStatus);
        output.add("SystemOutput", systemOutput);
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
