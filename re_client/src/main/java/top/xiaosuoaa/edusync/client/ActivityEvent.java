package top.xiaosuoaa.edusync.client;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import top.xiaosuoaa.edusync.client.core.AbstractComputer;
import top.xiaosuoaa.edusync.client.core.StatusUploader;

import java.awt.*;
import java.util.Objects;

public class ActivityEvent {
	@FXML
	public Label macList;
	@FXML
	private TextField otherNameField;

	@FXML
	public void onUploadStatusButtonClick(ActionEvent event) {
		Button button = (Button) event.getSource();
		if (Objects.equals(button.getText(), "上传状态")) {
			StatusUploader.start();
			macList.setText(new AbstractComputer().getUUID());

			// 获取备注名并设置到AbstractComputer
			String otherName = otherNameField.getText();
			AbstractComputer.setOtherName(otherName);

			button.setText("停止上传");
		} else if (Objects.equals(button.getText(), "停止上传")) {
			StatusUploader.stop();
			button.setText("上传状态");
		}
	}

	@FXML
	public void onUploadOtherNameButtonClick(ActionEvent actionEvent) {
		String text = otherNameField.getText();
		if (!text.isEmpty() && !text.equals(AbstractComputer.getOtherName())) {
			AbstractComputer.setOtherName(text);
			TrayNotificationManager.showNotification("上传成功", "更改备注名成功", TrayIcon.MessageType.INFO);
		}
	}
}