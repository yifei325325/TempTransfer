#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月11日

@author: Kenny
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
app = QApplication(sys.argv)
widget = QWidget()
widget.resize(500,300)
widget.setWindowTitle("simple")
widget.show()
sys.exit(app.exec_())