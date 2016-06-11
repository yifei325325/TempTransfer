#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月11日

@author: Kenny
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Tooltip(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("ToolTip")
        self.setToolTip("This is a <b>QWidget<b> widget")
        QToolTip.setFont(QFont("OldEnglish",10))
        self.setWindowIcon(QIcon("icons/tools_16px.ico"))
        
app = QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())