import cv2 as cv
import numpy as np

src1 = cv.imread('test0.jpg')
src2 = cv.imread('test1.jpg')
#cv.namedWindow('m1',cv.WINDOW_NORMAL)
#cv.namedWindow('m2',cv.WINDOW_NORMAL)
#cv.namedWindow('add_result',cv.WINDOW_NORMAL)

#cv.imshow('m1',src1)
#cv.imshow('m2',src2)

#对两张图进行加减乘的融合
cv.imshow("add_result",cv.add(src1,src2))
cv.imshow("sub_result",cv.subtract(src1,src2))
cv.imshow("mul_result",cv.multiply(src1,src2))
cv.imshow("div_result",cv.divide(src1,src2))

cv.waitKey(0)
cv.destroyAllWindows()
