module top.xiaosuoaa.edusync.client {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
	requires com.github.oshi;
	requires java.net.http;
	requires com.google.gson;
	requires java.desktop;
	requires java.logging;
	requires org.slf4j;
	requires java.security.jgss;
	requires java.management;

	opens top.xiaosuoaa.edusync.client to javafx.fxml;
    exports top.xiaosuoaa.edusync.client;
	exports top.xiaosuoaa.edusync.client.core;
}