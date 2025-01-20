package top.xiaosuoaa.edusync.client;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import top.xiaosuoaa.edusync.client.core.StatusUploader;

import java.io.IOException;

public class HomeApplication extends Application {
	@Override
	public void start(Stage stage) throws IOException {
		FXMLLoader fxmlLoader = new FXMLLoader(HomeApplication.class.getResource("home-view.fxml"));
		Scene scene = new Scene(fxmlLoader.load(), 640, 340);
		stage.setTitle("EduSync");
		stage.setScene(scene);
		stage.show();
	}

	@Override
	public void stop() throws Exception {
		StatusUploader.stop(); // 直接调用StatusUploader的实例方法停止线程
		super.stop();
	}

	public static void main(String[] args) {
		launch();
	}
}