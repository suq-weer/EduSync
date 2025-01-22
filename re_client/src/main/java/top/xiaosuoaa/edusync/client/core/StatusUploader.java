package top.xiaosuoaa.edusync.client.core;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import top.xiaosuoaa.edusync.client.HomeApplication;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class StatusUploader {
	private static final Logger LOGGER = LoggerFactory.getLogger(StatusUploader.class);
	private static ScheduledExecutorService scheduler;
	public static volatile boolean running;

	public void start() {
		if (running) {
			LOGGER.warn("StatusUploader is already running.");
			return;
		}
		running = true;
		scheduler = Executors.newSingleThreadScheduledExecutor();
		scheduler.scheduleAtFixedRate(() -> {
			try {
				new AbstractComputer().sync();
			} catch (Exception e) {
				HomeApplication.showError("上传进程中发生了意料之外的结果：", e, LOGGER);
			}
		}, 0, 5, TimeUnit.SECONDS);
		LOGGER.info("上传进程已启动。");
	}

	public static void stop() {
		running = false;
		if (scheduler != null) {
			scheduler.shutdown();
			try {
				if (!scheduler.awaitTermination(800, TimeUnit.MILLISECONDS)) {
					scheduler.shutdownNow();
				}
			} catch (InterruptedException e) {
				scheduler.shutdownNow();
			}
		}
		LOGGER.info("上传进程已停止。");
	}
}
