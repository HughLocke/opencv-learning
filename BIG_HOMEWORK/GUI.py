#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cv2 as cv
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QGridLayout,
                             QLabel, QPushButton,QLineEdit)
import coloring

class win(QDialog):
    def __init__(self):

        # 初始化一个img的ndarray, 用于存储图像
        self.img = np.ndarray(())

        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 400)
        self.btnOpen = QPushButton('Open', self)
        self.btnSave = QPushButton('Save', self)
        self.btnProcess = QPushButton('Classify', self)
        self.btnQuit = QPushButton('Quit', self)
        self.btncoloring = QPushButton('Coloring',self)

        self.thresholdDio = QLineEdit(self)
        self.thresholdDio.move(20,20)
        self.thresholdDio.resize(280,40)
        self.label = QLabel()
        self.thresholdDio.setText("50")

        self.CclKDio = QLineEdit(self)
        self.CclKDio.move(250,20)
        self.CclKDio.resize(200,40)
        self.label = QLabel()
        self.CclKDio.setText("220,250,200,220,60,100")

        self.EclKDio = QLineEdit(self)
        self.EclKDio.move(250,60)
        self.EclKDio.resize(200,40)
        self.label = QLabel()
        self.EclKDio.setText("200,250,160,180,40,50")

        self.BclKDio = QLineEdit(self)
        self.BclKDio.move(250,60)
        self.BclKDio.resize(200,40)
        self.label = QLabel()
        self.BclKDio.setText("225,235,205,215,110,120")
        # 布局设定
        layout = QGridLayout(self)
        layout.addWidget(self.label, 0, 1, 3, 4)
        layout.addWidget(self.btnOpen, 4, 1, 1, 1)
        layout.addWidget(self.btnSave, 4, 2, 1, 1)
        layout.addWidget(self.btnProcess, 4, 3, 1, 1)
        layout.addWidget(self.btnQuit, 4, 4, 1, 1)
        layout.addWidget(self.btncoloring,3,4,1,1)
        layout.addWidget(self.thresholdDio,3,3,1,1)
        layout.addWidget(self.CclKDio,5,3,1,1)
        layout.addWidget(self.EclKDio,6,3,1,1)
        layout.addWidget(self.BclKDio,7,3,1,1)
        # 信号与槽连接, PyQt5与Qt5相同, 信号可绑定普通成员函数
        self.btnOpen.clicked.connect(self.openSlot)
        self.btnSave.clicked.connect(self.saveSlot)
        self.btnProcess.clicked.connect(self.processSlot)
        self.btnQuit.clicked.connect(self.close)
        self.btncoloring.clicked.connect(self.coloring)

    def coloring(self):
        x = int(self.thresholdDio.text())
        EclKList = list(self.EclKDio.text().split(','))
        CclKList = list(self.CclKDio.text().split(','))
        BclKList = list(self.BclKDio.text().split(','))
        EclK = [int(x) for x in EclKList]
        CclK = [int(x) for x in CclKList]
        BclK = [int(x) for x in BclKList]
        print(EclK,CclK,BclK)
        self.img = coloring.colorjn(self.img,EclK,CclK,BclK)
        self.refreshShow()
        print("done")

    def openSlot(self):
        # 调用打开文件diglog
        fileName, tmp = QFileDialog.getOpenFileName(
            self, 'Open Image', './__data', '*.png *.jpg *.bmp')

        if fileName is '':
            return

        # 采用opencv函数读取数据
        self.img = cv.imread(fileName, -1)

        if self.img.size == 1:
            return

        self.refreshShow()

    def saveSlot(self):
        # 调用存储文件dialog
        fileName, tmp = QFileDialog.getSaveFileName(
            self, 'Save Image', './__data', '*.png *.jpg *.bmp', '*.png')

        if fileName is '':
            return
        if self.img.size == 1:
            return

        # 调用opencv写入图像
        cv.imwrite(fileName, self.img)

    def processSlot(self):
        x = int(self.thresholdDio.text())
        EclKList = list(self.EclKDio.text().split(','))
        CclKList = list(self.CclKDio.text().split(','))
        BclKList = list(self.BclKDio.text().split(','))
        print(self.EclKDio.text(),EclKList)
        EclK = [int(x) for x in EclKList]
        CclK = [int(x) for x in CclKList]
        BclK = [int(x) for x in BclKList]
        self.img = coloring.classifyjn(self.img,x,EclK,CclK,BclK)
        print("done")
        self.refreshShow()


    def refreshShow(self):
        # 提取图像的尺寸和通道, 用于将opencv下的image转换成Qimage
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()

        # 将Qimage显示出来
        self.label.setPixmap(QPixmap.fromImage(self.qImg))
'''
杰尼龟
CclK = [30,60,60,120,180,220]
EclK = [80,200,200,255,200,255]
BclK = [180,250,180,240,140,185]
皮卡丘
CclK = 110,120,205,215,225,235
EclK = 40,50,160,180,200,250
BclK = 60,100,200,220,220,250
'''

if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = win()
    w.show()
    sys.exit(a.exec_())