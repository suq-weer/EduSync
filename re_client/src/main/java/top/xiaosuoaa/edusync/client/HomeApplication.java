package top.xiaosuoaa.edusync.client;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.imageio.ImageIO;
import java.awt.*;
import java.io.IOException;
import java.net.URL;

public class HomeApplication extends Application {
    private static final Logger LOGGER = LoggerFactory.getLogger(HomeApplication.class);
    private static TrayIcon trayIcon;
    private static boolean isWindowVisible = true;
    private Stage primaryStage; // 添加: 定义primaryStage变量

    public static void main(String[] args) {
        launch();
    }

    public static void showError(String message, Exception e, Logger logger) {
        logger.error(message, e);
        TrayNotificationManager.showNotification("Error", message, TrayIcon.MessageType.ERROR);
    }

    @Override
    public void start(Stage stage) throws IOException {
        primaryStage = stage; // 添加: 初始化primaryStage
        FXMLLoader fxmlLoader = new FXMLLoader(HomeApplication.class.getResource("home-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 400, 800);
        stage.setTitle("EduSync");
        stage.setScene(scene);
        stage.show();

        // 添加托盘图标
        addTrayIcon(stage);
    }

    private void addTrayIcon(Stage stage) {
        if (SystemTray.isSupported()) {
            SystemTray systemTray = SystemTray.getSystemTray();
            PopupMenu popupMenu = new PopupMenu();
            MenuItem exitItem = new MenuItem("Exit");

            exitItem.addActionListener(e -> {
                Platform.exit();
                System.exit(0);
            });

            popupMenu.add(exitItem);

            URL imageUrl = HomeApplication.class.getResource("assets/logo.png");
            Image image = null;
            try {
                if (imageUrl != null) {
                    image = ImageIO.read(imageUrl);
                }
            } catch (Exception e) {
                LOGGER.error("无法加载托盘图标", e);
            }

            if (image != null) {
                trayIcon = new TrayIcon(image, "EduSync", popupMenu);
                // 确保 trayIcon 不为 null 后再调用 setImageAutoSize
                trayIcon.setImageAutoSize(true);
            }

            trayIcon.addActionListener(e -> Platform.runLater(() -> {
                stage.show();
                isWindowVisible = true;
            }));

            try {
                systemTray.add(trayIcon);
            } catch (AWTException e) {
                LOGGER.error("无法添加托盘图标", e);
            }

            // 设置 TrayNotificationManager 的 trayIcon
            TrayNotificationManager.setTrayIcon(trayIcon);
        } else {
            LOGGER.warn("系统不支持托盘图标");
        }
    }

    @Override
    public void stop() throws Exception {
        if (isWindowVisible) {
            Platform.runLater(() -> {
                primaryStage.hide();
                isWindowVisible = false;
                showTrayNotification();
            });
        }
    }

    private void showTrayNotification() {
        if (trayIcon != null) {
            trayIcon.displayMessage("EduSync 互联服务", "已进入安静模式，右键托盘图标可以退出", TrayIcon.MessageType.INFO);
        }
    }
}