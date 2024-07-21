from client.event import StatusUploadEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_homepage import Ui_EduSync

class MainWindow(QMainWindow):
    def __init__(self):
        super(),__init__()

        self.ui = Ui_EduSync
        self.ui.setupUi(self)



if __name__ == "__main__":
    event_status = StatusUploadEvent(1, 'status_bus', 1)
    event_status.start()
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
