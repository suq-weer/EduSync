package top.xiaosuoaa.edusync.client;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import top.xiaosuoaa.edusync.client.core.ServiceInfo;

public class ActivityEvent {
	@FXML
	public void onStatusButtonClick(ActionEvent event) {
		ServiceInfo serviceInfo = new ServiceInfo();
		System.out.println(serviceInfo.getJSONInfo().toString());
	}
}
