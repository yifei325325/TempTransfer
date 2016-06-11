#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月11日

@author: Kenny
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MessageBox(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("message box")
        self.setWindowIcon(QIcon("icons/tools_16px.ico"))
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self,"Message",
                                     "Are you sure to quit?",QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
app = QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())
            
            
            
        