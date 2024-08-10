# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepageTkzaPp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

from qfluentwidgets import (PlainTextEdit, PushButton, StatusBar, ToolButton)

class Ui_EduSync(object):
    def setupUi(self, EduSync):
        if not EduSync.objectName():
            EduSync.setObjectName(u"EduSync")
        EduSync.resize(652, 454)
        EduSync.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.centralwidget = QWidget(EduSync)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plainTextEdit = PlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 10, 631, 41))
        self.plainTextEdit.setStyleSheet(u"border-radius:15%;\n"
"border:2px solid blue;\n"
"background-color: rgb(255, 255, 255);")
        self.toolButton = ToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(610, 20, 24, 21))
        self.pushButton = PushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 80, 200, 200))
        self.pushButton.setMinimumSize(QSize(200, 200))
        self.pushButton.setMaximumSize(QSize(200, 200))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(31)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border-radius:100%;\n"
"background-color: rgb(234, 234, 234);\n"
"border:2px solid #6B6B6B;")
        self.pushButton.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton.setIconSize(QSize(30, 30))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 71, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 320, 151, 111))
        self.pushButton_2.setStyleSheet(u"border-radius: 15%;\n"
"border:2px solid blue;\n"
"box-shadow: 5px 5px 5px #888888;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(170, 320, 151, 111))
        self.pushButton_3.setStyleSheet(u"border-radius: 15%;\n"
"border:2px solid blue;\n"
"box-shadow: 5px 5px 5px #888888;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_3.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.pushButton_3.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(330, 320, 151, 111))
        self.pushButton_4.setStyleSheet(u"border-radius: 15%;\n"
"border:2px solid blue;\n"
"box-shadow: 5px 5px 5px #888888;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_4.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(490, 320, 151, 111))
        self.pushButton_5.setStyleSheet(u"border-radius: 15%;\n"
"border:2px solid blue;\n"
"box-shadow: 5px 5px 5px #888888;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_5.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 60, 631, 251))
        self.plainTextEdit_2.setStyleSheet(u"border-radius:15%;\n"
"background-color: rgb(255, 255, 255);\n"
"border:2px solid blue;")
        EduSync.setCentralWidget(self.centralwidget)
        self.plainTextEdit_2.raise_()
        self.plainTextEdit.raise_()
        self.toolButton.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.statusbar = StatusBar(EduSync)
        self.statusbar.setObjectName(u"statusbar")
        EduSync.setStatusBar(self.statusbar)

        self.retranslateUi(EduSync)

        QMetaObject.connectSlotsByName(EduSync)
    # setupUi

    def retranslateUi(self, EduSync):
        EduSync.setWindowTitle(QCoreApplication.translate("EduSync", u"MainWindow", None))
        self.toolButton.setText(QCoreApplication.translate("EduSync", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("EduSync", u"\u542f\u52a8", None))
        self.label.setText(QCoreApplication.translate("EduSync", u"EduSync", None))
        self.pushButton_2.setText(QCoreApplication.translate("EduSync", u"\u6309\u94ae", None))
        self.pushButton_3.setText(QCoreApplication.translate("EduSync", u"\u6309\u94ae", None))
        self.pushButton_4.setText(QCoreApplication.translate("EduSync", u"\u6309\u94ae", None))
        self.pushButton_5.setText(QCoreApplication.translate("EduSync", u"\u6309\u94ae", None))
    # retranslateUi

