#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月10日

@author: kenny.li
'''
from PyQt4.QtGui import  *
from PyQt4.QtCore import *
import sys

app = QApplication(sys.argv)
w = QWidget()
w.resize(500,300)
w.show()
b = QPushButton("Hello Kitty!",w)
b.setGeometry(400,200,80,50)

b.show()
app.connect(b, SIGNAL("clicked()"),app,SLOT("quit()"))
app.exec_()
            
            