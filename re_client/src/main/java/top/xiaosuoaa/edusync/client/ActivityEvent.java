package top.xiaosuoaa.edusync.client;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import top.xiaosuoaa.edusync.client.core.ServiceInfo;
import top.xiaosuoaa.edusync.client.core.StatusUploader;

import java.util.Objects;

public class ActivityEvent {
	public static final StatusUploader STATUS_UPLOADER = new StatusUploader();

	@FXML
	public void onStatusButtonClick(ActionEvent event) {
		ServiceInfo serviceInfo = new ServiceInfo();
		System.out.println(serviceInfo.getJSONInfo().toString());
	}

	@FXML
	public void onUploadStatusButtonClick(ActionEvent event) {
		Button button = (Button) event.getSource();
		if (Objects.equals(button.getText(), "上传状态")) {
			STATUS_UPLOADER.start();
			button.setText("停止上传");
		} else if (Objects.equals(button.getText(), "停止上传")) {
			StatusUploader.stop();
			button.setText("上传状态");
		}
	}
}
