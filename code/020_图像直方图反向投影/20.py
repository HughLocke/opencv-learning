import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def back_projection_demo():
    sample = cv.imread("./Mat.png")
    target = cv.imread("./test.png")
    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)

    cv.imshow("sample",sample)
    cv.imshow("target",target)
    cv.imshow("213",sample)
    roiHist = cv.calcHist([roi_hsv],[0,1],None,[32,32],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)
    cv.imshow("backProjectionDemo",dst)



back_projection_demo()
cv.waitKey(0)
cv.destroyAllWindows()