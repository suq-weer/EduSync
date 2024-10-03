import sys
from PySide6.QtWidgets import  QApplication, QMainWindow
from ui.homepage import Ui_EduSync

'''
from event import StatusUploadEvent
StatusUploadEvent(1, 'status_bus', 1).start()
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_EduSync
    ui.show()
    sys.exit(app.exec())
