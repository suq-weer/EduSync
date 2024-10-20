package top.xiaosuoaa.edusync.client;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import top.xiaosuoaa.edusync.client.translate.StringTranslateList;

public class HomeController {
	@FXML
	private Button serviceButton;

	protected int serviceStatus = 0;

	@FXML
	protected void onServiceButtonClicked() {
		if (serviceStatus == 0) {
			serviceButton.setText(StringTranslateList.END_SERVICE);
			serviceStatus = 1;
		} else if (serviceStatus == 1) {
			serviceButton.setText(StringTranslateList.START_SERVICE);
			serviceStatus = 0;
		}
	}
}