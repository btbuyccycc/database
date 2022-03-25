# 数据库
运行环境：python 3.7,pandas,numpy,PUQT5

#问题1：
在不同分辨率的屏幕下，字体会有显示不全的情况
解决方法：将PointSize换成PixelSize

#问题2：
生成可执行文件命令
pyinstaller -Dw main.py

#问题3：代码中的路径要用相对地址

#问题4：控件大小缩放与界面缩放不一致（不自适应）
先用水平与垂直布局，再顶层选择合适的布局（sizepolic的设置很重要，fixed表示大小不会变），单独的一行想要居中的话，将这一行再加入一个垂直布局

#同一设定字体
  font = QtGui.QFont()
  font.setFamily("微软雅黑 Light") //字体
  font.setPointSize(16) //字号
  self.foodname.setFont(font) //控件名

下载所有文件，运行main.py即可
有问题请联系：1094104300@qq.com
