from client.event import StatusUploadEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.homepage import Ui_EduSync


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_EduSync()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.__on_PushButton_clicked)

    def __on_PushButton_clicked(self):
        self.event_status = StatusUploadEvent(1, 'status_bus', 1)
        self.event_status.start()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
