from client.event import StatusUploadEvent
from PySide6.QtWidgets import QApplication. QMainWindow
from ui_untitled import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self),__init__()



if __name__ == "__main__":
    event_status = StatusUploadEvent(1, 'status_bus', 1)
    event_status.start()
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
