package top.xiaosuoaa.edusync.client;

import java.awt.*;

public class TrayNotificationManager {
    private static TrayIcon trayIcon;

    public static void setTrayIcon(TrayIcon icon) {
        trayIcon = icon;
    }

    public static void showNotification(String title, String message, TrayIcon.MessageType messageType) {
        if (trayIcon != null) {
            trayIcon.displayMessage(title, message, messageType);
        }
    }
}