module top.xiaosuoaa.edusync.client.re_client {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;

    opens top.xiaosuoaa.edusync.client.re_client to javafx.fxml;
    exports top.xiaosuoaa.edusync.client.re_client;
}