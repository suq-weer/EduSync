# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepagezVhLYU.ui'
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
                               QSizePolicy, QWidget, QStatusBar, QToolButton, QPushButton)

class Ui_EduSync(object):
    def setupUi(self, EduSync):
        if not EduSync.objectName():
            EduSync.setObjectName(u"EduSync")
        EduSync.resize(652, 388)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EduSync.sizePolicy().hasHeightForWidth())
        EduSync.setSizePolicy(sizePolicy)
        EduSync.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.centralwidget = QWidget(EduSync)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 10, 631, 41))
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setStyleSheet(u"border-radius:15%;\n"
"border:2px solid blue;\n"
"background-color: rgb(255, 255, 255);")
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(610, 20, 24, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 80, 200, 200))
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(200, 200))
        self.pushButton.setMaximumSize(QSize(200, 200))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(31)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border-radius:100%;\n"
"background-color: rgb(234, 234, 234);\n"
"border:2px solid #6B6B6B;\n"
"color:rgb(0,0,0);")
        self.pushButton.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.pushButton.setIconSize(QSize(30, 30))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 71, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(0,0,0);")
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 60, 631, 251))
        sizePolicy1.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy1)
        self.plainTextEdit_2.setStyleSheet(u"border-radius:15%;\n"
"background-color: rgb(255, 255, 255);\n"
"border:2px solid blue;")
        self.plainTextEdit_3 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(10, 320, 631, 41))
        sizePolicy.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy)
        self.plainTextEdit_3.setStyleSheet(u"border-radius:15%;\n"
"border:2px solid blue;\n"
"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(573, 333, 53, 15))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 85);")
        EduSync.setCentralWidget(self.centralwidget)
        self.plainTextEdit_2.raise_()
        self.plainTextEdit.raise_()
        self.toolButton.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.plainTextEdit_3.raise_()
        self.label_2.raise_()
        self.statusbar = QStatusBar(EduSync)
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
        self.label_2.setText(QCoreApplication.translate("EduSync", u"0.0.0.1", None))
    # retranslateUi

