# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QSizePolicy, QStatusBar, QToolButton,
    QWidget)

from qfluentwidgets import PushButton

class Ui_EduSync(object):
    def setupUi(self, EduSync):
        if not EduSync.objectName():
            EduSync.setObjectName(u"EduSync")
        EduSync.resize(504, 352)
        self.centralwidget = QWidget(EduSync)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 0, 501, 41))
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(0, 40, 501, 271))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(460, 10, 24, 21))
        self.pushButton = PushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 80, 200, 200))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 10, 41, 21))
        EduSync.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(EduSync)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 504, 33))
        EduSync.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(EduSync)
        self.statusbar.setObjectName(u"statusbar")
        EduSync.setStatusBar(self.statusbar)

        self.retranslateUi(EduSync)

        QMetaObject.connectSlotsByName(EduSync)
    # setupUi

    def retranslateUi(self, EduSync):
        EduSync.setWindowTitle(QCoreApplication.translate("EduSync", u"MainWindow", None))
        self.toolButton.setText(QCoreApplication.translate("EduSync", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("EduSync", u"\u6309\u94ae", None))
        self.label.setText(QCoreApplication.translate("EduSync", u"EduSync", None))
    # retranslateUi

