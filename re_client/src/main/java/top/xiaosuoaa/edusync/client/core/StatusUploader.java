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

	/**
	 * 启动上传进程
	 * 此方法首先检查上传进程是否已经在运行，以避免重复启动
	 * 如果进程未运行，则设置运行状态为true，并使用单线程调度器安排定期执行上传任务
	 * 上传任务是同步操作，执行失败时会记录错误信息
	 */
	public void start() {
	    // 检查上传进程是否已经在运行
	    if (running) {
	        LOGGER.warn("StatusUploader is already running.");
	        return;
	    }
	    running = true;
	    scheduler = Executors.newSingleThreadScheduledExecutor();
	    // 定期执行上传任务，初始延迟为0，之后每5秒执行一次
	    scheduler.scheduleAtFixedRate(() -> {
	        try {
	            // 执行同步操作
	            new AbstractComputer().sync();
	        } catch (Exception e) {
	            // 处理上传过程中出现的异常
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
