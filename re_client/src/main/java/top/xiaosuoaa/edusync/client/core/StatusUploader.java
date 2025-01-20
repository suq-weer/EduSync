package top.xiaosuoaa.edusync.client.core;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class StatusUploader {
    private static final Logger LOGGER = LoggerFactory.getLogger(StatusUploader.class);
    private static Thread uploadThread;
    private static volatile boolean running;

    public void start() {
        if (running) {
            LOGGER.warn("StatusUploader is already running.");
            return;
        }
        running = true;
        uploadThread = new Thread(() -> {
            while (running) {
                try {
                    new AbstractComputer().uploadStatus();
                    Thread.sleep(5000);
                } catch (InterruptedException e) {
                    LOGGER.error("上传进程崩溃：", e);
                    break;
                } catch (Exception e) {
                    LOGGER.error("上传进程中发生了意料之外的结果：", e);
                }
            }
        });
        uploadThread.start();
    }

    public static void stop() {
        running = false;
        if (uploadThread != null) {
            uploadThread.interrupt();
        }
        LOGGER.info("上传进程已停止。");
    }
}