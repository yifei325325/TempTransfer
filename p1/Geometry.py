#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月10日

@author: kenny.li
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Geometry(QDialog):
    def __init__(self,parent=None):
        super(Geometry,self).__init__(parent)
        
        self.setWindowTitle("Geometry")
        
        Label1 = QLabel("X0:")
        Label2 = QLabel("Y0:")
        Label3 = QLabel("frameGeometry():")
        Label4 = QLabel("pos():")
        Label5 = QLabel("geometry():")
        Label6 = QLabel("width():")
        Label7 = QLabel("height():")
        Label8 = QLabel("rect():")
        Label9 = QLabel("size():")
        
        self.xLabel = QLabel()
        self.yLabel = QLabel()
        self.frameGeoLabel = QLabel()
        self.posLabel = QLabel()
        self.geoLabel = QLabel()
        self.widthLabel = QLabel()
        self.heightLabel = QLabel()
        self.rectLabel = QLabel()
        self.sizeLabel = QLabel()
        
        layout = QGridLayout()
        layout.addWidget(Label1,0,0)
        layout.addWidget(self.xLabel,0,1)
        layout.addWidget(Label2,1,0)
        layout.addWidget(self.yLabel,1,1)
        layout.addWidget(Label3,2,0)
        layout.addWidget(self.frameGeoLabel,2,1)
        layout.addWidget(Label4,3,0)
        layout.addWidget(self.posLabel,3,1)
        layout.addWidget(Label5,4,0)
        layout.addWidget(self.geoLabel,4,1)
        layout.addWidget(Label6,5,0)
        layout.addWidget(self.widthLabel,5,1)
        layout.addWidget(Label7,6,0)
        layout.addWidget(self.heightLabel,6,1)
        layout.addWidget(Label8,7,0)
        layout.addWidget(self.rectLabel,7,1)
        layout.addWidget(Label9,8,0)
        layout.addWidget(self.sizeLabel,8,1)
        
        self.setLayout(layout)
        
        self.updateLabel()
        
    def moveEvent(self,event):
        self.updateLabel()
        
    def updateLabel(self):
        temp = QString()
        
        self.xLabel.setText(temp.setNum(self.x(), base=10))
        self.yLabel.setText(temp.setNum(self.y(), base=10))
        
app = QApplication(sys.argv)
form = Geometry()
form.show()
app.exec_()
        
        
        
        
        
        