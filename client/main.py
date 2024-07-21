from client.event import StatusUploadEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.__on_PushButton_clicked)

    def __on_PushButton_clicked(self):
        event_status = StatusUploadEvent(1, 'status_bus', 1)
        event_status.start()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
