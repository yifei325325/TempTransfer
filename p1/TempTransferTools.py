#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月2日

@author: Kenny
'''
from PyQt4.QtGui import  *
from PyQt4.QtCore import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class StandardDialog(QDialog):
    def __init__(self,parent=None):
        super(StandardDialog,self).__init__(parent)
        
        self.setWindowTitle("Standard Dialog")
        
        filePushButton = QPushButton(self.tr("文件对话框"))
        colorPushButton = QPushButton(self.tr("颜色对话框"))
        fontPushButton = QPushButton(self.tr("字体对话框"))
        
        self.fileLineEdit = QLineEdit()
        self.colorFrame = QFrame()
        self.colorFrame.setFrameShape(QFrame.Box)
        self.colorFrame.setAutoFillBackground(True)
        self.fontLineEdit = QLineEdit("Hello world!")
        
        layout = QGridLayout()
        layout.addWidget(filePushButton,0,0)
        layout.addWidget(self.fileLineEdit,0,1)
        layout.addWidget(colorPushButton,1,0)
        layout.addWidget(self.colorFrame,1,1)
        layout.addWidget(fontPushButton,2,0)
        layout.addWidget(self.fontLineEdit,2,1)
        
        self.setLayout(layout)
        
        
        
        
        
        
        
        
app = QApplication(sys.argv)
form = StandardDialog()
form.show()
app.exec_()

        
        
        
        
        
        