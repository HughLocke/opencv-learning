import cv2 as cv
import numpy as np

src = cv.imread("01_实验测试图_汇总/04_彩色图像/Fig6.16(a).bmp")
src = cv.cvtColor(src,cv.COLOR_BGR2RGB)
ret = np.zeros(src.shape,src.dtype)

n,m,ch = src.shape
for i in range(n):
    for j in range(m):
        R = src[i,j,0]
        G = src[i,j,1]
        B = src[i,j,2]
        Y = 0.299 * R + 0.587 * G + 0.114 * B
        U = -0.1687 * R - 0.3313 * G + 0.5 * B + 128
        V = 0.5 * R - 0.4187 * G - 0.0813 * B + 128
        ret[i,j] = [Y,U,V]
#src = cv.cvtColor(src,cv.COLOR_RGB2YUV)
cv.imshow("src",src)
cv.imshow("ret",ret)
cv.waitKey(0)
cv.destroyAllWindows()