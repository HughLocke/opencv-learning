import cv2 as cv
import numpy as np

src = cv.imread("01_实验测试图_汇总/04_彩色图像/Fig6.35(1).bmp")
ret = np.zeros(src.shape,src.dtype)
n,m,ch = src.shape
for i in range(n):
    for j in range(m):
        for k in range(2):
            ret[i,j,k] = 255 - src[i,j,k]

cv.imshow("src",src)
cv.imshow("ret",ret)
cv.waitKey(0)
cv.destroyAllWindows()