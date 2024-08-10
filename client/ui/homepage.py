# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepagetGSmNn.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

from qfluentwidgets import (MenuBar, PlainTextEdit, PushButton, StatusBar,
    ToolButton)

class Ui_EduSync(object):
    def setupUi(self, EduSync):
        if not EduSync.objectName():
            EduSync.setObjectName(u"EduSync")
        EduSync.resize(659, 478)
        self.centralwidget = QWidget(EduSync)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plainTextEdit = PlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 0, 651, 41))
        self.toolButton = ToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(620, 10, 24, 21))
        self.pushButton = PushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 100, 200, 200))
        self.pushButton.setMinimumSize(QSize(200, 200))
        self.pushButton.setMaximumSize(QSize(200, 200))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border-radius:100px;\n"
"background-color: rgb(222, 222, 222);")
        self.pushButton.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton.setIconSize(QSize(30, 30))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 10, 41, 21))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 370, 75, 31))
        self.pushButton_2.setStyleSheet(u"border-radius: 50%;\n"
"box-shadow: 4px 4px 4px 4px black inset;\n"
"background-color: rgb(222, 222, 222);")
        self.pushButton_2.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(200, 370, 75, 31))
        self.pushButton_3.setStyleSheet(u"border-radius: 50%;\n"
"box-shadow: 4px 4px 4px 4px black inset;\n"
"background-color: rgb(222, 222, 222);")
        self.pushButton_3.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.pushButton_3.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(390, 370, 75, 31))
        self.pushButton_4.setStyleSheet(u"border-radius: 50%;\n"
"box-shadow: 4px 4px 4px 4px black inset;\n"
"background-color: rgb(222, 222, 222);")
        self.pushButton_4.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(540, 370, 75, 31))
        self.pushButton_5.setStyleSheet(u"border-radius: 50%;\n"
"box-shadow: 4px 4px 4px 4px black inset;\n"
"background-color: rgb(222, 222, 222);")
        self.pushButton_5.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 40, 651, 381))
        EduSync.setCentralWidget(self.centralwidget)
        self.listWidget.raise_()
        self.plainTextEdit.raise_()
        self.toolButton.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.menubar = MenuBar(EduSync)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 659, 33))
        EduSync.setMenuBar(self.menubar)
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

