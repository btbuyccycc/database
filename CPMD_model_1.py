# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPMD_model_1.ui'
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
        MainWindow.setStyleSheet("#MainWindow{border-image:url(background4.jpg);}")
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 90, 491, 111))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_hanliang = QtWidgets.QLabel(self.centralwidget)
        self.label_hanliang.setGeometry(QtCore.QRect(190, 670, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_hanliang.setFont(font)
        self.label_hanliang.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_hanliang.setObjectName("label_hanliang")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(130, 500, 72, 15))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(650, 670, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 670, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 90, 322, 129))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(231, 59))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(22)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(231, 59))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(860, 670, 391, 53))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(191, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_28.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setMinimumSize(QtCore.QSize(191, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_28.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(190, 520, 1069, 98))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_10.setObjectName("label_10")
        self.gridLayout_29.addWidget(self.label_10, 0, 0, 1, 1)
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.jiarewendu = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.jiarewendu.setFont(font)
        self.jiarewendu.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.jiarewendu.setObjectName("jiarewendu")
        self.gridLayout_26.addWidget(self.jiarewendu, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_21.setObjectName("label_21")
        self.gridLayout_26.addWidget(self.label_21, 0, 1, 1, 1)
        self.wendu = QtWidgets.QComboBox(self.layoutWidget2)
        self.wendu.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.wendu.setFont(font)
        self.wendu.setObjectName("wendu")
        self.gridLayout_26.addWidget(self.wendu, 0, 2, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_26, 0, 0, 1, 1)
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.jiareshijian_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.jiareshijian_2.setMinimumSize(QtCore.QSize(74, 92))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.jiareshijian_2.setFont(font)
        self.jiareshijian_2.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.jiareshijian_2.setObjectName("jiareshijian_2")
        self.gridLayout_25.addWidget(self.jiareshijian_2, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_22.setMinimumSize(QtCore.QSize(61, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_22.setObjectName("label_22")
        self.gridLayout_25.addWidget(self.label_22, 0, 1, 1, 1)
        self.shijian = QtWidgets.QComboBox(self.layoutWidget2)
        self.shijian.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.shijian.setFont(font)
        self.shijian.setObjectName("shijian")
        self.gridLayout_25.addWidget(self.shijian, 0, 2, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_25, 0, 1, 1, 1)
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setMinimumSize(QtCore.QSize(74, 92))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_13.setObjectName("label_13")
        self.gridLayout_24.addWidget(self.label_13, 0, 0, 1, 1)
        self.mibi = QtWidgets.QComboBox(self.layoutWidget2)
        self.mibi.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.mibi.setFont(font)
        self.mibi.setObjectName("mibi")
        self.gridLayout_24.addWidget(self.mibi, 0, 1, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_24, 0, 2, 1, 1)
        self.gridLayout_29.addLayout(self.gridLayout_27, 0, 1, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(60, 230, 1332, 250))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_3.setObjectName("label_3")
        self.gridLayout_30.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tang_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.tang_2.setMinimumSize(QtCore.QSize(40, 119))
        self.tang_2.setMaximumSize(QtCore.QSize(40, 119))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.tang_2.setFont(font)
        self.tang_2.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.tang_2.setObjectName("tang_2")
        self.gridLayout_5.addWidget(self.tang_2, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setMaximumSize(QtCore.QSize(104, 54))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tanglei = QtWidgets.QComboBox(self.layoutWidget3)
        self.tanglei.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.tanglei.setFont(font)
        self.tanglei.setStyleSheet("")
        self.tanglei.setObjectName("tanglei")
        self.gridLayout_3.addWidget(self.tanglei, 0, 0, 1, 1)
        self.tanghanliang = QtWidgets.QComboBox(self.layoutWidget3)
        self.tanghanliang.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.tanghanliang.setFont(font)
        self.tanghanliang.setStyleSheet("")
        self.tanghanliang.setObjectName("tanghanliang")
        self.gridLayout_3.addWidget(self.tanghanliang, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 2, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_11.setMaximumSize(QtCore.QSize(104, 54))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_7.setMaximumSize(QtCore.QSize(42, 114))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_7.setObjectName("label_7")
        self.gridLayout_15.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_20.setMinimumSize(QtCore.QSize(104, 50))
        self.label_20.setMaximumSize(QtCore.QSize(104, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_20.setObjectName("label_20")
        self.gridLayout_14.addWidget(self.label_20, 0, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.qita = QtWidgets.QComboBox(self.layoutWidget3)
        self.qita.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.qita.setFont(font)
        self.qita.setObjectName("qita")
        self.gridLayout_13.addWidget(self.qita, 0, 0, 1, 1)
        self.qitahanliang = QtWidgets.QComboBox(self.layoutWidget3)
        self.qitahanliang.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.qitahanliang.setFont(font)
        self.qitahanliang.setObjectName("qitahanliang")
        self.gridLayout_13.addWidget(self.qitahanliang, 1, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_9.setObjectName("label_9")
        self.gridLayout_10.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.zhifanglei = QtWidgets.QComboBox(self.layoutWidget3)
        self.zhifanglei.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.zhifanglei.setFont(font)
        self.zhifanglei.setObjectName("zhifanglei")
        self.gridLayout_6.addWidget(self.zhifanglei, 0, 0, 1, 1)
        self.zhifanghanliang = QtWidgets.QComboBox(self.layoutWidget3)
        self.zhifanghanliang.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.zhifanghanliang.setFont(font)
        self.zhifanghanliang.setObjectName("zhifanghanliang")
        self.gridLayout_6.addWidget(self.zhifanghanliang, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.NaCl = QtWidgets.QLabel(self.layoutWidget3)
        self.NaCl.setMinimumSize(QtCore.QSize(80, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.NaCl.setFont(font)
        self.NaCl.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.NaCl.setObjectName("NaCl")
        self.gridLayout_17.addWidget(self.NaCl, 0, 0, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_19.setMinimumSize(QtCore.QSize(104, 50))
        self.label_19.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_19.setObjectName("label_19")
        self.gridLayout_16.addWidget(self.label_19, 0, 0, 1, 1)
        self.NaClhanliang = QtWidgets.QComboBox(self.layoutWidget3)
        self.NaClhanliang.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.NaClhanliang.setFont(font)
        self.NaClhanliang.setObjectName("NaClhanliang")
        self.gridLayout_16.addWidget(self.NaClhanliang, 0, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 1, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_17, 1, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_21, 0, 1, 1, 1)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_6.setObjectName("label_6")
        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_16.setMinimumSize(QtCore.QSize(110, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_16.setObjectName("label_16")
        self.gridLayout_11.addWidget(self.label_16, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.anjisuanlei = QtWidgets.QComboBox(self.layoutWidget3)
        self.anjisuanlei.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.anjisuanlei.setFont(font)
        self.anjisuanlei.setObjectName("anjisuanlei")
        self.gridLayout_7.addWidget(self.anjisuanlei, 0, 0, 1, 1)
        self.anjisuanhanliang = QtWidgets.QComboBox(self.layoutWidget3)
        self.anjisuanhanliang.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.anjisuanhanliang.setFont(font)
        self.anjisuanhanliang.setObjectName("anjisuanhanliang")
        self.gridLayout_7.addWidget(self.anjisuanhanliang, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 1, 2, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_17.setMinimumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_17.setObjectName("label_17")
        self.gridLayout_11.addWidget(self.label_17, 1, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 1, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.shui = QtWidgets.QLabel(self.layoutWidget3)
        self.shui.setMinimumSize(QtCore.QSize(120, 120))
        self.shui.setMaximumSize(QtCore.QSize(120, 120))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.shui.setFont(font)
        self.shui.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.shui.setObjectName("shui")
        self.gridLayout_19.addWidget(self.shui, 0, 0, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_18.setMinimumSize(QtCore.QSize(104, 51))
        self.label_18.setMaximumSize(QtCore.QSize(104, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        self.label_18.setObjectName("label_18")
        self.gridLayout_18.addWidget(self.label_18, 0, 0, 1, 1)
        self.shuihanliang = QtWidgets.QComboBox(self.layoutWidget3)
        self.shuihanliang.setMinimumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.shuihanliang.setFont(font)
        self.shuihanliang.setObjectName("shuihanliang")
        self.gridLayout_18.addWidget(self.shuihanliang, 0, 1, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 1, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_19, 1, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_22, 0, 2, 1, 1)
        self.gridLayout_30.addLayout(self.gridLayout_23, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.querenmoxing)
        self.pushButton_2.clicked.connect(MainWindow.querentiaojian)
        self.pushButton_4.clicked['bool'].connect(MainWindow.fanhui)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "氯丙醇含量查询"))
        self.label_hanliang.setText(_translate("MainWindow", "含量："))
        self.result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\',\'Agency FB\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Agency FB\'; font-size:10pt;\"><br /></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\',\'Agency FB\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\';\">氯丙醇含量/μg/kg</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "模型\n"
"选择"))
        self.pushButton.setText(_translate("MainWindow", "确认模型"))
        self.pushButton_2.setText(_translate("MainWindow", "确认条件"))
        self.pushButton_4.setText(_translate("MainWindow", "返回"))
        self.label_10.setText(_translate("MainWindow", " 条\n"
" 件"))
        self.jiarewendu.setText(_translate("MainWindow", "加热\n"
"温度"))
        self.label_21.setText(_translate("MainWindow", "/℃"))
        self.jiareshijian_2.setText(_translate("MainWindow", "加热\n"
"时间"))
        self.label_22.setText(_translate("MainWindow", "/min"))
        self.label_13.setText(_translate("MainWindow", "体系\n"
"密闭"))
        self.label_3.setText(_translate("MainWindow", " 组\n"
" 分"))
        self.tang_2.setText(_translate("MainWindow", "糖"))
        self.label_8.setText(_translate("MainWindow", "种    类"))
        self.label_11.setText(_translate("MainWindow", "含量(g)"))
        self.label_7.setText(_translate("MainWindow", "其\n"
"他"))
        self.label_20.setText(_translate("MainWindow", "含量(g)"))
        self.label_9.setText(_translate("MainWindow", "脂肪"))
        self.label_14.setText(_translate("MainWindow", "种  类"))
        self.label_12.setText(_translate("MainWindow", "含量(g)"))
        self.NaCl.setText(_translate("MainWindow", "NaCl"))
        self.label_19.setText(_translate("MainWindow", "含量(g)"))
        self.label_6.setText(_translate("MainWindow", "氨基酸"))
        self.label_16.setText(_translate("MainWindow", "种类"))
        self.label_17.setText(_translate("MainWindow", "含量(g)"))
        self.shui.setText(_translate("MainWindow", "     水"))
        self.label_18.setText(_translate("MainWindow", "含量(g)"))