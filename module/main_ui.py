# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(642, 494)
        MainWindow.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    border-bottom: 2px solid gray;\n"
"    padding: 4px;\n"
"    font-size: 12px;\n"
"    background-color: transparent;\n"
"    width: 500px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid blue;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.inputTelefono = QLineEdit(self.centralwidget)
        self.inputTelefono.setObjectName(u"inputTelefono")
        self.inputTelefono.setGeometry(QRect(40, 50, 271, 31))
        self.inputTelefono.setStyleSheet(u"")
        self.inputEmail = QLineEdit(self.centralwidget)
        self.inputEmail.setObjectName(u"inputEmail")
        self.inputEmail.setGeometry(QRect(350, 50, 271, 31))
        self.inputEmail.setStyleSheet(u"")
        self.inputCURP = QLineEdit(self.centralwidget)
        self.inputCURP.setObjectName(u"inputCURP")
        self.inputCURP.setGeometry(QRect(40, 140, 271, 31))
        self.inputCURP.setStyleSheet(u"")
        self.inputRFC = QLineEdit(self.centralwidget)
        self.inputRFC.setObjectName(u"inputRFC")
        self.inputRFC.setGeometry(QRect(350, 140, 271, 31))
        self.inputRFC.setStyleSheet(u"")
        self.inputIPv4 = QLineEdit(self.centralwidget)
        self.inputIPv4.setObjectName(u"inputIPv4")
        self.inputIPv4.setGeometry(QRect(40, 230, 271, 31))
        self.inputIPv4.setStyleSheet(u"")
        self.inputFechaNacimiento = QLineEdit(self.centralwidget)
        self.inputFechaNacimiento.setObjectName(u"inputFechaNacimiento")
        self.inputFechaNacimiento.setGeometry(QRect(350, 230, 271, 31))
        self.inputFechaNacimiento.setStyleSheet(u"")
        self.inputContrasenia = QLineEdit(self.centralwidget)
        self.inputContrasenia.setObjectName(u"inputContrasenia")
        self.inputContrasenia.setGeometry(QRect(40, 320, 271, 31))
        self.inputContrasenia.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 642, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.inputTelefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero de Telefono", None))
        self.inputEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo Electronico", None))
        self.inputCURP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CURP", None))
        self.inputRFC.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RFC", None))
        self.inputIPv4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IPv4", None))
        self.inputFechaNacimiento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha de Nacimiento", None))
        self.inputContrasenia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
    # retranslateUi

