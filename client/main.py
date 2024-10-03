import sys
from PySide6.QtWidgets import  QApplication, QMainWindow
from ui.homepage import Ui_EduSync
from event import StatusUploadEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.thread_status = 1
        self.id = 0
        self.thread = StatusUploadEvent(self.id, 'status_bus', 1)
        self.ui = Ui_EduSync()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        if self.thread_status == 0:
            self.thread.stop()
            self.ui.pushButton.setText("启动")
            self.id += 1
            self.thread = StatusUploadEvent(self.id, 'status_bus', 1)
            self.thread_status = 1
        else:
            self.thread.start()
            self.ui.pushButton.setText("停止")
            self.thread_status = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())
