#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月11日

@author: Kenny
'''
import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QtGui.QIcon("icons/tools_16px.ico"))
        
        
app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())