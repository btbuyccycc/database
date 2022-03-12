# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_01.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setMaximumSize(QtCore.QSize(1440, 900))
        MainWindow.setStyleSheet("#MainWindow{border-image:url(background3.jpg);}")
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 540, 431, 81))
        self.pushButton.setMinimumSize(QtCore.QSize(431, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 150, 791, 171))
        self.label.setMinimumSize(QtCore.QSize(791, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 380, 430, 113))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(161, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255,255, 255)\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(161, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255,255, 255)\n"
"}")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(256, 51))
        self.textEdit.setMaximumSize(QtCore.QSize(256, 51))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setMinimumSize(QtCore.QSize(256, 51))
        self.textEdit_2.setMaximumSize(QtCore.QSize(256, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.jinru)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "点击进入"))
        self.label.setText(_translate("MainWindow", "粮食产后收储运质量数据的\n"
"可信感知、存储和分享系统"))
        self.label_2.setText(_translate("MainWindow", "        用户名"))
        self.label_3.setText(_translate("MainWindow", "          密码"))