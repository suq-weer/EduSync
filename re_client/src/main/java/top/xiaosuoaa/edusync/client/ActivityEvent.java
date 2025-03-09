package top.xiaosuoaa.edusync.client;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import top.xiaosuoaa.edusync.client.core.AbstractComputer;
import top.xiaosuoaa.edusync.client.core.StatusUploader;

import java.util.Objects;

public class ActivityEvent {
	public static final StatusUploader STATUS_UPLOADER = new StatusUploader();
	public Label macList;

	@FXML
	public void onUploadStatusButtonClick(ActionEvent event) {
		Button button = (Button) event.getSource();
		if (Objects.equals(button.getText(), "上传状态")) {
			STATUS_UPLOADER.start();
			macList.setText(new AbstractComputer().getUUID().toString());

			button.setText("停止上传");
		} else if (Objects.equals(button.getText(), "停止上传")) {
			StatusUploader.stop();
			button.setText("上传状态");
		}
	}
}
