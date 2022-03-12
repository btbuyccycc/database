import sys
import pandas as pd
import numpy as np
from read_data import read_data
import page_01,page_02,CPMD_model_1,CPMD_model_2,CPMD_model_3,CPMD_model_4
import MCPDE_model_1,MCPDE_model_2,MCPDE_model_3,MCPDE_model_4
from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget, QHeaderView, QFileDialog, QTableWidgetItem, QCheckBox,\
    QApplication,QComboBox
from PyQt5.QtGui import QPixmap, QImage,QFont

from PyQt5.QtCore import QTimer, QDateTime, Qt
data_dir_MCPD = r"mcpd模型数据汇总1011.xlsx"
data_dir_MCPDE = r"MCPDE模型数据汇总1011.xlsx"
xl = pd.read_excel(data_dir_MCPD,engine='openpyxl',sheet_name=None)
xl_MCPDE = pd.read_excel(data_dir_MCPDE,engine='openpyxl',sheet_name=None)
model_name_CPMD = []
model_name_MCPDE = []
for i in xl.keys():
    model_name_CPMD.append(i)

for i in xl_MCPDE.keys():
    model_name_MCPDE.append(i)
leibie = ["MCPD","MCPDE"]
class page_1(QMainWindow,page_01.Ui_MainWindow):
    def __init__(self):
        super(page_1, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)
        #MainWindow.setStyleSheet("#MainWindow{border-image:url(bk4.jpg);}")
        #MainWindow.setStyleSheet("#MainWindow{border-image:url(background3.jpg);}")
    def jinru(self):
        page_1_new.close()
        page_2_new.show()

class page_2(QMainWindow,page_02.Ui_MainWindow):
    def __init__(self):
        super(page_2, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)

    def lvbingchun(self):
        page_2_new.close()
        CPMD_model_1_new.show()

    def julvbingchun(self):
        page_2_new.close()
        MCPDE_model_1_new.show()


    def fanhui(self):
        page_2_new.close()
        page_1_new.show()

#糖模型
class CPMD_model_01(QMainWindow,CPMD_model_1.Ui_MainWindow):
    def __init__(self):
        super(CPMD_model_01, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)

        self.model_name = model_name_CPMD
        self.comboBox.addItems(self.model_name)
        self.comboBox.setCurrentIndex(0)
        zucheng,hanliang = read_data_1.huoqu_zucheng(self.model_name[0],leibie[0])

        self.tanglei.addItems(hanliang[zucheng[0]])
        self.tanglei.setCurrentIndex(0)

        self.tanghanliang.addItems(hanliang[zucheng[1]])
        self.tanghanliang.setCurrentIndex(0)

        self.NaClhanliang.addItems(hanliang[zucheng[2]])
        self.shuihanliang.addItems(hanliang[zucheng[3]])
        self.wendu.addItems(hanliang[zucheng[4]])
        self.shijian.addItems(hanliang[zucheng[5]])

        self.anjisuanlei.setEnabled(False)
        self.anjisuanhanliang.setEnabled(False)

        self.zhifanglei.setEnabled(False)
        self.zhifanghanliang.setEnabled(False)
        self.qita.setEnabled(False)
        self.qitahanliang.setEnabled(False)
        mibi = ['是']
        self.mibi.addItems(mibi)

    def fanhui(self):
        CPMD_model_1_new.close()
        page_2_new.show()

    def querenmoxing(self):
        model = self.comboBox.currentText()
        if model == model_name_CPMD[1]:
            CPMD_model_1_new.close()
            CPMD_model_2_new.show()
            self.comboBox.setCurrentIndex(0)
        if model == model_name_CPMD[2]:
            CPMD_model_1_new.close()
            CPMD_model_3_new.show()
            self.comboBox.setCurrentIndex(0)


    def querentiaojian(self):#确认条件
        font = QFont()
        lei_tang = self.tanglei.currentText()
        num_tang = self.tanghanliang.currentText()
        num_NaCl = self.NaClhanliang.currentText()
        num_shui = self.shuihanliang.currentText()
        num_shijian = self.shijian.currentText()
        num_wendu = self.wendu.currentText()

        tiaojian = [lei_tang,num_tang,num_NaCl,num_shui,num_wendu,num_shijian]

        result = read_data_1.jieguochazhao(self.model_name[0],tiaojian,leibie[0])

        self.result.setText(str(result))
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.result.setFont(font)


class CPMD_model_02(QMainWindow, CPMD_model_2.Ui_MainWindow):
    def __init__(self):
        super(CPMD_model_02, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)
        self.model_name = model_name_CPMD
        # self.comboBox = page_5_new.comboBox
        self.comboBox.addItems(self.model_name)
        self.comboBox.setCurrentIndex(1)
        zucheng, hanliang = read_data_1.huoqu_zucheng(self.model_name[1],leibie[0])

        self.anjisuanlei.addItems(hanliang[zucheng[0]])
        self.anjisuanlei.setCurrentIndex(0)

        self.anjisuanhanliang.addItems(hanliang[zucheng[1]])

        self.anjisuanhanliang.setCurrentIndex(0)

        self.zhifanglei.addItems(["牛脂"])
        self.zhifanglei.setCurrentIndex(0)

        self.zhifanghanliang.addItems(hanliang[zucheng[2]])
        self.zhifanghanliang.setCurrentIndex(0)

        self.NaClhanliang.addItems(hanliang[zucheng[3]])
        self.shuihanliang.addItems(hanliang[zucheng[4]])
        self.wendu.addItems(hanliang[zucheng[5]])
        self.shijian.addItems(hanliang[zucheng[6]])

        self.tanglei.setEnabled(False)
        self.tanghanliang.setEnabled(False)

        # self.zhifanglei.setEnabled(False)
        # self.zhifanghanliang.setEnabled(False)

        self.qita.setEnabled(False)
        self.qitahanliang.setEnabled(False)
        mibi = ['是']
        self.mibi.addItems(mibi)

    def fanhui(self):
        CPMD_model_2_new.close()
        page_2_new.show()

    def querenmoxing(self):
        model = CPMD_model_2_new.comboBox.currentText()
        if model == model_name_CPMD[0]:
            CPMD_model_2_new.close()
            CPMD_model_1_new.show()
            self.comboBox.setCurrentIndex(1)
        if model == model_name_CPMD[2]:
            CPMD_model_2_new.close()
            CPMD_model_3_new.show()
            self.comboBox.setCurrentIndex(1)

    def querentiaojian(self):
        font = QFont()
        lei_anjisuan = self.anjisuanlei.currentText()
        num_anjisuan = self.anjisuanhanliang.currentText()
        num_zhifang = self.zhifanghanliang.currentText()
        num_NaCl = self.NaClhanliang.currentText()
        num_shui = self.shuihanliang.currentText()
        num_shijian = self.shijian.currentText()
        num_wendu = self.wendu.currentText()

        tiaojian = [lei_anjisuan, num_anjisuan, num_zhifang,num_NaCl, num_shui, num_wendu, num_shijian]

        result = read_data_1.jieguochazhao(model=self.model_name[1],tiaojian=tiaojian,leibie=leibie[0])

        self.result.setText(str(result))
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.result.setFont(font)

class CPMD_model_03(QMainWindow, CPMD_model_3.Ui_MainWindow):#氨基酸
    def __init__(self):
        super(CPMD_model_03, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)
        self.model_name = model_name_CPMD
        #self.comboBox = page_5_new.comboBox
        self.comboBox.addItems(self.model_name)
        self.comboBox.setCurrentIndex(2)

        zucheng, hanliang = read_data_1.huoqu_zucheng(self.model_name[2],leibie[0])

        self.all_data = hanliang#

        self.zhifanglei.addItems(hanliang[zucheng[0]])
        self.zhifanglei.setCurrentIndex(0)

        # self.zhifanghanliang.addItems(hanliang[zucheng[1]])
        # self.zhifanghanliang.setCurrentIndex(0)

        #self.NaClhanliang.addItems(hanliang[zucheng[2]])
        #self.shuihanliang.addItems(hanliang[zucheng[3]])
        #self.wendu.addItems(hanliang[zucheng[4]])
        #self.shijian.addItems(hanliang[zucheng[5]])

        self.anjisuanlei.setEnabled(False)
        self.anjisuanhanliang.setEnabled(False)

        self.tanglei.setEnabled(False)
        self.tanghanliang.setEnabled(False)
        self.qita.setEnabled(False)
        self.qitahanliang.setEnabled(False)
        mibi = ['是']
        self.mibi.addItems(mibi)

    def querenmoxing(self):
        model = CPMD_model_3_new.comboBox.currentText()
        if model == model_name_CPMD[0]:
            CPMD_model_3_new.close()
            CPMD_model_1_new.show()
            self.comboBox.setCurrentIndex(3)
        if model == model_name_CPMD[1]:
            CPMD_model_3_new.close()
            CPMD_model_2_new.show()
            self.comboBox.setCurrentIndex(3)
    def fanhui(self):
        CPMD_model_3_new.close()
        page_2_new.show()

    def querentiaojian(self):
        font = QFont()
        lei_zhifang = self.zhifanglei.currentText()
        num_zhifang = self.zhifanghanliang.currentText()
        num_NaCl = self.NaClhanliang.currentText()
        num_shui = self.shuihanliang.currentText()
        num_shijian = self.shijian.currentText()
        num_wendu = self.wendu.currentText()

        tiaojian = [lei_zhifang, num_zhifang, num_NaCl, num_shui, num_wendu, num_shijian]

        result = read_data_1.jieguochazhao(self.model_name[2], tiaojian,leibie[0])

        self.result.setText(str(result))
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.result.setFont(font)
    def change(self):
        sanyousuanganyouzhi = ['0.05','0.1','0.2','0.3','0.4']
        other = ['0.02']
        num_shui_1 = ['1']
        num_shui_2 = ['0.05']
        if self.zhifanglei.currentText() == "三油酸甘油酯" or self.zhifanglei.currentText() == "三硬脂酸甘油酯":
            self.zhifanghanliang.clear()
            self.zhifanghanliang.addItems(sanyousuanganyouzhi)
            self.zhifanghanliang.setCurrentIndex(0)
            self.shuihanliang.clear()
            self.shuihanliang.addItems(num_shui_1)
        else:
            self.zhifanghanliang.clear()
            self.zhifanghanliang.addItems(other)
            self.zhifanghanliang.setCurrentIndex(0)
            self.shuihanliang.clear()
            self.shuihanliang.addItems(num_shui_2)
    def zhifangliang_change(self):
        num_ganyouzhi = ['0.1','0.2','0.3','0.4']
        num_NaCl = ["0.1"]
        num_NaCl_1 = ['0.05','0.075','0.1','0.2','0.3']
        other = ['0.003']
        wendu_1 = ['100']
        wendu_2 = ['100','120','140','160','180']
        wendu_3 = ['100','120','140']
        if self.zhifanglei.currentText() == "三油酸甘油酯" or self.zhifanglei.currentText() == "三硬脂酸甘油酯":
            if self.zhifanghanliang.currentText() in num_ganyouzhi:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(num_NaCl)
                # self.wendu.clear()
                # self.wendu.addItems(wendu_1)
            else:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(num_NaCl_1)
                # self.wendu.clear()
                # self.wendu.addItems(wendu_2)
        else:
            self.NaClhanliang.clear()
            self.NaClhanliang.addItems(other)
            # self.wendu.clear()
            # self.wendu.addItems(wendu_3)
    def wendu_change(self):
        shijian_1 = ['110']
        shijian_2 = ['60','110','120','240','360','480']
        shijian_3 = ['0','2','4','6','8','16']
        wendu_1 = ['100','140','160','180']
        wendu_2 = ['120']
        if self.zhifanglei.currentText() == "三油酸甘油酯" or self.zhifanglei.currentText() == "三硬脂酸甘油酯":
            if self.wendu.currentText() in wendu_1:
                self.shijian.clear()
                self.shijian.addItems(shijian_1)
            else:
                self.shijian.clear()
                self.shijian.addItems(shijian_2)
        else:
            self.shijian.clear()
            self.shijian.addItems(shijian_3)
    def Na_change(self):
        pass
        Na_num = ['0.05', '0.075', '0.2', '0.3']
        wendu_1 = ['100']
        wendu_2 = ['100', '120', '140', '160', '180']
        wendu_3 = ['100', '120', '140']
        if self.zhifanglei.currentText() == "三油酸甘油酯" or self.zhifanglei.currentText() == "三硬脂酸甘油酯":
            if self.NaClhanliang.currentText() in Na_num:
                self.wendu.clear()
                self.wendu.addItems(wendu_1)
            else:
                self.wendu.clear()
                self.wendu.addItems(wendu_2)
        else:
            self.wendu.clear()
            self.wendu.addItems(wendu_3)

class MCPDE_1(QMainWindow, MCPDE_model_1.Ui_MPCDE_shiyongyou):
    def __init__(self):
        super(MCPDE_1, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)
        self.model_name = model_name_MCPDE
        # self.comboBox = page_5_new.comboBox
        self.comboBox.addItems(self.model_name)
        self.comboBox.setCurrentIndex(0)

        zucheng, hanliang = read_data_1.huoqu_zucheng(self.model_name[0],leibie[1])

        self.all_data = hanliang  #
        self.zhifanglei.addItems(hanliang[zucheng[0]])
        self.zhifanglei.setCurrentIndex(0)

        self.zhifanghanliang.addItems(hanliang[zucheng[1]])
        self.zhifanghanliang.setCurrentIndex(0)
        self.NaClhanliang.addItems(hanliang[zucheng[2]])
        self.shuihanliang.addItems(hanliang[zucheng[3]])
        self.wendu.addItems(hanliang[zucheng[4]])
        self.shijian.addItems(hanliang[zucheng[5]])

        self.anjisuanlei.setEnabled(False)
        self.anjisuanhanliang.setEnabled(False)

        self.tanglei.setEnabled(False)
        self.tanghanliang.setEnabled(False)
        self.qita.setEnabled(False)
        self.qitahanliang.setEnabled(False)
        mibi = ['是']
        self.mibi.addItems(mibi)

    def querenmoxing(self):
        model = self.comboBox.currentText()
        if model == model_name_MCPDE[1]:
            MCPDE_model_1_new.close()
            MCPDE_model_2_new.show()
            self.comboBox.setCurrentIndex(0)
        if model == model_name_MCPDE[2]:
            MCPDE_model_1_new.close()
            MCPDE_model_3_new.show()
            self.comboBox.setCurrentIndex(0)
        if model == model_name_MCPDE[3]:
            MCPDE_model_1_new.close()
            MCPDE_model_4_new.show()
            self.comboBox.setCurrentIndex(0)
    def querentiaojian(self):
        font = QFont()
        lei_zhifang = self.zhifanglei.currentText()
        num_zhifang = self.zhifanghanliang.currentText()

        num_NaCl = self.NaClhanliang.currentText()
        num_shui = self.shuihanliang.currentText()
        num_shijian = self.shijian.currentText()
        num_wendu = self.wendu.currentText()
        tiaojian = [lei_zhifang, num_zhifang, num_NaCl, num_shui, num_wendu, num_shijian]

        result = read_data_1.jieguochazhao(self.model_name[0], tiaojian,leibie[1])

        self.result.setText(str(result))
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.result.setFont(font)
    def fanhui(self):
        MCPDE_model_1_new.close()
        page_2_new.show()

class MCPDE_2(QMainWindow, MCPDE_model_2.Ui_MPCDE_shiyongyou):
    def __init__(self):
        super(MCPDE_2, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)
        self.model_name = model_name_MCPDE
        # self.comboBox = page_5_new.comboBox
        self.comboBox.addItems(self.model_name)
        self.comboBox.setCurrentIndex(1)

        zucheng, hanliang = read_data_1.huoqu_zucheng(self.model_name[1],leibie[1])

        self.all_data = hanliang  #
        self.zhifanglei.addItems(hanliang[zucheng[0]])
        self.zhifanglei.setCurrentIndex(0)

        self.zhifanghanliang.addItems(hanliang[zucheng[1]])
        self.zhifanghanliang.setCurrentIndex(0)
        #self.NaClhanliang.addItems(hanliang[zucheng[6]])
        #self.shuihanliang.addItems(hanliang[zucheng[4]])
        #self.wendu.addItems(hanliang[zucheng[5]])
        #self.shijian.addItems(hanliang[zucheng[6]])

        #self.qitahanliang.addItems(hanliang[zucheng[3]])
        #self.qitahanliang.setCurrentIndex(0)
        self.qita.addItems(["水含量"])

        self.anjisuanlei.setEnabled(False)
        self.anjisuanhanliang.setEnabled(False)

        self.tanglei.setEnabled(False)
        self.tanghanliang.setEnabled(False)

        #self.qitahanliang.setEnabled(False)
        mibi = ['是']
        self.mibi.addItems(mibi)

    def querenmoxing(self):
        model = self.comboBox.currentText()
        if model == model_name_MCPDE[0]:
            MCPDE_model_2_new.close()
            MCPDE_model_1_new.show()
            self.comboBox.setCurrentIndex(1)
        if model == model_name_MCPDE[2]:
            MCPDE_model_2_new.close()
            MCPDE_model_3_new.show()
            self.comboBox.setCurrentIndex(1)
        if model == model_name_MCPDE[3]:
            MCPDE_model_2_new.close()
            MCPDE_model_4_new.show()
            self.comboBox.setCurrentIndex(1)

    def querentiaojian(self):
        font = QFont()
        lei_zhifang = self.zhifanglei.currentText()
        num_zhifang = self.zhifanghanliang.currentText()
        num_NaCl = self.NaClhanliang.currentText()
        num_shui = self.shuihanliang.currentText()
        num_shijian = self.shijian.currentText()
        num_wendu = self.wendu.currentText()
        num_shuihanliang = self.qitahanliang.currentText()

        tiaojian = [lei_zhifang, num_zhifang, num_shijian, num_shuihanliang, num_shui, num_wendu, num_NaCl]

        result,result2,result3 = read_data_1.jieguochazhao(self.model_name[1], tiaojian,leibie[1])

        self.result.setText(str(result))
        self.result_2.setText(str(result2))
        self.result_3.setText(str(round(result3,1)))
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.result.setFont(font)
    def fanhui(self):
        MCPDE_model_2_new.close()
        page_2_new.show()

    def zhifanglei_change(self):
        shui_1 = ['6','47.6']
        shui_2 = ['6']
        shui_3 = ['0','2','4','6','8','9.52','10','19','28.6','38.1','47.6']
        shui_4 = ['47.6']

        if self.zhifanglei.currentText() == '大豆油' or self.zhifanglei.currentText() == '玉米油' or self.zhifanglei.currentText() == '棕榈油':
            self.qitahanliang.clear()
            self.qitahanliang.addItems(shui_1)

        elif self.zhifanglei.currentText() == '葵花籽油':
            self.qitahanliang.clear()
            self.qitahanliang.addItems(shui_2)
        elif self.zhifanglei.currentText() == '菜籽油':
            self.qitahanliang.clear()
            self.qitahanliang.addItems(shui_4)
        else:
            self.qitahanliang.clear()
            self.qitahanliang.addItems(shui_3)

    def qitahanliang_change(self):
        Na_1 = ['1']
        Na_2 = ['4']
        Na_3 = ['0.5','1','1.5','2','2.5']
        shuihanliang_1 = ['6']
        shuihanliang_2 = ['47.6']
        shuihanliang_3 =  ['0','2','4','8','10']
        if self.zhifanglei.currentText() == '大豆油' or self.zhifanglei.currentText() == '玉米油' or self.zhifanglei.currentText() == '棕榈油':
            if self.qitahanliang.currentText() in shuihanliang_1:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(Na_1)
            else:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(Na_2)
        elif self.zhifanglei.currentText() == '菜籽油':
            self.NaClhanliang.clear()
            self.NaClhanliang.addItems(Na_2)
        elif self.zhifanglei.currentText() == '葵花籽油':
            self.NaClhanliang.clear()
            self.NaClhanliang.addItems(Na_1)
        else:
            if self.qitahanliang.currentText() in shuihanliang_1:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(Na_3)
            elif self.qitahanliang.currentText() in shuihanliang_3:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(Na_1)
            else:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(Na_2)

    def NaCl_change(self):
        Na_1 = ['1']
        Na_2 = ['4']
        Na_3 = ['0.5','1.5','2','2.5']
        shui_1 = ['60']
        shui_2 = ['100']
        shui_3 = ['60','160']
        shuihanliang = ['0','2','4','8','10']
        shui_4 = ['160']
        if self.zhifanglei.currentText() == '大豆油' or self.zhifanglei.currentText() == '玉米油' or self.zhifanglei.currentText() == '棕榈油':
            if self.NaClhanliang.currentText() in Na_1:
                self.shuihanliang.clear()
                self.shuihanliang.addItems(shui_1)
            else:
                self.shuihanliang.clear()
                self.shuihanliang.addItems(shui_2)
        elif self.zhifanglei.currentText() == '菜籽油':
            self.shuihanliang.clear()
            self.shuihanliang.addItems(shui_2)
        elif self.zhifanglei.currentText() == '葵花籽油':
            self.shuihanliang.clear()
            self.shuihanliang.addItems(shui_1)
        else:
           if self.NaClhanliang.currentText() in Na_1:
               if self.qitahanliang.currentText() in shuihanliang:
                   self.shuihanliang.clear()
                   self.shuihanliang.addItems(shui_4)
               else:
                   self.shuihanliang.clear()
                   self.shuihanliang.addItems(shui_3)
           elif self.NaClhanliang.currentText() in Na_3:
               self.shuihanliang.clear()
               self.shuihanliang.addItems(shui_1)
           else:
               self.shuihanliang.clear()
               self.shuihanliang.addItems(shui_2)
    def shui_change(self):
        shui_1 = ['60']
        shui_2 = ['160']
        shui_3 = ['100']
        tem_1 = ['100','130','160','190','220']
        tem_2 = ['160']
        tem_3 = ['100','130','160','190']
        shuihanliang = ['0', '2', '4', '8', '10']
        Na = ['0.5','1.5','2','2.5']
        if self.zhifanglei.currentText() == '大豆油' or self.zhifanglei.currentText() == '玉米油' or self.zhifanglei.currentText() == '棕榈油':
            if self.shuihanliang.currentText() in shui_1:
                self.wendu.clear()
                self.wendu.addItems(tem_2)
            else:
                self.wendu.clear()
                self.wendu.addItems(tem_2)
        elif self.zhifanglei.currentText() == '菜籽油':
            self.wendu.clear()
            self.wendu.addItems(tem_2)
        elif self.zhifanglei.currentText() == '葵花籽油':
            self.wendu.clear()
            self.wendu.addItems(tem_2)
        else:
            if self.shuihanliang.currentText() in shui_1:
                if self.NaClhanliang.currentText() in Na:
                    self.wendu.clear()
                    self.wendu.addItems(tem_2)
                else:

                    self.wendu.clear()
                    self.wendu.addItems(tem_1)
            elif self.shuihanliang.currentText() in shui_2:
                self.wendu.clear()
                self.wendu.addItems(tem_2)
            else:
                self.wendu.clear()
                self.wendu.addItems(tem_3)
    def wendu_change(self):
        wendu_1 = ['100','130','190','220']
        wendu_2 = ['160']
        shuihanliang = ['0', '2', '4', '8', '10']
        Na = ['0.5', '1.5', '2', '2.5']
        time_1 = ['0.5']
        time_2 = ['0.25','0.5','0.75','1','1.25','2','3','4']
        if self.zhifanglei.currentText() == '花生油':
            if self.wendu.currentText() in wendu_1:
                self.shijian.clear()
                self.shijian.addItems(time_1)
            elif self.wendu.currentText() in wendu_2 and self.qitahanliang.currentText() in shuihanliang:
                self.shijian.clear()
                self.shijian.addItems(time_1)
            elif self.wendu.currentText() in wendu_2 and self.NaClhanliang.currentText() in Na:
                self.shijian.clear()
                self.shijian.addItems(time_1)
            else:
                self.shijian.clear()
                self.shijian.addItems(time_2)
        else:
            self.shijian.clear()
            self.shijian.addItems(time_1)

class MCPDE_3(QMainWindow, MCPDE_model_3.Ui_MPCDE_shiyongyou):
    def __init__(self):
        super(MCPDE_3, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)
        self.model_name = model_name_MCPDE
        # self.comboBox = page_5_new.comboBox
        self.comboBox.addItems(self.model_name)
        self.comboBox.setCurrentIndex(2)

        zucheng, hanliang = read_data_1.huoqu_zucheng(self.model_name[2],leibie[1])

        self.all_data = hanliang  #

        self.qita.addItems(["NaCl浸泡浓度%"])
        self.qitahanliang.addItems(hanliang[zucheng[2]])
        self.wendu.addItems(hanliang[zucheng[1]])
        self.shijian.addItems(hanliang[zucheng[0]])

        self.anjisuanlei.setEnabled(False)
        self.anjisuanhanliang.setEnabled(False)

        self.tanglei.setEnabled(False)
        self.tanghanliang.setEnabled(False)
        self.zhifanglei.setEnabled(False)
        self.zhifanghanliang.setEnabled(False)
        self.tanglei.setEnabled(False)
        self.shuihanliang.setEnabled(False)

        self.NaClhanliang.setEnabled(False)
        #self.qitahanliang.setEnabled(False)
        mibi = ['否']
        self.mibi.addItems(mibi)

    def querenmoxing(self):
        model = self.comboBox.currentText()
        if model == model_name_MCPDE[0]:
            MCPDE_model_3_new.close()
            MCPDE_model_1_new.show()
            self.comboBox.setCurrentIndex(2)
        if model == model_name_MCPDE[1]:
            MCPDE_model_3_new.close()
            MCPDE_model_2_new.show()
            self.comboBox.setCurrentIndex(2)
        if model == model_name_MCPDE[3]:
            MCPDE_model_3_new.close()
            MCPDE_model_4_new.show()
            self.comboBox.setCurrentIndex(2)
    def querentiaojian(self):
        font = QFont()
        #lei_zhifang = self.zhifanglei.currentText()
        #num_zhifang = self.zhifanghanliang.currentText()
        num_NaCl = self.qitahanliang.currentText()
        #num_shui = self.shuihanliang.currentText()
        num_shijian = self.shijian.currentText()
        num_wendu = self.wendu.currentText()
        #num_shuihanliang = self.qitahanliang.currentText()

        tiaojian = [num_shijian,num_wendu,num_NaCl,]

        result = read_data_1.jieguochazhao(self.model_name[2], tiaojian,leibie[1])

        self.result.setText(str(result))
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.result.setFont(font)
    def fanhui(self):
        MCPDE_model_3_new.close()
        page_2_new.show()

    def zhifanglei_change(self):
        pass

    def qitahanliang_change(self):
        pass

    def NaCl_change(self):
        pass
    def shui_change(self):
        pass
    def wendu_change(self):
        pass

class MCPDE_4(QMainWindow, MCPDE_model_4.Ui_MPCDE_shiyongyou):
    def __init__(self):
        super(MCPDE_4, self).__init__()
        self.setupUi(self)
        self.setGeometry(300,100,1440,900)
        self.model_name = model_name_MCPDE
        # self.comboBox = page_5_new.comboBox
        self.comboBox.addItems(self.model_name)
        self.comboBox.setCurrentIndex(1)

        zucheng, hanliang = read_data_1.huoqu_zucheng(self.model_name[3],leibie[1])

        self.all_data = hanliang  #

        self.zhifanglei.addItems(hanliang[zucheng[0]])
        self.zhifanglei.setCurrentIndex(3)

        self.qita.addItems(["豇豆"])
        self.qitahanliang.addItems(hanliang[zucheng[3]])
        #self.wendu.addItems(hanliang[zucheng[6]])
        self.shijian.addItems(hanliang[zucheng[5]])
        self.shuihanliang.addItems(hanliang[zucheng[4]])
        #self.NaClhanliang.addItems(hanliang[zucheng[2]])

        self.anjisuanlei.setEnabled(False)
        self.anjisuanhanliang.setEnabled(False)

        self.tanglei.setEnabled(False)
        self.tanghanliang.setEnabled(False)
        #self.zhifanglei.setEnabled(False)
        #self.zhifanghanliang.setEnabled(False)
        self.tanglei.setEnabled(False)
        #self.shuihanliang.setEnabled(False)

        mibi = ['是']
        self.mibi.addItems(mibi)

    def querenmoxing(self):
        model = self.comboBox.currentText()
        if model == model_name_MCPDE[0]:
            MCPDE_model_4_new.close()
            MCPDE_model_1_new.show()
            self.comboBox.setCurrentIndex(3)
        if model == model_name_MCPDE[1]:
            MCPDE_model_4_new.close()
            MCPDE_model_2_new.show()
            self.comboBox.setCurrentIndex(3)
        if model == model_name_MCPDE[2]:
            MCPDE_model_4_new.close()
            MCPDE_model_3_new.show()
            self.comboBox.setCurrentIndex(3)
    def querentiaojian(self):
        font = QFont()
        lei_zhifang = self.zhifanglei.currentText()
        num_zhifang = self.zhifanghanliang.currentText()
        num_NaCl = self.NaClhanliang.currentText()
        num_qita = self.qitahanliang.currentText()
        num_shui = self.shuihanliang.currentText()
        num_shijian = self.shijian.currentText()
        num_wendu = self.wendu.currentText()

        #num_shuihanliang = self.qitahanliang.currentText()

        tiaojian = [lei_zhifang,num_zhifang,num_NaCl,num_qita,num_shui,num_shijian,num_wendu]

        result1,result2,result3 = read_data_1.jieguochazhao(self.model_name[3], tiaojian,leibie[1])

        self.result.setText(str(result1))
        self.result_2.setText(str(result2))
        self.result_3.setText(str(round(result3,1)))
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.result.setFont(font)
    def fanhui(self):
        MCPDE_model_4_new.close()
        page_2_new.show()

    def zhifanglei_change(self):
        zhi_1 = ['5','10','15','20','25']
        zhi_2 = ['5']
        Na_1 = ['1.5']
        Na_2 = ['1','1.5','2','2.5','5']
        if self.zhifanglei.currentText() == "花生油":
            self.zhifanghanliang.clear()
            self.zhifanghanliang.addItems(zhi_1)
        else:
            self.zhifanghanliang.clear()
            self.zhifanghanliang.addItems(zhi_2)

    def zhifanghanliang_change(self):
        zhi_1 = ['10','15','20','25']
        NaCl_1 = ['1.5']
        NaCl_2 = ['1','1.5','2','2.5','5']
        NaCl_3 = ['1','1.5','2.5','5']
        if self.zhifanglei.currentText() == "花生油":
            if self.zhifanghanliang.currentText() in zhi_1:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(NaCl_1)

            else:
                self.NaClhanliang.clear()
                self.NaClhanliang.addItems(NaCl_2)

        else:
            self.NaClhanliang.clear()
            self.NaClhanliang.addItems(NaCl_1)

    def NaCl_change(self):
        NaCl_1 = ['1.5']
        NaCl_2 = ['1', '2', '2.5', '5']
        zhifang = ['10','15','20','25']
        wendu_1 = ['80', '100', '120', '140', '160']
        wendu_2 = ['100']
        if self.zhifanglei.currentText() == "花生油":
            if self.NaClhanliang.currentText() in NaCl_2:
                self.wendu.clear()
                self.wendu.addItems(wendu_2)
            elif self.NaClhanliang.currentText() in NaCl_1 and self.zhifanghanliang.currentText():
                self.wendu.clear()
                self.wendu.addItems(wendu_2)
            else:
                self.wendu.clear()
                self.wendu.addItems(wendu_1)
        else:
            self.wendu.clear()
            self.wendu.addItems(wendu_2)

    def shui_change(self):
        pass
    def wendu_change(self):
        pass
    def slot1(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)

    read_data_1 = read_data()
    page_1_new = page_1()
    page_2_new = page_2()
    CPMD_model_1_new = CPMD_model_01()
    CPMD_model_2_new = CPMD_model_02()
    CPMD_model_3_new = CPMD_model_03()
    MCPDE_model_1_new = MCPDE_1()
    MCPDE_model_2_new = MCPDE_2()
    MCPDE_model_3_new = MCPDE_3()
    MCPDE_model_4_new = MCPDE_4()
    page_1_new.show()

    sys.exit(app.exec_())
