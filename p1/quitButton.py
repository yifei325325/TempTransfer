#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月11日

@author: Kenny
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class QuitButton(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("QuitButton")
        self.setWindowIcon(QIcon("icons/tools_16px.ico"))
        quit = QPushButton(u"关闭",self)
        quit.setGeometry(170,100,64,35)
        
        self.connect(quit, SIGNAL("clicked()"),app,SLOT("quit()"))
                     
app = QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())