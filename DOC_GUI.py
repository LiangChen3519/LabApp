# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'DOCsXZKPs.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

class Ui_DOC(object):
    def setupUi(self, DOC):
        if DOC.objectName():
            DOC.setObjectName(u"DOC")
        # DOC.setWindowModality(Qt.ApplicationModal)
        DOC.resize(600, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DOC.sizePolicy().hasHeightForWidth())
        DOC.setSizePolicy(sizePolicy)
        # make sure the windows can not be resized by users....
        DOC.setMinimumSize(QSize(600, 800))
        DOC.setMaximumSize(QSize(600, 800))
        font = QFont()
        font.setFamily(u"Times New Roman")
        DOC.setFont(font)
        self.centralwidget = QWidget(DOC)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Folder = QFrame(self.centralwidget)
        self.Folder.setObjectName(u"Folder")
        self.Folder.setGeometry(QRect(10, 20, 581, 121))
        self.Folder.setFrameShape(QFrame.StyledPanel)
        self.Folder.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.Folder)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 81, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.textEdit = QLineEdit(self.Folder)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(90, 55, 371, 21))
        self.pushButton = QPushButton(self.Folder)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 54, 91, 24))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 160, 601, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 190, 581, 441))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 640, 601, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 690, 81, 21))
        self.label_2.setFont(font1)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 740, 581, 23))
        self.progressBar.setValue(0)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(87, 692, 172, 21))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(280, 685, 311, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.textEdit_2 = QLineEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        DOC.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(DOC)
        self.statusbar.setObjectName(u"statusbar")
        DOC.setStatusBar(self.statusbar)

        self.retranslateUi(DOC)

        QMetaObject.connectSlotsByName(DOC)

    # setupUi

    # weights labeling
    def retranslateUi(self, DOC):
        DOC.setWindowTitle(QCoreApplication.translate("DOC", u"DOC Transformer", None))
        self.label.setText(QCoreApplication.translate("DOC", u"Path:", None))
        self.pushButton.setText(QCoreApplication.translate("DOC", u"Select", None))
        self.label_2.setText(QCoreApplication.translate("DOC", u"Format:", None))
        self.radioButton_2.setText(QCoreApplication.translate("DOC", u".CSV", None))
        self.radioButton_3.setText(QCoreApplication.translate("DOC", u".XLSX", None))
        self.radioButton.setText(QCoreApplication.translate("DOC", u".TXT", None))
        self.label_3.setText(QCoreApplication.translate("DOC", u"File name:", None))
        self.pushButton_2.setText(QCoreApplication.translate("DOC", u"Run", None))

