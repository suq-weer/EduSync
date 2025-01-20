package top.xiaosuoaa.edusync.client.core;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import oshi.SystemInfo;
import oshi.hardware.CentralProcessor;
import oshi.hardware.GlobalMemory;
import oshi.software.os.FileSystem;
import oshi.software.os.OSFileStore;
import oshi.software.os.OperatingSystem;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ServiceInfo {
    private static final Logger log = LoggerFactory.getLogger(ServiceInfo.class);
    private static final ExecutorService executor = Executors.newFixedThreadPool(4);

    private SystemInfo systemInfo;
    private CentralProcessor processor;
    private long cpuTime;
    private int cpuCount;
    private double cpuPercent;
    private String cpuName;
    private String cpuArchitecture;
    private GlobalMemory memory;
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
            log.error("Error collecting system information", e);
        }
    }

    private void collectCPUStatus() {
        processor = systemInfo.getHardware().getProcessor();
        long[] prevTicks = processor.getSystemCpuLoadTicks();
        try {
            TimeUnit.MILLISECONDS.sleep(500);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            log.warn("Interrupted during CPU status collection", e);
        }
        long[] ticks = processor.getSystemCpuLoadTicks();
        cpuTime = ticks[CentralProcessor.TickType.USER.getIndex()] - prevTicks[CentralProcessor.TickType.USER.getIndex()];
        cpuCount = processor.getLogicalProcessorCount();
        cpuPercent = processor.getSystemCpuLoadBetweenTicks(prevTicks) * 100;
        cpuName = processor.getProcessorIdentifier().getName();
        cpuArchitecture = processor.getProcessorIdentifier().getMicroarchitecture();
    }

    private void collectMemoryStatus() {
        memory = systemInfo.getHardware().getMemory();
        memoryTotal = memory.getTotal();
        memoryUsed = memoryTotal - memory.getAvailable();
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
            this.percent = used * 1.0 / total;
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
