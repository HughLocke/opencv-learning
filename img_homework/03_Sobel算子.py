import cv2 as cv
import numpy as np
from math import sqrt
src = cv.imread("01_实验测试图_汇总/03_03线性滤波/Fig3.35(a).bmp")
src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("src",src)
ret = np.zeros(src.shape,src.dtype)
n,m = src.shape
for i in range(1,n - 1):
    for j in range(1,m - 1):
        z1 = int(src[i - 1,j - 1])
        z2 = int(src[i - 1, j])
        z3 = int(src[i - 1, j + 1])
        z4 = int(src[i, j - 1])
        z5 = int(src[i, j])
        z6 = int(src[i, j + 1])
        z7 = int(src[i + 1, j - 1])
        z8 = int(src[i + 1, j])
        z9 = int(src[i + 1, j + 1])
        sum = abs(z7+2*z8+z9-z1-2*z2-z3) + abs(z3+2*z6+z9-z1-2*z4-z7)
        ret[i,j] = sum
cv.imshow("ret",ret)
cv.waitKey(0)
cv.destroyAllWindows()